# -*- coding: utf-8 -*-
# @Time    : 2021/06/22
# @Author  : Yili Shen
# @Email   : 1851009@tongji.edu.cn
# @File    : main.py
# @Software: PyCharm Python3.9 MacOS 10.15.3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
from PyQt5.QtGui import QIcon
import mainwindowui
from mw import Ui_MainWindow
from popup import Ui_Dialog
import controller
from createFile import Ui_Create_dlg
from createFolder import Ui_Create_folder
from change_name_dialog import Ui_change_name_dlg
from file_detail import Ui_file_dialog
class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)
class MyCreateDialog(QDialog, Ui_Create_dlg):
    def __init__(self, parent=None):
        super(MyCreateDialog, self).__init__(parent)
        self.setupUi(self)
class MyChangeDlg(QDialog, Ui_change_name_dlg):
    def __init__(self, parent=None):
        super(MyChangeDlg, self).__init__(parent)
        self.setupUi(self)
class MyCreateFolderDialog(QDialog, Ui_Create_folder):
    def __init__(self, parent=None):
        super(MyCreateFolderDialog, self).__init__(parent)
        self.setupUi(self)

class MyFileDialog(QDialog, Ui_file_dialog):
    def __init__(self, parent=None):
        super(MyFileDialog, self).__init__(parent)
        self.setupUi(self)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyMainForm()

    dialog = MyDialog()
    createDlg = MyCreateDialog()
    folderDlg = MyCreateFolderDialog()
    changeDlg = MyChangeDlg()
    fileDlg = MyFileDialog()
    controller.controller(mw=MainWindow,
                          dialog=dialog,
                          create_dialog=createDlg,
                          create_folder=folderDlg,
                          change_dlg=changeDlg,
                          file_dlg=fileDlg)

    MainWindow.show()
    dialog.show()
    sys.exit(app.exec_())