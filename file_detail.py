# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_detail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal



class Ui_file_dialog(object):
    closed = pyqtSignal()
    def setupUi(self, file_dialog):
        file_dialog.setObjectName("file_dialog")
        file_dialog.resize(403, 303)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(file_dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(file_dialog)
        QtCore.QMetaObject.connectSlotsByName(file_dialog)

    def retranslateUi(self, file_dialog):
        _translate = QtCore.QCoreApplication.translate
        file_dialog.setWindowTitle(_translate("file_dialog", "Dialog"))


    def closeEvent(self, event):
        self.closed.emit()
        pass

