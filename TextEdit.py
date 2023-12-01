# TextEdit.py
from PyQt6.QtWidgets import QTextEdit

class ExcelTextEdit(QTextEdit):
    def __init__(self):
        super().__init__()

    def display_selected_data(self, selected_data_str):
        self.setPlainText(selected_data_str)
