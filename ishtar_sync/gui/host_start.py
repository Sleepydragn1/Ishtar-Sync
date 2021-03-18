# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'host_start.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_HostStart(object):
    def setupUi(self, HostStart):
        if not HostStart.objectName():
            HostStart.setObjectName(u"HostStart")
        HostStart.resize(400, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HostStart.sizePolicy().hasHeightForWidth())
        HostStart.setSizePolicy(sizePolicy)
        HostStart.setMinimumSize(QSize(400, 280))
        HostStart.setStyleSheet(u"QWidget {\n"
"	font: 12pt \"Arial\";\n"
"}\n"
"QLabel {\n"
"	font: bold 12pt \"Arial\";\n"
"}\n"
"")
        self.verticalLayoutWidget = QWidget(HostStart)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 261))
        self.host_start_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.host_start_layout.setSpacing(0)
        self.host_start_layout.setObjectName(u"host_start_layout")
        self.host_start_layout.setContentsMargins(0, 0, 0, 0)
        self.address_layout = QHBoxLayout()
        self.address_layout.setSpacing(0)
        self.address_layout.setObjectName(u"address_layout")
        self.address_layout.setContentsMargins(-1, 0, 0, -1)
        self.address = QLabel(self.verticalLayoutWidget)
        self.address.setObjectName(u"address")
        self.address.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.address.setFont(font)
        self.address.setAlignment(Qt.AlignCenter)

        self.address_layout.addWidget(self.address)


        self.host_start_layout.addLayout(self.address_layout)

        self.port_layout = QHBoxLayout()
        self.port_layout.setSpacing(10)
        self.port_layout.setObjectName(u"port_layout")
        self.port_layout.setContentsMargins(-1, 0, 15, -1)
        self.port_label = QLabel(self.verticalLayoutWidget)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setMaximumSize(QSize(16777215, 20))
        self.port_label.setFont(font)
        self.port_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.port_label.setWordWrap(False)

        self.port_layout.addWidget(self.port_label)

        self.port = QLineEdit(self.verticalLayoutWidget)
        self.port.setObjectName(u"port")
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setMinimumSize(QSize(240, 0))
        self.port.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.port.setFont(font1)
        self.port.setMaxLength(2000)
        self.port.setAlignment(Qt.AlignCenter)

        self.port_layout.addWidget(self.port)


        self.host_start_layout.addLayout(self.port_layout)

        self.password_layout = QHBoxLayout()
        self.password_layout.setSpacing(10)
        self.password_layout.setObjectName(u"password_layout")
        self.password_layout.setContentsMargins(-1, 0, 15, -1)
        self.password_label = QLabel(self.verticalLayoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(16777215, 20))
        self.password_label.setFont(font)
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_layout.addWidget(self.password_label)

        self.password = QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QSize(240, 0))
        self.password.setBaseSize(QSize(0, 0))
        self.password.setFont(font1)
        self.password.setMaxLength(25)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)

        self.password_layout.addWidget(self.password)


        self.host_start_layout.addLayout(self.password_layout)

        self.start = QPushButton(self.verticalLayoutWidget)
        self.start.setObjectName(u"start")
        self.start.setMinimumSize(QSize(0, 50))
        self.start.setFont(font1)

        self.host_start_layout.addWidget(self.start)

        self.back = QPushButton(self.verticalLayoutWidget)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(0, 50))
        self.back.setFont(font1)

        self.host_start_layout.addWidget(self.back)


        self.retranslateUi(HostStart)

        QMetaObject.connectSlotsByName(HostStart)
    # setupUi

    def retranslateUi(self, HostStart):
        HostStart.setWindowTitle(QCoreApplication.translate("HostStart", u"IshtarSync", None))
        self.address.setText(QCoreApplication.translate("HostStart", u"<html><head/><body><p><span>Address: 127.0.0.1</span></p></body></html>", None))
        self.port_label.setText(QCoreApplication.translate("HostStart", u"<html><head/><body><p>Port</p></body></html>", None))
        self.port.setText("")
        self.port.setPlaceholderText(QCoreApplication.translate("HostStart", u"42401", None))
        self.password_label.setText(QCoreApplication.translate("HostStart", u"<html><head/><body><p>Password</p></body></html>", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("HostStart", u"hunter2", None))
        self.start.setText(QCoreApplication.translate("HostStart", u"Start", None))
        self.back.setText(QCoreApplication.translate("HostStart", u"Back", None))
    # retranslateUi

