# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkoutdialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 564)
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 200, 251, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 200, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 170, 501, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.recvCash = QtWidgets.QLineEdit(Dialog)
        self.recvCash.setGeometry(QtCore.QRect(110, 10, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.recvCash.setFont(font)
        self.recvCash.setObjectName("recvCash")
        self.okBtn = QtWidgets.QPushButton(Dialog)
        self.okBtn.setGeometry(QtCore.QRect(350, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.okBtn.setFont(font)
        self.okBtn.setObjectName("okBtn")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 391, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_5B.setFont(font)
        self.pushButton_5B.setObjectName("pushButton_5B")
        self.gridLayout.addWidget(self.pushButton_5B, 0, 0, 1, 1)
        self.pushButton_10B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_10B.setFont(font)
        self.pushButton_10B.setObjectName("pushButton_10B")
        self.gridLayout.addWidget(self.pushButton_10B, 0, 1, 1, 1)
        self.pushButton_20B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_20B.setFont(font)
        self.pushButton_20B.setObjectName("pushButton_20B")
        self.gridLayout.addWidget(self.pushButton_20B, 0, 2, 1, 1)
        self.pushButton_500B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_500B.setFont(font)
        self.pushButton_500B.setObjectName("pushButton_500B")
        self.gridLayout.addWidget(self.pushButton_500B, 1, 2, 1, 1)
        self.pushButton_50B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_50B.setFont(font)
        self.pushButton_50B.setObjectName("pushButton_50B")
        self.gridLayout.addWidget(self.pushButton_50B, 1, 0, 1, 1)
        self.pushButton_100B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_100B.setFont(font)
        self.pushButton_100B.setObjectName("pushButton_100B")
        self.gridLayout.addWidget(self.pushButton_100B, 1, 1, 1, 1)
        self.pushButton_1000B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_1000B.setFont(font)
        self.pushButton_1000B.setObjectName("pushButton_1000B")
        self.gridLayout.addWidget(self.pushButton_1000B, 0, 3, 1, 1)
        self.pushButton_3000B = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_3000B.setFont(font)
        self.pushButton_3000B.setObjectName("pushButton_3000B")
        self.gridLayout.addWidget(self.pushButton_3000B, 1, 3, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(240, 300, 251, 81))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_3.setGeometry(QtCore.QRect(240, 390, 251, 81))
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 390, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 480, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 500, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_5B.clicked.connect(partial(Dialog.insertMoneyBtn,5))
        self.pushButton_10B.clicked.connect(partial(Dialog.insertMoneyBtn,10))
        self.pushButton_20B.clicked.connect(partial(Dialog.insertMoneyBtn,20))
        self.pushButton_50B.clicked.connect(partial(Dialog.insertMoneyBtn,50))
        self.pushButton_100B.clicked.connect(partial(Dialog.insertMoneyBtn,100))
        self.pushButton_500B.clicked.connect(partial(Dialog.insertMoneyBtn,500))
        self.pushButton_1000B.clicked.connect(partial(Dialog.insertMoneyBtn,1000))
        self.pushButton_3000B.clicked.connect(partial(Dialog.insertMoneyBtn,3000))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "ราคารวม"))
        self.label_2.setText(_translate("Dialog", "รับเงินมา"))
        self.okBtn.setText(_translate("Dialog", "ตกลง (enter)"))
        self.pushButton_5B.setText(_translate("Dialog", "5"))
        self.pushButton_10B.setText(_translate("Dialog", "10"))
        self.pushButton_20B.setText(_translate("Dialog", "20"))
        self.pushButton_500B.setText(_translate("Dialog", "500"))
        self.pushButton_50B.setText(_translate("Dialog", "50"))
        self.pushButton_100B.setText(_translate("Dialog", "100"))
        self.pushButton_1000B.setText(_translate("Dialog", "1000"))
        self.pushButton_3000B.setText(_translate("Dialog", "3000"))
        self.label_3.setText(_translate("Dialog", "เงินทอน"))
        self.label_4.setText(_translate("Dialog", "รับเงินมา"))
        self.pushButton.setText(_translate("Dialog", "ออก (esc)"))
