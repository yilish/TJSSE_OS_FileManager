# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mw.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
class Ui_MainWindow(object):
    closed = pyqtSignal()
    def closeEvent(self, e):
        self.closed.emit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(780, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(0, 49, 150, 431))
        self.treeView.setStyleSheet("")
        self.treeView.setObjectName("treeView")
        self.treeView.header().setCascadingSectionResizes(False)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 0, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 20, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 133);\n"
"border-radius: 2px 4px;")
        self.textBrowser.setObjectName("textBrowser")
        self.btn_formatting = QtWidgets.QPushButton(self.centralwidget)
        self.btn_formatting.setGeometry(QtCore.QRect(670, 50, 101, 31))
        self.btn_formatting.setStyleSheet("")
        self.btn_formatting.setCheckable(False)
        self.btn_formatting.setObjectName("btn_formatting")
        self.btn_newFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newFolder.setGeometry(QtCore.QRect(670, 140, 101, 31))
        self.btn_newFolder.setStyleSheet("")
        self.btn_newFolder.setCheckable(False)
        self.btn_newFolder.setObjectName("btn_newFolder")
        self.btn_newFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_newFile.setGeometry(QtCore.QRect(670, 190, 101, 31))
        self.btn_newFile.setStyleSheet("")
        self.btn_newFile.setCheckable(False)
        self.btn_newFile.setObjectName("btn_newFile")
        self.lbl_blockSize = QtWidgets.QLabel(self.centralwidget)
        self.lbl_blockSize.setGeometry(QtCore.QRect(670, 410, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_blockSize.setFont(font)
        self.lbl_blockSize.setObjectName("lbl_blockSize")
        self.lbl_diskSize = QtWidgets.QLabel(self.centralwidget)
        self.lbl_diskSize.setGeometry(QtCore.QRect(670, 430, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_diskSize.setFont(font)
        self.lbl_diskSize.setObjectName("lbl_diskSize")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(170, 50, 481, 391))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 15, 58, 31))
        self.label_2.setObjectName("label_2")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(550, 20, 100, 21))
        self.btn_back.setObjectName("btn_back")
        self.btn_delFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delFile.setGeometry(QtCore.QRect(670, 230, 101, 31))
        self.btn_delFile.setStyleSheet("")
        self.btn_delFile.setCheckable(False)
        self.btn_delFile.setObjectName("btn_delFile")
        self.btn_changeName = QtWidgets.QPushButton(self.centralwidget)
        self.btn_changeName.setGeometry(QtCore.QRect(670, 270, 101, 31))
        self.btn_changeName.setStyleSheet("")
        self.btn_changeName.setCheckable(False)
        self.btn_changeName.setObjectName("btn_changeName")
        self.search_text = QtWidgets.QLineEdit(self.centralwidget)
        self.search_text.setGeometry(QtCore.QRect(40, 20, 101, 21))
        self.search_text.setStyleSheet("background-color: rgba(255, 255, 255, 133);\n"
"border-radius: 2px 4px;")
        self.search_text.setObjectName("search_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "当前路径"))
        self.btn_formatting.setText(_translate("MainWindow", "格式化"))
        self.btn_newFolder.setText(_translate("MainWindow", "新建文件夹"))
        self.btn_newFile.setText(_translate("MainWindow", "新建文件"))
        self.lbl_blockSize.setText(_translate("MainWindow", "当前盘块大小:"))
        self.lbl_diskSize.setText(_translate("MainWindow", "当前磁盘大小:"))
        self.label_2.setText(_translate("MainWindow", "搜索"))
        self.btn_back.setText(_translate("MainWindow", "返回上级"))
        self.btn_delFile.setText(_translate("MainWindow", "删除文件"))
        self.btn_changeName.setText(_translate("MainWindow", "修改文件名"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

