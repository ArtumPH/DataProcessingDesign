import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDockWidget, QTextEdit, QLabel
from PyQt6.QtCore import Qt

class DockWidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Dock Widget Example")
        self.setGeometry(100, 100, 800, 600)

        # Create a QTextEdit widget (or any other widget you want in the dock)
        text_edit = QTextEdit()
        text_edit.setPlainText("This is the dock widget content.")

        # Create a QDockWidget
        dock_widget = QDockWidget("Dock Widget", self)
        dock_widget.setWidget(text_edit)

        # Set dock options
        dock_widget.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)

        # Add the dock widget to the main window
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock_widget)

        # Add a label to the main window (outside the dock widget)
        label = QLabel("This is the main window content.")
        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dock_widget_example = DockWidgetExample()
    dock_widget_example.show()
    sys.exit(app.exec())
