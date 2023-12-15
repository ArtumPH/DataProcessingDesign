# Menubar_functions.py
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QAction

class Menu_Open:
    #def __init__(self, table_widget):
        #lambda: self.load_excel(table_widget)

    def load_excel(self, table_widget):
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            table_widget.load_data_from_excel(file_name)
