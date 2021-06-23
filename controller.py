import math
import sys
# from PyQt5 import Qt
from functools import partial

from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout, QMainWindow, QLabel, \
    QPushButton, QHeaderView, QTableWidgetItem, QAbstractItemView, QFrame, QMessageBox
from PyQt5.QtGui import QIcon, QPalette, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QModelIndex
# import MyTreeModel
from MyTreeModel import MyTreeModel
import mw
from main import MyMainForm
from main import MyDialog
from main import MyCreateDialog
from main import MyCreateFolderDialog, MyChangeDlg, MyFileDialog
from MyTreeModel import MyStandardItem, MyTreeModel
from FCB import FCB
import time


header_field = ['文件名', '修改日期', '类型', '大小']

class controller():
    def update_sizes(self, dialog: MyDialog):
        self.capacity = int(dialog.txt_diskCapacity.text())
        self.blockSize = int(dialog.txt_blockSize.text())
        self.block_num = int(int(self.capacity) / int(self.blockSize))
        # 更新盘块/磁盘大小
        self.mw.lbl_blockSize.setText('当前盘块大小: ' + str(self.blockSize))
        self.mw.lbl_diskSize.setText('当前磁盘大小: ' + str(self.capacity))
        self.bitmap = self.block_num * [-1]
        self.mem_storage = self.block_num * [""]
        # todo: 绑定盘块、磁盘大小

    def __init__(self, mw: MyMainForm, dialog: MyDialog,
                 create_dialog: MyCreateDialog,
                 create_folder: MyCreateFolderDialog,
                 change_dlg: MyChangeDlg,
                 file_dlg: MyFileDialog):
        self.capacity = 1000
        self.blockSize = 2
        self.block_num = 500
        self.bitmap = []
        self.mem_storage = []
        self.content_map = []
        self.mw = mw
        self.file_dlg = file_dlg
        self.dialog = dialog
        self.change_dlg = change_dlg
        self.dialog.buttonBox.accepted.connect(partial(self.update_sizes, dialog))
        self.mid_table_init()
        self.left_treeview_init()
        self.table_widget_init()
        self.mw.btn_formatting.clicked.connect(self.formatting)
        self.mw.textBrowser.setText('/')
        self.create_dialog = create_dialog
        self.create_dialog.accepted.connect(self.create_new_file)
        self.create_folder_dlg = create_folder
        self.create_folder_dlg.accepted.connect(self.create_new_folder)
        self.change_dlg.accepted.connect(self.change_name)
        self.cur_item = self.root_item
        # self.mw.treeView.model().setHeaderData(0, Qt.Orientation.Horizontal, '文件目录')
        self.cur_item.fcb.item = self.root_item
        self.mw.search_text.returnPressed.connect(self.search)
        self.file_dlg.closed.connect(self.file_closed)

    def file_closed(self):
        self.cur_text = self.file_dlg.plainTextEdit.toPlainText()
        self.file_dlg.plainTextEdit.setPlainText('')
        # 分块处理
        first_free_block = -1
        file_len = len(self.cur_text) / 2
        block_num = math.ceil(file_len / 2)
        free_num = len([i for i in self.bitmap if i == -1])
        if block_num > free_num:
            QMessageBox.warning(self.mw, "No more space", "空闲空间不足", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            return
        for i in range(len(self.bitmap)):
            if self.bitmap[i] == -1:
                first_free_block = i
                break
        self.clicked_item.fcb.start_block = first_free_block
        # 按顺序往里填就完事了


    def search(self):
        target_name = self.mw.search_text.text()
        target_fcb = self.search_fcb_by_name(target_name, self.root_item) # type: FCB
        # QTreeView.select
        if not target_fcb:
            QMessageBox.warning(self.mw, "Not Found", "没有找到所需的文件", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            return
        self.cur_item = target_fcb.parent.item
        row_num = self.get_row_by_name(target_name)
        if row_num == -1:
            QMessageBox.warning(self.mw, "Not Found", "没有找到所需的文件", QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.Yes)
            return
        self.set_widget_table(self.cur_item)
        self.mw.tableWidget.selectRow(row_num)
        # target_fcb.item



    def table_widget_init(self):
        self.model = self.mw.treeView.model() # type: MyTreeModel

        self.root_item = self.model.myInvisibleRootItem()
        try:
            self.root_item.fcb.firstChild = self.root_item.child(0).fcb
        except:
            pass
        print(self.root_item)
        self.set_widget_table(self.root_item)



    def mid_table_init(self):
        self.mw.tableWidget.horizontalHeader().setVisible(True)
        self.mw.tableWidget.setColumnCount(4)
        self.mw.tableWidget.setHorizontalHeaderLabels(header_field)
        self.mw.tableWidget.horizontalHeader().setStretchLastSection(True)
        # # font = self.mw.tableWidget.horizontalHeader().font().
        # pe = QPalette()
        # pe.setColor(QPalette.WindowText, Qt.black)
        # self.mw.tableWidget.horizontalHeader().setPalette(pe)
        self.mw.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{font:12pt ;color: white;};")
        self.mw.btn_newFile.clicked.connect(self.get_create_dialog)
        self.mw.btn_newFolder.clicked.connect(self.get_folder_dialog)
        self.mw.btn_back.clicked.connect(self.rollback)
        self.mw.btn_delFile.clicked.connect(self.delete_file)
        self.mw.btn_changeName.clicked.connect(self.show_change_dlg)
        # self.mw.tableWidget.horizontalHeader().font().setStyle(QFont.Bold)
        # self.mw.label_2.setText('123')
    def left_treeview_init(self):
        self.model = MyTreeModel()
        # self.model.set_default_model()
        # print(model)
        header = QHeaderView(Qt.Orientation.Horizontal)
        # header.seth
        # header.setObjectName('123')
        self.mw.treeView.setModel(self.model)
        self.mw.treeView.header().setVisible(True)
        self.mw.treeView.doubleClicked.connect(self.updatetable)
        self.mw.tableWidget.doubleClicked.connect(self.open_file)
        self.mw.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.mw.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行
        self.mw.tableWidget.setShowGrid(False)

    def open_file(self, index):
        self.clicked_item = self.mw.tableWidget.itemFromIndex(index) # type: MyStandardItem

        if self.clicked_item.fcb.type == 'Folder':
            self.cur_item = self.clicked_item
            self.set_widget_table(self.cur_item)
            return
        else:
            self.file_dlg.show()
            self.file_dlg.setWindowTitle(self.clicked_item.fcb.file_name)
            # self.file_dlg.closed.connect()
        # Todo: 加入读取盘块



    def updatetable(self, index: QModelIndex):
        self.cur_item = self.model.itemFromIndex(index) # type: MyStandardItem
        self.set_widget_table(self.cur_item)


    def set_widget_table(self, parent_item):
        self.mw.textBrowser.setText(parent_item.fcb.path)
        # print(parent_item.fcb.path)
        tmp_child = parent_item.fcb.firstChild # type: FCB
        item_list = []
        while tmp_child:
            item_list.append(tmp_child.item)
            tmp_child = tmp_child.sibling
        self.mw.tableWidget.setRowCount(len(item_list))
        # self.table_model = self.mw.tableWidget.model()
        for i in range(len(item_list)):
            cur_item = item_list[i]# type: MyStandardItem
            file_name = QTableWidgetItem(cur_item.fcb.file_name)
            # print(item_list[i].fcb.file_name)
            self.mw.tableWidget.setItem(i, 0, file_name)
            # time = item_list[i].fcb.time # type: # time
            # time_str = '{}年{}'.format(item_list[i].fcb.time.tm_year)
            file_name.fcb = cur_item.fcb
            time = QTableWidgetItem(item_list[i].fcb.time)
            self.mw.tableWidget.setItem(i, 1, time)
            time.fcb = cur_item.fcb
            type = QTableWidgetItem(item_list[i].fcb.type)
            self.mw.tableWidget.setItem(i, 2, type)
            type.fcb = cur_item.fcb
            size = QTableWidgetItem(str(item_list[i].fcb.size))
            size.fcb = cur_item.fcb
            print(item_list[i].fcb.size)
            self.mw.tableWidget.setItem(i, 3, size)
        # self.mw.tableWidget.setModel(self.model)
        # self.mw.tableWidget.model()

    def formatting(self):
        self.mw.treeView.setModel(MyTreeModel())
        # self.mw.treesetHeaderData(0, Qt.Orientation.Horizontal, '文件目录')
        self.mw.tableWidget.setRowCount(0)


    def get_create_dialog(self):
        self.create_dialog.show()
    def get_folder_dialog(self):
        self.create_folder_dlg.show()


    def get_last_sibling(self, fcb: FCB):
        i = 0
        while fcb.sibling:
            # item_list.append(tmp_child.item)
            fcb = fcb.sibling
            i += 1
        return fcb, i

    def get_all_fcb_under_this_folder(self, parent_fcb: FCB):
        L = []
        if parent_fcb.firstChild:

            tmp_fcb = parent_fcb.firstChild
            while tmp_fcb:
                # item_list.append(tmp_child.item)
                L.append(tmp_fcb)
                tmp_fcb = tmp_fcb.sibling

        return L

    def create_new_file(self): # 增
        file_name = self.create_dialog.lineEdit.text()
        L = self.get_all_fcb_under_this_folder(self.cur_item.fcb)
        print(L)
        L_name = []
        for fcb in L:
            L_name.append(fcb.file_name)
        print(L_name)
        if file_name in L_name:
            QMessageBox.warning(self.mw, "Duplicate", "请确保目录下唯一的文件名！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return False
        tmp_fcb = FCB(file_name, type='txt',time=time.asctime( time.localtime(time.time()) ),
                      path=self.cur_item.fcb.path+'/'+file_name,
                      parent=self.cur_item.fcb,
                      size='0'
                      )
        item = MyStandardItem(tmp_fcb)
        item.setEditable(False)
        tmp_fcb.item = item
        if self.cur_item.fcb.firstChild:
            last_child, num = self.get_last_sibling(self.cur_item.fcb.firstChild)
            last_child.sibling = tmp_fcb
            self.cur_item.setChild(num+1, item)
        else:
            self.cur_item.fcb.firstChild = tmp_fcb
            self.cur_item.setChild(0, item)
        self.set_widget_table(self.cur_item)
        self.create_dialog.lineEdit.setText("")
        return True


    def create_new_folder(self): # 增
        file_name = self.create_folder_dlg.lineEdit.text()
        L = self.get_all_fcb_under_this_folder(self.cur_item.fcb)
        print(L)
        L_name = []
        for fcb in L:
            L_name.append(fcb.file_name)
        print(L_name)
        if file_name in L_name:
            QMessageBox.warning(self.mw, "Duplicate", "请确保目录下唯一的文件名！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return False
        tmp_fcb = FCB(file_name, type='Folder',
                      time=time.asctime(time.localtime(time.time())),
                      path=self.cur_item.fcb.path+'/'+file_name,
                      parent=self.cur_item.fcb,
                      size='/'
                      )
        item = MyStandardItem(tmp_fcb)
        item.setEditable(False)
        tmp_fcb.item = item
        # self.get_last_sibling()
        if self.cur_item.fcb.firstChild:
            last_child, num = self.get_last_sibling(self.cur_item.fcb.firstChild)
            last_child.sibling = tmp_fcb
            self.cur_item.setChild(num+ 1, item)
        else:
            self.cur_item.fcb.firstChild = tmp_fcb
            self.cur_item.setChild(0, item)
        self.set_widget_table(self.cur_item)
        self.create_folder_dlg.lineEdit.setText("")

    def rollback(self):
        try:
            self.cur_item = self.cur_item.fcb.parent.item
            self.set_widget_table(self.cur_item)
        except Exception as er:
            print(er)
            pass

    def get_fcb_by_name(self, name):
        if self.cur_item.fcb.firstChild:
            tmp_child = self.cur_item.fcb.firstChild
            while tmp_child:
                if tmp_child.fcb.file_name == name:
                    return tmp_child
        return None

    def get_row_by_name(self, name):
        i = 0
        if self.cur_item.fcb.firstChild:
            tmp_child = self.cur_item.fcb.firstChild
            while tmp_child:
                if tmp_child.file_name == name:
                    return i
                i += 1
        return -1


    def get_former_fcb_by_name(self, name):
        if self.cur_item.fcb.firstChild:
            tmp_child = self.cur_item.fcb.firstChild
            while tmp_child.sibling:
                if tmp_child.sibling.fcb.file_name == name:
                    return tmp_child
        return None


    def get_fcb_by_row(self, row):
        i = 0
        if self.cur_item.fcb.firstChild:
            tmp_fcb = self.cur_item.fcb.firstChild # type: FCB
            while i < row:
                if not tmp_fcb:
                    return None
                tmp_fcb = tmp_fcb.sibling
                i += 1
            return tmp_fcb
        return None

    # def del_file_by_fcb(self, target_fcb):
    def del_fcb_by_name(self, name):
        if self.cur_item.fcb.firstChild.file_name == name:
            self.cur_item.fcb.firstChild = self.cur_item.fcb.firstChild.sibling
            return
        former_fcb = self.get_former_fcb_by_name(name)
        former_fcb.sibling = former_fcb.sibling.sibling


    def delete_file(self):
        if self.mw.tableWidget.selectedIndexes():
            row_num = self.mw.tableWidget.selectedIndexes()[0].row()
            target_fcb = self.get_fcb_by_row(row_num)
            self.del_fcb_by_name(target_fcb.file_name)
            self.set_widget_table(self.cur_item)
            self.cur_item.removeRow(row_num)
        else:
            print('No selected data.')

    def show_change_dlg(self):
        self.change_dlg.show()
        pass

    def search_fcb_by_name(self, file_name, root: MyStandardItem):
        L = self.get_all_fcb_under_this_folder(root.fcb)
        for item in L:
            if item.file_name == file_name:
                return item
        for fcb in L:
            tmp_res = self.search_fcb_by_name(file_name, fcb.item)
            if tmp_res:
                return tmp_res
        return None

    def change_name(self):
        new_name = self.change_dlg.lineEdit.text()
        if self.mw.tableWidget.selectedIndexes():
            row_num = self.mw.tableWidget.selectedIndexes()[0].row()
            target_fcb = self.get_fcb_by_row(row_num)
            target_fcb.file_name = new_name
            target_fcb.item.setText(new_name)
            # self.del_fcb_by_name(target_fcb.file_name)
            self.set_widget_table(self.cur_item)
            # self.cur_item.removeRow(row_num)