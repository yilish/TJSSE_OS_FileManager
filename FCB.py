class FCB:
    def __init__(self, file_name, start_block=-1, type='txt', size='0', path=None, sibling=None,
                 firstChild=None, item=None, time=None, parent=None):
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

