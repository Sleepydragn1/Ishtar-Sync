import time
import logging
import urllib.request
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, QThread, QMutex, Signal, Slot, QRegularExpression
from PySide6.QtGui import QIntValidator, QRegularExpressionValidator
from .start import Ui_Start
from .host_start import Ui_HostStart
from .host_main import Ui_HostMain
from .client_start import Ui_ClientStart
from .client_main import Ui_ClientMain
from .resizing_stacked_widget import QResizingStackedWidget
from host import Host  # Ignore PyCharm's ire, these are meant to be imported from within the IshtarSync package
from client import Client


port_validator = QIntValidator(1024, 65535)                                         # 1024-65535
password_validator = QRegularExpressionValidator(QRegularExpression("[^|]{1,25}"))  # Basically, just don't use |, idiot


class StartWidget(QWidget):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window

        super(StartWidget, self).__init__()
        self.ui = Ui_Start()
        self.ui.setupUi(self)

        self.ui.host.clicked.connect(self.host)
        self.ui.join.clicked.connect(self.join)

    def host(self):
        self.window.setCurrentIndex(self.window.w["host_start"])

    def join(self):
        self.window.setCurrentIndex(self.window.w["client_start"])


class HostStartWidget(QWidget):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window

        super().__init__()
        self.ui = Ui_HostStart()
        self.ui.setupUi(self)

        self.ui.port.setValidator(port_validator)
        self.ui.password.setValidator(password_validator)

        # Stolen from: https://stackoverflow.com/a/41432835
        self.ui.address.setText(
           f"Address: {urllib.request.urlopen('https://checkip.amazonaws.com').read().decode('utf8')}".strip())

        self.thread = QThread()
        self.worker = None

    # Run after window has had all widgets added
    def setup(self):
        self.worker = HostWorker(self.window)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        # self.worker.error.connect(self.error)

        self.ui.start.clicked.connect(self.start)
        self.ui.back.clicked.connect(self.back)

        # Connect up host main's buttons
        host_main = self.window.widget(self.window.w["host_main"])
        host_main.ui.ready.clicked.connect(self.ready)
        host_main.ui.stop.clicked.connect(self.stop)

    def start(self):
        self.ui.start.setEnabled(False)
        # Stylesheets allow changed text to keep its styling without HTML tags
        self.window.widget(self.window.w["host_main"]).ui.port.setText(f"Port: {self.ui.port.text()}")
        self.thread.start()
        self.window.setCurrentIndex(self.window.w["host_main"])
        self.ui.start.setEnabled(True)

    def back(self):
        self.window.setCurrentIndex(self.window.w["start"])

    def error(self, exception):
        self.window.setCurrentIndex(self.window.w["host_start"])

    # Methods for communicating to HostWorker
    def ready(self):
        self.window.hw_ready = True

    def stop(self):
        self.window.hw_stop = True


class HostWorker(QObject):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window
        self.host = None

        self.error = Signal(Exception)

        super().__init__()

    def run(self):
        logging.info("Host worker thread started.")
        #self.host = Host(44444, "a")
        ui = self.window.widget(self.window.w["host_start"]).ui
        self.host = Host(int(ui.port.text()), ui.password.text())  # Cast port to int
        while True:
            # Look for communication from the main thread
            if self.window.hw_ready:
                self.ready()
            if self.window.hw_stop:
                self.stop()
                break
            logging.debug("Host io_loop running...")
            if self.host.io_loop():
                logging.info("Clicking!")
                self.window.kp.click()
                self.window.widget(self.window.w["host_main"]).ui.ready.setEnabled(True)

    def ready(self):
        logging.info("Host worker executing ready!")
        self.window.hw_ready = False
        self.window.widget(self.window.w["host_main"]).ui.ready.setEnabled(False)  # Disable the Ready button
        self.host.ready()

    def stop(self):
        logging.info("Host worker executing stop!")
        self.window.hw_stop = False
        self.host.cleanup()
        self.window.setCurrentIndex(self.window.w["host_start"])  # Go back to host start


class HostMainWidget(QWidget):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window

        super(HostMainWidget, self).__init__()
        self.ui = Ui_HostMain()
        self.ui.setupUi(self)

        window.currentChanged.connect(self.register_keybinds)

    @Slot()
    def click_ready(self):
        self.ui.ready.animateClick()

    @Slot(int)
    def register_keybinds(self, active_index):
        if active_index == self.window.w["host_main"]:
            self.window.currentChanged.disconnect(self.register_keybinds)
            self.window.currentChanged.connect(self.unregister_keybinds)

            self.window.km.ready_pressed.connect(self.click_ready)

    @Slot()
    def unregister_keybinds(self):
        self.window.currentChanged.connect(self.register_keybinds)

        # Disconnects all signals, but that's okay as nothing else should be connected
        self.window.km.ready_pressed.disconnect()


class ClientStartWidget(QWidget):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window

        super(ClientStartWidget, self).__init__()
        self.ui = Ui_ClientStart()
        self.ui.setupUi(self)

        self.ui.port.setValidator(port_validator)
        self.ui.password.setValidator(password_validator)

        self.thread = QThread()
        self.worker = None

    # Run after window has had all widgets added
    def setup(self):
        self.worker = ClientWorker(self.window)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)

        self.ui.connect.clicked.connect(self.start)
        self.ui.back.clicked.connect(self.back)

        # Connect up client main's buttons
        client_main = self.window.widget(self.window.w["client_main"])
        client_main.ui.ready.clicked.connect(self.ready)
        client_main.ui.disconnect.clicked.connect(self.stop)

    def start(self):
        self.ui.connect.setEnabled(False)
        self.thread.start()
        self.window.setCurrentIndex(self.window.w["client_main"])
        self.ui.connect.setEnabled(True)

    def back(self):
        self.window.setCurrentIndex(self.window.w["start"])

    # Methods for communicating to ClientWorker
    def ready(self):
        self.window.cw_ready = True

    def stop(self):
        self.window.cw_stop = True


class ClientWorker(QObject):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window
        self.client = None

        self.error = Signal(Exception)

        super().__init__()

    def run(self):
        logging.info("Client worker thread started.")
        # self.client = Client("127.0.0.1", 44444, "a")
        ui = self.window.widget(self.window.w["client_start"]).ui
        self.client = Client(ui.address.text(), int(ui.port.text()), ui.password.text())  # Cast port to int
        while True:
            # Look for communication from the main thread
            if self.window.cw_ready:
                self.ready()
            if self.window.cw_stop:
                self.stop()
                break
            logging.debug("Client io_loop running...")
            if self.client.io_loop():
                logging.info("Waiting to hit enter...")
                # Wait for the specified delay
                time.sleep(self.window.widget(self.window.w["client_main"]).ui.delay.value())
                self.window.kp.enter()
                self.window.widget(self.window.w["client_main"]).ui.ready.setEnabled(True)
                logging.info("Enter hit!")

    def ready(self):
        logging.info("Client worker executing ready!")
        self.window.cw_ready = False
        # Disable the Ready button
        self.window.widget(self.window.w["client_main"]).ui.ready.setEnabled(False)
        self.client.ready()

    def stop(self):
        logging.info("Client worker executing stop!")
        self.window.cw_stop = False
        self.client.cleanup()
        self.window.setCurrentIndex(self.window.w["client_start"])  # Go back to client start


class ClientMainWidget(QWidget):
    def __init__(self, window: QResizingStackedWidget):
        self.window = window

        super(ClientMainWidget, self).__init__()
        self.ui = Ui_ClientMain()
        self.ui.setupUi(self)

        window.currentChanged.connect(self.register_keybinds)

    @Slot()
    def click_ready(self):
        self.ui.ready.animateClick()

    @Slot()
    def increment(self):
        logging.debug("Delay val: " + str(self.ui.delay.value()))
        logging.debug("Step val: " + str(self.ui.step.value()))
        self.ui.delay.setValue(self.ui.delay.value() + self.ui.step.value())

    @Slot()
    def decrement(self):
        self.ui.delay.setValue(self.ui.delay.value() - self.ui.step.value())

    @Slot(int)
    def register_keybinds(self, active_index):
        if active_index == 4:
            # The old switcharoo
            self.window.currentChanged.disconnect(self.register_keybinds)
            self.window.currentChanged.connect(self.unregister_keybinds)

            self.window.km.ready_pressed.connect(self.click_ready)
            self.window.km.increment_pressed.connect(self.increment)
            self.window.km.decrement_pressed.connect(self.decrement)

    @Slot()
    def unregister_keybinds(self):
        self.window.currentChanged.connect(self.register_keybinds)

        # Disconnects all signals, but that's okay as nothing else should be connected
        self.window.km.ready_pressed.disconnect()
        self.window.km.increment_pressed.disconnect()
        self.window.km.decrement_pressed.disconnect()
