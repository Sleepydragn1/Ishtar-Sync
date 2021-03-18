from PySide6.QtWidgets import QStackedWidget, QWidget


class QResizingStackedWidget(QStackedWidget):
    def setCurrentIndex(self, index: int):
        self.setFixedSize(self.widget(index).size())

        super(QResizingStackedWidget, self).setCurrentIndex(index)

    def setCurrentWidget(self, w: QWidget):
        self.setFixedSize(w.size())
        super(QResizingStackedWidget, self).setCurrentWidget(w)
