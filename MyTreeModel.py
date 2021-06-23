from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QMainWindow, QLabel, \
    QPushButton, QHeaderView
from PyQt5.QtGui import QIcon, QPalette, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QAbstractItemModel, pyqtSignal
from FCB import FCB



class MyStandardItem(QStandardItem):
    DoubleClicked = pyqtSignal()
    def __init__(self, fcb: FCB):
        super(MyStandardItem, self).__init__()
        self.fcb = fcb
        self.setText(self.fcb.file_name)
        self.fcb.item = self

        # self.
    def getFCB(self):
        return self.fcb
    def test1(self):
        print(self.parent())


class MyTreeModel(QStandardItemModel):
    def __init__(self):
        super(MyTreeModel, self).__init__()

    def myInvisibleRootItem(self) -> 'QStandardItem':
        root = self.invisibleRootItem()
        root.fcb = FCB('root', 0, path='/')
        return root

    def set_parent_path(self, item: MyStandardItem):
        try:
            item.fcb.path = item.fcb.parent.path + '/' + item.fcb.file_name
        except Exception as arr:
            print(arr)
            item.fcb.path = '/' + item.fcb.file_name


    def set_default_model(self):
        # self.appendRow(MyStandardItem(FCB('root', 0)))
        root = self.myInvisibleRootItem() # type: MyStandardItem
        root.setEditable(False)
        root.fcb.path = '/'
        # print(root)
        # print(root.child(0))
        for i in range(4):

            test_fcb = FCB(str(100+i), i)
            item = MyStandardItem(test_fcb)
            item.setEditable(False)
            item.fcb.parent = root.fcb
            self.set_parent_path(item)
            if i >= 1:
                root.child(i - 1).fcb.sibling = test_fcb
            for j in range(3):
                test_fcb_inner = FCB(str(j), j)
                chidItem = MyStandardItem(test_fcb_inner)
                if j >= 1:
                    item.child(j-1).fcb.sibling = test_fcb_inner
                item.setChild(j, chidItem)
                chidItem.fcb.parent = item.fcb
                # item.appendRow(chidItem)
                chidItem.setEditable(False)
                print(chidItem.parent())
                self.set_parent_path(chidItem)
                # print(chidItem.parent())
            root.setChild(i, item)
            item.fcb.firstChild = item.child(0).fcb

        root.fcb.firstChild = root.child(0).fcb
        # print(item.parent())
        print(root.child(0).parent())
        self.setHeaderData(0, Qt.Orientation.Horizontal, '文件目录')
        # print(root.child(1))
        # print(root.child(0).text())

