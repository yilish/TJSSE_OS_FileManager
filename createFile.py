# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createFile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Create_dlg(object):
    def setupUi(self, Create_dlg):
        Create_dlg.setObjectName("Create_dlg")
        Create_dlg.resize(400, 108)
        self.buttonBox = QtWidgets.QDialogButtonBox(Create_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Create_dlg)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Create_dlg)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Create_dlg)
        self.buttonBox.accepted.connect(Create_dlg.accept)
        self.buttonBox.rejected.connect(Create_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(Create_dlg)

    def retranslateUi(self, Create_dlg):
        _translate = QtCore.QCoreApplication.translate
        Create_dlg.setWindowTitle(_translate("Create_dlg", "Create New File"))
        self.label.setText(_translate("Create_dlg", "请输入名称"))

