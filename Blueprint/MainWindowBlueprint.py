import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QStatusBar, QTextEdit, QDockWidget, QVBoxLayout, QLabel, QToolBar, QTreeView, QTabWidget
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QFileSystemModel, QAction

class VSCodeStyleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("VSCode Style Window")
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vs_code_style_window = VSCodeStyleWindow()
    vs_code_style_window.show()
    sys.exit(app.exec())
