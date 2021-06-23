# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popup.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 251, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 40, 251, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 90, 251, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 110, 251, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 130, 251, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(50, 160, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 200, 91, 16))
        self.label_7.setObjectName("label_7")
        self.txt_diskCapacity = QtWidgets.QLineEdit(Dialog)
        self.txt_diskCapacity.setGeometry(QtCore.QRect(140, 160, 91, 21))
        self.txt_diskCapacity.setObjectName("txt_diskCapacity")
        self.txt_blockSize = QtWidgets.QLineEdit(Dialog)
        self.txt_blockSize.setGeometry(QtCore.QRect(140, 200, 91, 21))
        self.txt_blockSize.setObjectName("txt_blockSize")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tongji SSE 2020 - 2021 Spring"))
        self.label_2.setText(_translate("Dialog", "OS Project3 - File Manager"))
        self.label_3.setText(_translate("Dialog", "Author: Yili Shen"))
        self.label_4.setText(_translate("Dialog", "Student Number: 1851009"))
        self.label_5.setText(_translate("Dialog", "Teacher: Dongqing Wang"))
        self.label_6.setText(_translate("Dialog", "磁盘容量(B):"))
        self.label_7.setText(_translate("Dialog", "块大小(B):"))
        self.txt_diskCapacity.setText(_translate("Dialog", "1000"))
        self.txt_blockSize.setText(_translate("Dialog", "2"))

