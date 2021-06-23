# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_name_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_change_name_dlg(object):
    def setupUi(self, change_name_dlg):
        change_name_dlg.setObjectName("change_name_dlg")
        change_name_dlg.resize(387, 103)
        self.buttonBox = QtWidgets.QDialogButtonBox(change_name_dlg)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(change_name_dlg)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 181, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(change_name_dlg)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.label.setObjectName("label")

        self.retranslateUi(change_name_dlg)
        self.buttonBox.accepted.connect(change_name_dlg.accept)
        self.buttonBox.rejected.connect(change_name_dlg.reject)
        QtCore.QMetaObject.connectSlotsByName(change_name_dlg)

    def retranslateUi(self, change_name_dlg):
        _translate = QtCore.QCoreApplication.translate
        change_name_dlg.setWindowTitle(_translate("change_name_dlg", "Dialog"))
        self.label.setText(_translate("change_name_dlg", "新文件名称"))

