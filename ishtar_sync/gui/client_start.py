# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_start.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ClientStart(object):
    def setupUi(self, ClientStart):
        if not ClientStart.objectName():
            ClientStart.setObjectName(u"ClientStart")
        ClientStart.resize(400, 280)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ClientStart.sizePolicy().hasHeightForWidth())
        ClientStart.setSizePolicy(sizePolicy)
        ClientStart.setMinimumSize(QSize(400, 280))
        ClientStart.setStyleSheet(u"QWidget {\n"
"	font: 12pt \"Arial\";\n"
"}\n"
"QLabel {\n"
"	font: bold 12pt \"Arial\";\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(ClientStart)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 381, 261))
        self.client_start_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.client_start_layout.setSpacing(0)
        self.client_start_layout.setObjectName(u"client_start_layout")
        self.client_start_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.client_start_layout.setContentsMargins(0, 0, 0, 0)
        self.address_layout = QHBoxLayout()
        self.address_layout.setSpacing(10)
        self.address_layout.setObjectName(u"address_layout")
        self.address_layout.setContentsMargins(-1, 0, 15, -1)
        self.address_label = QLabel(self.verticalLayoutWidget_2)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        self.address_label.setFont(font)
        self.address_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.address_layout.addWidget(self.address_label)

        self.address = QLineEdit(self.verticalLayoutWidget_2)
        self.address.setObjectName(u"address")
        sizePolicy.setHeightForWidth(self.address.sizePolicy().hasHeightForWidth())
        self.address.setSizePolicy(sizePolicy)
        self.address.setMinimumSize(QSize(240, 0))
        self.address.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.address.setFont(font1)
        self.address.setMaxLength(2000)
        self.address.setAlignment(Qt.AlignCenter)

        self.address_layout.addWidget(self.address, 0, Qt.AlignHCenter)


        self.client_start_layout.addLayout(self.address_layout)

        self.port_layout = QHBoxLayout()
        self.port_layout.setSpacing(10)
        self.port_layout.setObjectName(u"port_layout")
        self.port_layout.setContentsMargins(-1, 0, 15, -1)
        self.port_label = QLabel(self.verticalLayoutWidget_2)
        self.port_label.setObjectName(u"port_label")
        self.port_label.setMaximumSize(QSize(16777215, 20))
        self.port_label.setFont(font)
        self.port_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.port_label.setWordWrap(False)

        self.port_layout.addWidget(self.port_label)

        self.port = QLineEdit(self.verticalLayoutWidget_2)
        self.port.setObjectName(u"port")
        sizePolicy.setHeightForWidth(self.port.sizePolicy().hasHeightForWidth())
        self.port.setSizePolicy(sizePolicy)
        self.port.setMinimumSize(QSize(240, 0))
        self.port.setBaseSize(QSize(0, 0))
        self.port.setFont(font1)
        self.port.setMaxLength(5)
        self.port.setAlignment(Qt.AlignCenter)

        self.port_layout.addWidget(self.port, 0, Qt.AlignHCenter)


        self.client_start_layout.addLayout(self.port_layout)

        self.password_layout = QHBoxLayout()
        self.password_layout.setSpacing(10)
        self.password_layout.setObjectName(u"password_layout")
        self.password_layout.setContentsMargins(-1, 0, 15, -1)
        self.password_label = QLabel(self.verticalLayoutWidget_2)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setMaximumSize(QSize(16777215, 20))
        self.password_label.setFont(font)
        self.password_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.password_layout.addWidget(self.password_label)

        self.password = QLineEdit(self.verticalLayoutWidget_2)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setMinimumSize(QSize(240, 0))
        self.password.setBaseSize(QSize(0, 0))
        self.password.setFont(font1)
        self.password.setMaxLength(25)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)

        self.password_layout.addWidget(self.password, 0, Qt.AlignHCenter)


        self.client_start_layout.addLayout(self.password_layout)

        self.connect = QPushButton(self.verticalLayoutWidget_2)
        self.connect.setObjectName(u"connect")
        self.connect.setMinimumSize(QSize(0, 50))
        self.connect.setFont(font1)

        self.client_start_layout.addWidget(self.connect)

        self.back = QPushButton(self.verticalLayoutWidget_2)
        self.back.setObjectName(u"back")
        self.back.setMinimumSize(QSize(0, 50))
        self.back.setFont(font1)

        self.client_start_layout.addWidget(self.back)


        self.retranslateUi(ClientStart)

        QMetaObject.connectSlotsByName(ClientStart)
    # setupUi

    def retranslateUi(self, ClientStart):
        ClientStart.setWindowTitle(QCoreApplication.translate("ClientStart", u"IshtarSync", None))
        self.address_label.setText(QCoreApplication.translate("ClientStart", u"<html><head/><body><p>Address</p></body></html>", None))
        self.address.setText("")
        self.address.setPlaceholderText(QCoreApplication.translate("ClientStart", u"127.0.0.1", None))
        self.port_label.setText(QCoreApplication.translate("ClientStart", u"<html><head/><body><p>Port</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.port.setToolTip(QCoreApplication.translate("ClientStart", u"The port number for the server. [1-65535]", None))
#endif // QT_CONFIG(tooltip)
        self.port.setText("")
        self.port.setPlaceholderText(QCoreApplication.translate("ClientStart", u"42401", None))
        self.password_label.setText(QCoreApplication.translate("ClientStart", u"<html><head/><body><p>Password</p></body></html>", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("ClientStart", u"hunter2", None))
        self.connect.setText(QCoreApplication.translate("ClientStart", u"Connect", None))
        self.back.setText(QCoreApplication.translate("ClientStart", u"Back", None))
    # retranslateUi

