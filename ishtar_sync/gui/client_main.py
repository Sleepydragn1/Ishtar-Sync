# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ClientMain(object):
    def setupUi(self, ClientMain):
        if not ClientMain.objectName():
            ClientMain.setObjectName(u"ClientMain")
        ClientMain.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClientMain.sizePolicy().hasHeightForWidth())
        ClientMain.setSizePolicy(sizePolicy)
        ClientMain.setMinimumSize(QSize(400, 400))
        ClientMain.setStyleSheet(u"QWidget {\n"
"	font: 12pt \"Arial\";\n"
"}\n"
"QDoubleSpinBox {\n"
"	font: 32pt \"Arial\";\n"
"}\n"
"QLabel {\n"
"	font: bold 12pt \"Arial\";\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(ClientMain)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(100, 20, 201, 201))
        self.timing_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.timing_layout.setSpacing(0)
        self.timing_layout.setObjectName(u"timing_layout")
        self.timing_layout.setContentsMargins(0, 0, 0, 0)
        self.delay_label = QLabel(self.verticalLayoutWidget_2)
        self.delay_label.setObjectName(u"delay_label")
        self.delay_label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.delay_label.setFont(font)
        self.delay_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.timing_layout.addWidget(self.delay_label)

        self.delay = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.delay.setObjectName(u"delay")
        sizePolicy.setHeightForWidth(self.delay.sizePolicy().hasHeightForWidth())
        self.delay.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        brush2 = QBrush(QColor(0, 120, 215, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.delay.setPalette(palette)
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(32)
        font1.setBold(False)
        font1.setItalic(False)
        self.delay.setFont(font1)
        self.delay.setWrapping(False)
        self.delay.setFrame(True)
        self.delay.setAlignment(Qt.AlignCenter)
        self.delay.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.delay.setKeyboardTracking(True)
        self.delay.setDecimals(3)
        self.delay.setMaximum(10.000000000000000)
        self.delay.setSingleStep(0.005000000000000)
        self.delay.setValue(1.000000000000000)

        self.timing_layout.addWidget(self.delay, 0, Qt.AlignHCenter)

        self.step_label = QLabel(self.verticalLayoutWidget_2)
        self.step_label.setObjectName(u"step_label")
        self.step_label.setMaximumSize(QSize(16777215, 20))
        self.step_label.setFont(font)
        self.step_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.timing_layout.addWidget(self.step_label)

        self.step = QDoubleSpinBox(self.verticalLayoutWidget_2)
        self.step.setObjectName(u"step")
        sizePolicy.setHeightForWidth(self.step.sizePolicy().hasHeightForWidth())
        self.step.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Active, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush1)
        self.step.setPalette(palette1)
        self.step.setFont(font1)
        self.step.setFocusPolicy(Qt.ClickFocus)
        self.step.setWrapping(False)
        self.step.setFrame(True)
        self.step.setAlignment(Qt.AlignCenter)
        self.step.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.step.setKeyboardTracking(True)
        self.step.setDecimals(3)
        self.step.setMinimum(0.010000000000000)
        self.step.setMaximum(1.000000000000000)
        self.step.setSingleStep(0.010000000000000)
        self.step.setValue(0.050000000000000)

        self.timing_layout.addWidget(self.step, 0, Qt.AlignHCenter)

        self.verticalLayoutWidget_3 = QWidget(ClientMain)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 250, 361, 131))
        self.button_layout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.button_layout.setSpacing(0)
        self.button_layout.setObjectName(u"button_layout")
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.ready = QPushButton(self.verticalLayoutWidget_3)
        self.ready.setObjectName(u"ready")
        self.ready.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.ready.setFont(font2)

        self.button_layout.addWidget(self.ready)

        self.disconnect = QPushButton(self.verticalLayoutWidget_3)
        self.disconnect.setObjectName(u"disconnect")
        self.disconnect.setMinimumSize(QSize(0, 50))
        self.disconnect.setFont(font2)

        self.button_layout.addWidget(self.disconnect)


        self.retranslateUi(ClientMain)

        QMetaObject.connectSlotsByName(ClientMain)
    # setupUi

    def retranslateUi(self, ClientMain):
        ClientMain.setWindowTitle(QCoreApplication.translate("ClientMain", u"IshtarSync", None))
        self.delay_label.setText(QCoreApplication.translate("ClientMain", u"<html><head/><body><p align=\"center\">Delay</p></body></html>", None))
        self.step_label.setText(QCoreApplication.translate("ClientMain", u"<html><head/><body><p align=\"center\">Step</p></body></html>", None))
        self.ready.setText(QCoreApplication.translate("ClientMain", u"Ready", None))
        self.disconnect.setText(QCoreApplication.translate("ClientMain", u"Disconnect", None))
    # retranslateUi

