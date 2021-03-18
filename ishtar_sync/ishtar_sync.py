import sys
import argparse
import logging
from PySide6.QtWidgets import QApplication
from key_press import KeyPress, KeyMonitor, SpinBoxFilter
from gui.resizing_stacked_widget import QResizingStackedWidget
from gui.widgets import StartWidget, HostStartWidget, HostMainWidget, ClientStartWidget, ClientMainWidget


# Execute this directly, you probably shouldn't be trying to import it
if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log_level", help="specify log level")
    args = parser.parse_args()
    if args.log_level:
        logging.basicConfig(level=getattr(logging, args.log_level.upper()))
    else:
        logging.basicConfig(level=logging.WARN)

    app = QApplication()
    app.setApplicationDisplayName("Ishtar Sync")
    window = QResizingStackedWidget()
    window.kp = KeyPress()
    window.km = KeyMonitor()
    # Convenience dict for human-readable widget names
    window.w = {
        "start": 0,
        "host_start": 1,
        "host_main": 2,
        "client_start": 3,
        "client_main": 4
    }
    # Widget communication flags
    # We could use QMutex here, but I don't think it's necessary...
    window.hw_ready = False
    window.hw_stop = False
    window.cw_ready = False
    window.cw_stop = False

    start_widget = StartWidget(window)                  # index 0
    host_start_widget = HostStartWidget(window)         # index 1
    host_main_widget = HostMainWidget(window)           # index 2
    client_start_widget = ClientStartWidget(window)     # index 3
    client_main_widget = ClientMainWidget(window)       # index 4

    window.addWidget(start_widget)
    window.addWidget(host_start_widget)
    window.addWidget(host_main_widget)
    window.addWidget(client_start_widget)
    window.addWidget(client_main_widget)

    # Install filter to prevent capture of hotkeys on the spin boxes
    sbf = SpinBoxFilter(window.km)
    window.widget(window.w["client_main"]).ui.delay.installEventFilter(sbf)
    window.widget(window.w["client_main"]).ui.step.installEventFilter(sbf)

    # Contains code that requires other widgets to be added to window
    host_start_widget.setup()
    client_start_widget.setup()

    window.km.start_monitoring()

    window.show()
    window.setCurrentIndex(0)  # Needed to run resizing code

    logging.info("Startup done.")

    sys.exit(app.exec_())
