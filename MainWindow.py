# MainWindow.py
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMenu
from TableWidget import ExcelTableWidget
from Buttons import Excel_Load_Button, Excel_read_seleced_data_Button
from ComboBoxes import ExcelComboBoxes
from TextEdit import ExcelTextEdit
from ListWidget import ExcelListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Add context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.table_widget = ExcelTableWidget()
        self.layout.addWidget(self.table_widget)

        self.excel_load_button = Excel_Load_Button(self.table_widget)
        self.layout.addWidget(self.excel_load_button.load_button)

        self.excel_read_button = Excel_read_seleced_data_Button(self.table_widget)
        self.layout.addWidget(self.excel_read_button.read_button)

        self.text_edit = ExcelTextEdit()
        self.layout.addWidget(self.text_edit)

        self.comboboxes = ExcelComboBoxes()
        self.layout.addWidget(self.comboboxes.x_axis_combobox)
        self.layout.addWidget(self.comboboxes.y_axis_combobox)

        self.list_widget = ExcelListWidget()
        self.layout.addWidget(self.list_widget)

        self.setWindowTitle('Excel Viewer')
        self.setGeometry(100, 100, 1000, 600)

    # Add on_context_menu method
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
