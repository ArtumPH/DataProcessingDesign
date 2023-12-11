# MainWindow.py
import sys
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, 
                             QVBoxLayout, QHBoxLayout, QMenu,
                             QMenuBar, QStatusBar, QDockWidget,
                             QTreeView, QTabWidget, QLabel,
                             QTextEdit, )
from TableWidget import ExcelTableWidget
from Buttons import Excel_Load_Button, Excel_read_seleced_data_Button
from ComboBoxes import ExcelComboBoxes
from TextEdit import ExcelTextEdit
from ListWidget import ExcelListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Data Analysis")
        self.setGeometry(100, 100, 1200, 800)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Actions
        new_action = QAction("New", self)
        new_action.triggered.connect(self.create_new_tab)
        file_menu.addAction(new_action)

        open_action = QAction("Open", self)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)

        edit_menu = menubar.addMenu("Edit")
        view_menu = menubar.addMenu("View")

        # Toolbar
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(save_action)

        # Central tab widget
        self.tab_widget = self.create_tab_widget()
        self.setCentralWidget(self.tab_widget)

        # Status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_label = QLabel("Ready")
        status_bar.addWidget(status_label)

        # Docked widget for file explorer
        explorer_dock = QDockWidget("Explorer", self)
        explorer_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        explorer_tree = self.create_file_explorer()
        explorer_dock.setWidget(explorer_tree)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, explorer_dock)

#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

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
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
    
    # Add on_context_menu method
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def create_tab_widget(self):
        tab_widget = QTabWidget(self)
        tab_widget.setTabsClosable(True)
        tab_widget.tabCloseRequested.connect(self.close_tab)

        # Create initial tab
        text_editor = QTextEdit(tab_widget)
        tab_widget.addTab(text_editor, "Untitled")

        return tab_widget

    def create_new_tab(self):
        text_editor = QTextEdit(self.tab_widget)
        self.tab_widget.addTab(text_editor, "Untitled")

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_file_explorer(self):
        explorer_tree = QTreeView()
        model = QFileSystemModel()
        
        # Set the root path to the current directory
        model.setRootPath(QDir.currentPath())

        explorer_tree.setModel(model)
        explorer_tree.setRootIndex(model.index(QDir.currentPath()))
        explorer_tree.setColumnWidth(0, 200)
        explorer_tree.setHeaderHidden(True)
        explorer_tree.clicked.connect(self.file_explorer_clicked)

        return explorer_tree

    def file_explorer_clicked(self, index):
        model = self.sender().model()
        file_path = model.filePath(index)
        status_label = self.statusBar().findChild(QLabel)
        status_label.setText(f"Selected: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
