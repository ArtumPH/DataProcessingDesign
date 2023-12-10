import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QToolBar
from PyQt6.QtGui import QAction

class ToolbarExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Toolbar Example")
        self.setGeometry(100, 100, 600, 400)

        # Create a toolbar
        toolbar = self.addToolBar("Main Toolbar")

        # Add actions to the toolbar
        action_open = QAction("Open", self)
        action_save = QAction("Save", self)
        action_exit = QAction("Exit", self)

        # Connect actions to functions
        action_open.triggered.connect(self.open_file)
        action_save.triggered.connect(self.save_file)
        action_exit.triggered.connect(self.close)

        # Add actions to the toolbar
        toolbar.addAction(action_open)
        toolbar.addAction(action_save)
        toolbar.addSeparator()
        toolbar.addAction(action_exit)

    def open_file(self):
        print("Open file action triggered.")

    def save_file(self):
        print("Save file action triggered.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    toolbar_example = ToolbarExample()
    toolbar_example.show()
    sys.exit(app.exec())
