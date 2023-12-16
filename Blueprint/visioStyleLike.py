import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsItem, QVBoxLayout, QWidget, QPushButton

class VisioApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Visio-like App")
        self.setGeometry(100, 100, 800, 600)

        # Create the main layout
        layout = QVBoxLayout(self)

        # Create graphics view and scene
        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        layout.addWidget(self.view)

        # Create button to add rectangles
        add_rect_button = QPushButton("Add Rectangle")
        add_rect_button.clicked.connect(self.add_rectangle)
        layout.addWidget(add_rect_button)

    def add_rectangle(self):
        rect_item = QGraphicsRectItem(0, 0, 100, 50)
        rect_item.setPos(50, 50)
        rect_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rect_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.scene.addItem(rect_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    visio_app = VisioApp()
    visio_app.show()
    sys.exit(app.exec())
