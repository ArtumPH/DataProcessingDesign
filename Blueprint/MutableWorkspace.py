import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QPoint

class DraggableTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setMovable(True)
        self.setTabsClosable(True)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            distance = (event.pos() - self.drag_start_position).manhattanLength()
            if distance > 5:
                drag = event.mimeData()
                drag_text = self.currentWidget().objectName() if self.count() > 0 else ""

                mime_data = self.create_mime_data(drag_text)
                drag = Qt.QDrag(self)
                drag.setMimeData(mime_data)
                drag.setHotSpot(event.pos() - self.rect().topLeft())

                drop_action = drag.exec_()

    def create_mime_data(self, text):
        mime_data = Qt.QMimeData()
        mime_data.setText(text)
        return mime_data

class DraggableWorkspaceApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.central_widget = DraggableTabWidget()
        self.setCentralWidget(self.central_widget)

        self.create_tabs()

        self.setWindowTitle("Draggable Workspace App")
        self.setGeometry(100, 100, 800, 600)

    def create_tabs(self):
        tab1 = QWidget()
        tab1.setObjectName("Tab 1")
        tab_layout1 = QVBoxLayout(tab1)
        tab_layout1.addWidget(QLabel("Content of Tab 1"))
        self.central_widget.addTab(tab1, "Tab 1")

        tab2 = QWidget()
        tab2.setObjectName("Tab 2")
        tab_layout2 = QVBoxLayout(tab2)
        tab_layout2.addWidget(QLabel("Content of Tab 2"))
        self.central_widget.addTab(tab2, "Tab 2")

        tab3 = QWidget()
        tab3.setObjectName("Tab 3")
        tab_layout3 = QVBoxLayout(tab3)
        tab_layout3.addWidget(QLabel("Content of Tab 3"))
        self.central_widget.addTab(tab3, "Tab 3")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    draggable_workspace_app = DraggableWorkspaceApp()
    draggable_workspace_app.show()
    sys.exit(app.exec())
