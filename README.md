# 文件管理大作业 - 文件系统模拟

> Course: 2021 操作系统 同济大学软件学院
>
> Project: 文件系统模拟
>
> Name: 
>
> Student Number: 1851009

## 1. 项目需求

​	在内存中开辟一个空间作为文件存储器，在其上实现一个简单的文件系统。

​	退出这个文件系统时，需要该文件系统的内容保存到磁盘上，以便下次可以将其恢复到内存中来。

## 1.1 功能描述

### 功能描述

- 文件存储空间管理可采取显式链接（如FAT）或者其他方法。（即自选一种方法）

- 空闲空间管理可采用位图或者其他方法。如果采用了位图，可将位图和FAT表合二为一。

- 文件目录采用多级目录结构。至于是否采用索引节点结构，自选。目录项目中应包含：文件名、物理地址、长度等信息。同学可在这里增加一些其他信息。

- 文件系统提供的操作：

  - 格式化

  - 创建子目录

  - 删除子目录

  - 显示目录

  - 更改当前目录

  - 创建文件

  - 打开文件

  - 关闭文件

  - 写文件

  - 读文件

  - 删除文件

### 1.1 项目目的

- 熟悉文件存储空间的管理；
- 熟悉文件的物理结构、目录结构和文件操作；
- 熟悉文件系统管理实现；
- 加深对文件系统内部功能和实现过程的理解



### 1.2 开发环境

- 开发系统：MacOS 10.15.3

- 开发软件:

  - PyCharm
  - Qt Designer(GUI设计)
  
- 开发语言

  - Python3.9
  - PyQt5.12
  - QSS
  - QML

  


## 2. 操作说明

1. 如果您拥有PyQt5以及相关依赖，可以直接在命令行输入`python3 ./main.py`即可进入该系统。若无，可以双击`FileManager.exe`可执行文件进入系统。(由于PyQt5跨平台的引擎使用有微小差异，建议在MacOS深色模式运行）![截屏2021-06-24下午1.10.22](/Users/bigpear/Library/Application Support/typora-user-images/截屏2021-06-24下午1.10.22.png)

2. （可选）修改磁盘容量和块大小进行模拟，若报错则说明有磁盘块越界，需要重新格式化磁盘。

   ![image-20210624131308451](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624131308451.png)

3. 单击新建文件夹按钮进行新建文件夹操作。

   ![image-20210624131440912](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624131440912.png)

   左侧文件树将随之更新。

   ![image-20210624131505795](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624131505795.png)

   

4. 单击新建文件即可新建一个txt文件。

   

   ![截屏2021-06-24下午1.17.06](/Users/bigpear/Library/Application Support/typora-user-images/截屏2021-06-24下午1.17.06.png)

左侧文件树也会随之更新

![image-20210624131735776](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624131735776.png)

5. 可以双击该文件来进行编辑。

![截屏2021-06-24下午1.18.17](/Users/bigpear/Library/Application Support/typora-user-images/截屏2021-06-24下午1.18.17.png)

6. 可以双击文件夹来进入文件夹，此时路径也会随之变化。

![截屏2021-06-24下午1.19.32](/Users/bigpear/Library/Application Support/typora-user-images/截屏2021-06-24下午1.19.32.png)

7. 单击返回上级，即可返回到上级目录。

![image-20210624132008920](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132008920.png)

8. 点击修改文件名，即可修改。

   ![截屏2021-06-24下午1.20.30](/Users/bigpear/Library/Application Support/typora-user-images/截屏2021-06-24下午1.20.30.png)

   ![image-20210624132108567](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132108567.png)

9. 可以点击“删除文件”进行文件删除操作。

   ![image-20210624132151070](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132151070.png)

   ![image-20210624132342584](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132342584.png)

10. 可以搜索文件。（要求搜索到到文件名等于字符串）

![image-20210624132456725](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132456725.png)

![image-20210624132614854](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132614854.png)

11. 退出重进后，仍能保留文件目录结构。

![image-20210624132658988](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624132658988.png)

## 3. 系统分析

### 3.1 显式链接法

使用显式链接法，先找到第一块未分配内容的块，然后按顺序向后查找空块，按照文件大小寻找若干个空闲块，将内容放入这些空块中并连接起来。分配的第一块地址加入FCB中。删除时将原来占据的块内容置空。

### 3.2 位图

使用了改进后的位图，将空闲区标记为`-1`，将结尾的块区标记为`-2`，其余的被占据的片区标记为下一块盘块的位置。

## 4. 系统设计

#### 4.1 视图设计

##### 4.1.1 整体设计

- ```
  Ui_MainWindow
  ```

![image-20210624133725691](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624133725691.png)

##### 4.1.2 首页弹出信息框

```html
Ui_Dialog
```

![image-20210624134120420](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624134120420.png)

##### 4.1.3 新建文件框

`Ui_Create_dlg`

![image-20210624134139404](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624134139404.png)

##### 4.1.4 改名框

```html
Ui_change_name_dlg
```

![image-20210624134212392](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624134212392.png)

##### 4.1.5 文件详情框

```html
Ui_file_dialog
```

![image-20210624134248215](/Users/bigpear/Library/Application Support/typora-user-images/image-20210624134248215.png)



##### 



#### 4.2 实体设计

##### 4.2.1 FCB类设计

```python
class FCB:
    def __init__(self, file_name, start_block=-1, type='txt', size='0', path=None, sibling=None,
                 firstChild=None, item=None, time=None, parent=None, code=None):
        self.file_name = file_name
        self.start_block = start_block
        self.type = type
        self.size = size
        self.sibling = sibling
        self.firstChild = firstChild
        self.item = item
        self.time = time
        self.path = path
        self.parent = parent
        # self.code = code
```

#### 4.2.2 StandardItem设计

```python
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
```

#### 4.2.3 TreeItem设计

```python
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
```

## 5. 系统实现

#### 5.1 添加文件

添加文件要先找到当前节点信息，然后在它的子节点上添加一个元素。并且为其开辟一块空间。

```python
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
```





#### 5.2  删除文件

删除文件首先要找到该节点的父节点，然后将其父节点的子节点减少一个。并且释放其内存上的空间。

```python
def delete_file(self):
    if self.mw.tableWidget.selectedIndexes():
        row_num = self.mw.tableWidget.selectedIndexes()[0].row()
        target_fcb = self.get_fcb_by_row(row_num)
        cur_block = target_fcb.start_block
        while cur_block >= 0:
            next_block = self.bitmap[cur_block]
            self.bitmap[cur_block] = -1
            self.mem_storage[cur_block] = ""
            cur_block = next_block
        self.del_fcb_by_name(target_fcb.file_name)
        self.set_widget_table(self.cur_item)
        self.cur_item.removeRow(row_num)
    else:
        print('No selected data.')
```

#### 5.3 修改文件名

修改FCB中的文件名并重新渲染即可。

```python
def change_name(self):
    new_name = self.change_dlg.lineEdit.text()
    if self.mw.tableWidget.selectedIndexes():
        row_num = self.mw.tableWidget.selectedIndexes()[0].row()
        target_fcb = self.get_fcb_by_row(row_num)
        target_fcb.file_name = new_name
        target_fcb.item.setText(new_name)
        # self.del_fcb_by_name(target_fcb.file_name)
        self.set_widget_table(self.cur_item)
        
```

#### 5.4 修改文件内容

为其分配内存，并且存入内容即可。

```python
def file_closed(self):
    self.cur_text = self.file_dlg.plainTextEdit.toPlainText()
    self.file_dlg.plainTextEdit.setPlainText('')
    # 分块处理
    first_free_block = -1
    file_len = len(self.cur_text)
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
    former_block = first_free_block
    filled_blocks = 0
    for i in range(first_free_block, len(self.bitmap)):
        if filled_blocks == block_num:
            self.bitmap[former_block] = -2 # 宣布封顶
            break
        if self.bitmap[i] == -1:
            self.bitmap[former_block] = i
            former_block = i
            self.mem_storage[i] = self.cur_text[2 * filled_blocks: 2*filled_blocks + 2]
            filled_blocks += 1
    self.clicked_item.fcb.size = str(block_num)
    self.set_widget_table(self.cur_item)
```

#### 5.5 查找文件内容

用DFS搜索文件，直到文件名匹配为止。

```python
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
```

#### 5.6 保存文件内容

按格式分别将位图、内存中的内容、FCB表写入本地文件。

```python
def mw_closed(self):
    with open('bitmap.txt', 'w') as f:
        for item in self.bitmap:
            f.write(str(item) + '\n')
        f.close()
    with open('content.txt', 'w') as f:
        for item in self.content_map:
            f.write(str(item) + ' ')
        f.close()
    with open('fcb.txt', 'w') as f:
        self.root_item.fcb.parentIdx = -1
        fcb_list = [self.root_item.fcb]

        i = 0
        print(self.root_item.fcb)
        self.root_item.fcb.time = time.asctime( time.localtime(time.time()) )
        while i < len(fcb_list):
            tmp_child = fcb_list[i].firstChild
            while tmp_child:
                fcb_list.append(tmp_child)
                tmp_child.parentIdx = i
                tmp_child = tmp_child.sibling
            i += 1
        for item in fcb_list:
            f.write(item.file_name + '\\' +
                    str(item.start_block) + '\\' +
                    item.type + '\\' +
                    item.size + '\\' +
                    item.path + '\\' +
                    str(item.parentIdx) + '\\' +
                    item.time + '\n')
```

#### 5.6 读取文件内容

按格式读入内存并且组织FCB树即可。

```python
def read_from_local_files(self):
    with open('bitmap.txt', 'r') as f:
        s = f.read()
        L = s.split('\n')
        self.bitmap = [-1] * (len(L) - 1)
        for i in range(len(L) - 1):
            self.bitmap[i] = int(L[i])
        f.close()
    with open('content.txt', 'r') as f:
        s = f.read()
        L = s.split('\n')
        self.mem_storage = [""] * (len(L) - 1)
        for i in range(len(L) - 1):
            self.mem_storage[i] = L[i]
        f.close()
    with open('fcb.txt', 'r') as f:
        s = f.read()
        L = s.split('\n')
        root_fcb = FCB('root', -1, 'folder', '0', '/')
        root_fcb.item = self.root_item
        self.root_item.fcb = root_fcb
        fcb_list = [root_fcb]

        for i in range(1, len(L) - 1):
            sub_L = L[i].split('\\')
            tmp_fcb = FCB(sub_L[0], int(sub_L[1]), sub_L[2], sub_L[3], sub_L[4])
            tmp_fcb.parent = fcb_list[int(sub_L[5])]
            tmp_fcb.time = sub_L[6]
            if tmp_fcb.parent.firstChild:
                f_child, pos = self.get_last_sibling(tmp_fcb.parent.firstChild)
                f_child.sibling = tmp_fcb
            else:
                tmp_fcb.parent.firstChild = tmp_fcb
            tmp_item = MyStandardItem(tmp_fcb)
            tmp_item.setEditable(False)
            parent_item = tmp_fcb.parent.item # type: MyStandardItem
            fcb_list.append(tmp_fcb)
            parent_item.setChild(parent_item.rowCount(), tmp_item)
        f.close()
        self.set_widget_table(root_fcb.item)
```

