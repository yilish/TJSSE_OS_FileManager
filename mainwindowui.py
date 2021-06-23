# -*- coding: utf-8 -*-
# @Time    : 2021/06/22
# @Author  : Yili Shen
# @Email   : 1851009@tongji.edu.cn
# @File    : mainwindowui.py
# @Software: PyCharm Python3.9 MacOS 10.15.3



import sys

# from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QMainWindow, QLabel, \
    QPushButton
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt

# 左侧放文件树形目录
# class App(QWidget):
    #
    # def __init__(self):
    #     super().__init__()
    #     self.titie = "File Manager"
    #     """用于设置窗体距屏幕左边的距离"""
    #     self.left = 20
    #     """用于设置窗体距屏幕上方的距离"""
    #     self.top = 20
    #     """用于设置窗体的宽度"""
    #     self.width = 640
    #     """用于设置窗体的高度"""
    #     self.height = 480
    #     self.initUI()
    #
    #
    # def initUI(self):
    #     """设置窗体的标题"""
    #     self.setWindowTitle(self.titie)
    #     """使用setGeometry(left, top, width, height)方法设置窗体的参数"""
    #     self.setGeometry(self.left, self.top, self.width, self.height)
    #     self.tree = QTreeView(self.window())
    #
    #     """通过调用show()函数来显示窗口"""
    #     self.show()
    #     self.tree.setAnimated(False)
    #     self.tree.setIndentation(20)
    #     self.tree.setSortingEnabled(True)
    #     # self.model = QFileSystemModel()
    #     # self.tree.setModel(self.model)
    #     # windowLayout = QVBoxLayout()
    #     # windowLayout.addWidget(self.tree)
    #     # self.setLayout(windowLayout)


class mainwindowui(QWidget):
    def __init__(self):
        super(mainwindowui, self).__init__()


    def initUI(self, mw: QMainWindow):
        mw.resize(640, 480)


        mw.setWindowTitle('File Manager')
        self.tree = left_tree_view()
        self.tree.init_left_tree_view(mw)
        # self.button = QPushButton(mw)
        # self.button.setGeometry(0, 0, 100, 100)
        # self.button.setText('1234')
        # mw.show()
        # mw.initUI()

class left_tree_view(QWidget):
    def __init__(self):
        super(left_tree_view, self).__init__()

    def init_left_tree_view(self, mw):
        self.tree = QTreeView(mw)
        self.label = QLabel(mw)
        self.label.setText('目录')
        pe = QPalette()
        pe.setColor(QPalette.WindowText, Qt.white)
        self.tree.setPalette(pe)
        self.label.setPalette(pe)
        self.label.setAlignment(Qt.AlignCenter)
        # self.label.setParent(mw)
        self.label.setGeometry(0, 0, 150, 30)
        self.tree.setGeometry(0, 30, 150, 480)
        self.tree.show()