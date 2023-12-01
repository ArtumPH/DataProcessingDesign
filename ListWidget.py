# ListWidget.py
from PyQt6.QtWidgets import QListWidget

class ExcelListWidget(QListWidget):
    def __init__(self):
        super().__init__()

    def update_combobox(self, update_func):
        self.itemClicked.connect(update_func)
