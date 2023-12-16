# MainWindow.py
import sys
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, 
                             QVBoxLayout, QHBoxLayout, QMenu,
                             QMenuBar, QStatusBar, QDockWidget,
                             QTreeView, QTabWidget, QLabel,
                             QTextEdit, QFileDialog, )
from TableWidget import ExcelTableWidget
from Buttons import Button_With_Image
from ComboBoxes import ExcelComboBoxes
from TextEdit import ExcelTextEdit
from ListWidget import ExcelListWidget
#from Menubar_functions import Menu_Open

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Data Analysis")
        self.setGeometry(200, 150, 1500, 800)

        self.table_widget = ExcelTableWidget()
        self.tab_widget = self.create_tab_widget()
        self.selected_data_display_text = ExcelTextEdit()

        # Diagram Choose Buttons
        self.Plot_X_Y_Button = Button_With_Image(self,"GrassTexture.jpg") # Replace with the actual path to image

        # Central tab widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)
        '''
        self.excel_load_button = Excel_Load_Button(self.table_widget)
        self.layout.addWidget(self.excel_load_button.load_button)
        
        self.excel_read_button = Excel_read_seleced_data_Button(self.table_widget,self.selected_data_display_text)
        self.layout.addWidget(self.excel_read_button.read_button)
        
        self.text_edit = ExcelTextEdit()
        self.layout.addWidget(self.text_edit)
        
        self.comboboxes = ExcelComboBoxes()
        self.layout.addWidget(self.comboboxes.x_axis_combobox)
        self.layout.addWidget(self.comboboxes.y_axis_combobox)
        
        self.list_widget = ExcelListWidget()
        self.layout.addWidget(self.list_widget)
        '''

        #----------------------------------------------------------------------------

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Actions
        new_action = QAction("New Tab", self)
        new_action.triggered.connect(self.create_new_tab)
        file_menu.addAction(new_action)

        open_action = QAction("Open File...", self)
        open_action.triggered.connect(lambda: self.load_excel(self.table_widget))
        file_menu.addAction(open_action)

        read_action = QAction("Read Selected Data", self)
        read_action.triggered.connect(lambda: self.read_selected_data(self.table_widget,self.selected_data_display_text))
        file_menu.addAction(read_action)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)

        edit_menu = menubar.addMenu("Edit")
        view_menu = menubar.addMenu("View")

        # Toolbar
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(read_action)
        toolbar.addAction(save_action)

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
        
        # Docked widget for Plot types Area
        plot_types_dock = QDockWidget("Plot types", self)
        plot_types_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        plot_types_dock.setWidget(self.Plot_X_Y_Button)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, plot_types_dock)

        # Docked widget for loaded data table Area
        data_load_dock = QDockWidget("Loaded data", self)
        data_load_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        data_load_dock.setWidget(self.selected_data_display_text)
        data_load_dock.setMinimumSize(500,500)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, data_load_dock)

        # Docked widget for After use
        after_use_dock = QDockWidget("After use", self)
        after_use_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        #after_use_dock.setWidget(self.)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, after_use_dock)

        # Combine docked widgets
        self.tabifyDockWidget(data_load_dock, plot_types_dock)

        # Raise docked widgets(Needs after combine docked widgets to work)
        data_load_dock.raise_()

        # Add context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    # Add load_excel method
    def load_excel(self, table_widget):
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            table_widget.load_data_from_excel(file_name)

    #Add read_selected_data method
    def read_selected_data(self, table_widget, text_edit):
        selected_data_matrix, selected_data_columns = table_widget.get_selected_data()

        if selected_data_matrix is not None:
            dispaly_text=table_widget.display_selected_data(selected_data_matrix, selected_data_columns)
            text_edit.display_selected_data(dispaly_text)
            

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
        tab_widget.setMovable(True)
        tab_widget.tabCloseRequested.connect(self.close_tab)

        # Create initial tab
        tab_widget.addTab(self.table_widget, "Untitled")

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
