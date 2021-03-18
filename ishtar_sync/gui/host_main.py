# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'host_main.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_HostMain(object):
    def setupUi(self, HostMain):
        if not HostMain.objectName():
            HostMain.setObjectName(u"HostMain")
        HostMain.resize(400, 170)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HostMain.sizePolicy().hasHeightForWidth())
        HostMain.setSizePolicy(sizePolicy)
        HostMain.setMinimumSize(QSize(400, 170))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        HostMain.setFont(font)
        HostMain.setStyleSheet(u"QWidget {\n"
"	font: 12pt \"Arial\";\n"
"}\n"
"QLabel {\n"
"	font: bold 12pt \"Arial\";\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(HostMain)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 381, 151))
        self.host_main_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.host_main_layout.setSpacing(0)
        self.host_main_layout.setObjectName(u"host_main_layout")
        self.host_main_layout.setContentsMargins(0, 0, 0, 0)
        self.port_layout = QHBoxLayout()
        self.port_layout.setSpacing(10)
        self.port_layout.setObjectName(u"port_layout")
        self.port_layout.setContentsMargins(-1, 0, 15, -1)
        self.port = QLabel(self.verticalLayoutWidget_2)
        self.port.setObjectName(u"port")
        self.port.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(True)
        self.port.setFont(font1)
        self.port.setStyleSheet(u"")
        self.port.setAlignment(Qt.AlignCenter)

        self.port_layout.addWidget(self.port)


        self.host_main_layout.addLayout(self.port_layout)

        self.ready = QPushButton(self.verticalLayoutWidget_2)
        self.ready.setObjectName(u"ready")
        self.ready.setMinimumSize(QSize(0, 50))
        self.ready.setFont(font)

        self.host_main_layout.addWidget(self.ready)

        self.stop = QPushButton(self.verticalLayoutWidget_2)
        self.stop.setObjectName(u"stop")
        self.stop.setMinimumSize(QSize(0, 50))
        self.stop.setFont(font)

        self.host_main_layout.addWidget(self.stop)


        self.retranslateUi(HostMain)

        QMetaObject.connectSlotsByName(HostMain)
    # setupUi

    def retranslateUi(self, HostMain):
        HostMain.setWindowTitle(QCoreApplication.translate("HostMain", u"IshtarSync", None))
        self.port.setText(QCoreApplication.translate("HostMain", u"<html><head/><body><p>Port: 42401</p></body></html>", None))
        self.ready.setText(QCoreApplication.translate("HostMain", u"Ready", None))
        self.stop.setText(QCoreApplication.translate("HostMain", u"Stop", None))
    # retranslateUi

