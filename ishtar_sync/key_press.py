import logging
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, Controller as KeyboardController
from PySide6.QtCore import QObject, Signal, QEvent


def convert_key(key):
    if isinstance(key, Key):
        key = key.value
    return key


class KeyPress:
    mouse = MouseController()
    keyboard = KeyboardController()

    def click(self):
        self.mouse.click(Button.left)

    def enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        # Can't use tap because it doesn't exist in 1.6.8, which is needed for pyinstaller...
        # https://stackoverflow.com/questions/63681770/getting-error-when-using-pynput-with-pyinstaller
        # self.keyboard.tap(Key.enter)


# Stolen from https://stackoverflow.com/a/61859909
class KeyMonitor(QObject):
    ready_pressed = Signal()
    increment_pressed = Signal()
    decrement_pressed = Signal()

    # .value() gets the KeyCode() object, which is useful to compare vk values later
    ready_key = Key.home.value
    increment_key = Key.page_up.value
    decrement_key = Key.page_down.value

    def __init__(self, parent=None):
        super().__init__(parent)
        self.listener = Listener(on_release=self.on_release)

    def on_release(self, key):
        key = convert_key(key)  # on_release may return Keys, so we'll convert them into KeyCodes
        logging.debug("Key pressed: " + str(key))
        if key == self.ready_key:
            logging.debug("Ready key " + str(key) + " pressed.")
            self.ready_pressed.emit()
        elif key == self.increment_key:
            logging.debug("Increment key " + str(key) + " pressed.")
            self.increment_pressed.emit()
        elif key == self.decrement_key:
            logging.debug("Decrement key " + str(key) + " pressed.")
            self.decrement_pressed.emit()

    def stop_monitoring(self):
        self.listener.stop()

    def start_monitoring(self):
        self.listener.start()

    def rebind_ready_key(self, key):
        self.ready_key = convert_key(key)

    def rebind_increment_key(self, key):
        self.increment_key = convert_key(key)

    def rebind_decrement_key(self, key):
        self.decrement_key = convert_key(key)


class SpinBoxFilter(QObject):
    def __init__(self, km: KeyMonitor):
        self.km = km
        super().__init__()

    # Camel case isn't exactly "pythonic" but in this case is required by the QT API
    def eventFilter(self, obj: QObject, event: QEvent):
        if event.type() == QEvent.KeyPress or event.type() == QEvent.KeyRelease:
            # We're using vk values to compare QT's keys and pynput's keys.
            key_vk = event.nativeVirtualKey()
            if key_vk == self.km.ready_key.vk or key_vk == self.km.increment_key.vk \
                    or key_vk == self.km.decrement_key.vk:
                return True  # Returning True prevents the QObject from getting the event
        return False
