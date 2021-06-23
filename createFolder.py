# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createFolder.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Create_folder(object):
    def setupUi(self, Create_folder):
        Create_folder.setObjectName("Create_folder")
        Create_folder.resize(400, 108)
        self.buttonBox = QtWidgets.QDialogButtonBox(Create_folder)
        self.buttonBox.setGeometry(QtCore.QRect(290, 20, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Create_folder)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 20))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Create_folder)
        self.lineEdit.setGeometry(QtCore.QRect(100, 40, 131, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Create_folder)
        self.buttonBox.accepted.connect(Create_folder.accept)
        self.buttonBox.rejected.connect(Create_folder.reject)
        QtCore.QMetaObject.connectSlotsByName(Create_folder)

    def retranslateUi(self, Create_folder):
        _translate = QtCore.QCoreApplication.translate
        Create_folder.setWindowTitle(_translate("Create_folder", "Create New Folder"))
        self.label.setText(_translate("Create_folder", "请输入名称"))

