import sys
from PyQt6.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsRectItem, QGraphicsLineItem, QGraphicsSimpleTextItem, QGraphicsItem
from PyQt6.QtCore import Qt

class DiagramPicker(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        scene = QGraphicsScene(self)
        self.setScene(scene)

        self.setWindowTitle("Diagram Picker")
        self.setGeometry(100, 100, 800, 600)

        self.create_shapes()

    def create_shapes(self):
        scene = self.scene()

        ellipse = QGraphicsEllipseItem(0, 0, 100, 50)
        ellipse.setPos(50, 50)
        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        scene.addItem(ellipse)

        rectangle = QGraphicsRectItem(0, 0, 100, 50)
        rectangle.setPos(200, 50)
        rectangle.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        rectangle.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        scene.addItem(rectangle)

        line = QGraphicsLineItem(0, 0, 100, 0)
        line.setPos(400, 75)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        line.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        scene.addItem(line)

        text = QGraphicsSimpleTextItem("Text")
        text.setPos(600, 50)
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        text.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        scene.addItem(text)

    def mousePressEvent(self, event):
        item = self.itemAt(event.pos())
        if item:
            print(f"Selected Item: {type(item)}")

        super().mousePressEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    diagram_picker = DiagramPicker()
    diagram_picker.show()
    sys.exit(app.exec())
