from PyQt5.QtGui import QStandardItem

class LibStandardItem(QStandardItem):
    """item base class for library"""
    def __init__(self, str):
        super().__init__(str)
        self.tagsList = []


