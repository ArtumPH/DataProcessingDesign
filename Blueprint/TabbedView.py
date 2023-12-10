from PyQt6.QtGui import QPalette, QColor
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QMenuBar
)




class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs1 = QTabWidget()
        tabs1.setTabPosition(QTabWidget.TabPosition.West)
        tabs1.setMovable(True)

        tabs2 = QTabWidget()
        tabs2.setTabPosition(QTabWidget.TabPosition.North)
        tabs2.setMovable(True)

        tabs2.addTab(Color("black"), "black")

        #tabs = QTabWidget()
        #tabs.setDocumentMode(True)

        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs1.addTab(Color(color), color)

        layout=QHBoxLayout()
        layout.addWidget(tabs1)
        layout.addWidget(tabs2)

        layout.setContentsMargins(0,20,0,0) # left, top, right, bottom
        layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.setMenuBar(QMenuBar())
        

        



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
