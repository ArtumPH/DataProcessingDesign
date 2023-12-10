import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu
from PyQt6.QtGui import QAction

class MenuBarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Menu Bar Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a menu bar
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        # Actions for the File menu
        action_new = QAction("New", self)
        action_open = QAction("Open", self)
        action_save = QAction("Save", self)
        action_exit = QAction("Exit", self)

        # Connect actions to functions
        action_new.triggered.connect(self.new_file)
        action_open.triggered.connect(self.open_file)
        action_save.triggered.connect(self.save_file)
        action_exit.triggered.connect(self.close)

        # Add actions to the File menu
        file_menu.addAction(action_new)
        file_menu.addAction(action_open)
        file_menu.addAction(action_save)
        file_menu.addSeparator()
        file_menu.addAction(action_exit)

        # Edit menu
        edit_menu = menubar.addMenu("Edit")

        # Actions for the Edit menu
        action_cut = QAction("Cut", self)
        action_copy = QAction("Copy", self)
        action_paste = QAction("Paste", self)

        # Connect actions to functions
        action_cut.triggered.connect(self.cut_text)
        action_copy.triggered.connect(self.copy_text)
        action_paste.triggered.connect(self.paste_text)

        # Add actions to the Edit menu
        edit_menu.addAction(action_cut)
        edit_menu.addAction(action_copy)
        edit_menu.addAction(action_paste)

    def new_file(self):
        print("New file action triggered.")

    def open_file(self):
        print("Open file action triggered.")

    def save_file(self):
        print("Save file action triggered.")

    def cut_text(self):
        print("Cut text action triggered.")

    def copy_text(self):
        print("Copy text action triggered.")

    def paste_text(self):
        print("Paste text action triggered.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    menu_bar_example = MenuBarExample()
    menu_bar_example.show()
    sys.exit(app.exec())
