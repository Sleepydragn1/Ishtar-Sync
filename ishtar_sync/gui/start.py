# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Start(object):
    def setupUi(self, Start):
        if not Start.objectName():
            Start.setObjectName(u"Start")
        Start.resize(400, 180)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Start.sizePolicy().hasHeightForWidth())
        Start.setSizePolicy(sizePolicy)
        Start.setMinimumSize(QSize(400, 180))
        Start.setMaximumSize(QSize(400, 180))
        Start.setFocusPolicy(Qt.NoFocus)
        Start.setStyleSheet(u"QWidget {\n"
"	font: 12pt \"Arial\";\n"
"}")
        self.verticalLayoutWidget_2 = QWidget(Start)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(40, 20, 321, 141))
        self.connection_layout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.connection_layout.setObjectName(u"connection_layout")
        self.connection_layout.setContentsMargins(0, 0, 0, 0)
        self.host = QPushButton(self.verticalLayoutWidget_2)
        self.host.setObjectName(u"host")
        self.host.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.host.setFont(font)

        self.connection_layout.addWidget(self.host)

        self.join = QPushButton(self.verticalLayoutWidget_2)
        self.join.setObjectName(u"join")
        self.join.setMinimumSize(QSize(0, 50))
        self.join.setFont(font)

        self.connection_layout.addWidget(self.join)


        self.retranslateUi(Start)

        QMetaObject.connectSlotsByName(Start)
    # setupUi

    def retranslateUi(self, Start):
        Start.setWindowTitle(QCoreApplication.translate("Start", u"IshtarSync", None))
        self.host.setText(QCoreApplication.translate("Start", u"Host", None))
        self.join.setText(QCoreApplication.translate("Start", u"Join", None))
    # retranslateUi

