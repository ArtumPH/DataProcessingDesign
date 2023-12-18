# CollapsibleWidget.py
from PyQt6.QtWidgets import (QWidget, QToolButton, QScrollArea, 
                             QSizePolicy, QFrame, QVBoxLayout, 
                             QApplication, QMainWindow, QDockWidget, 
                             QScrollArea, QLabel)
from PyQt6.QtCore import (Qt, QParallelAnimationGroup, QPropertyAnimation, 
                          pyqtSlot, QAbstractAnimation)
from PyQt6.QtGui import QColor

class CollapsibleWidget(QWidget):
    def __init__(self, title="", parent=None):
        super().__init__(parent)

        self.toggle_button = QToolButton(text=title, checkable=True, checked=False)
        self.toggle_button.setStyleSheet("QToolButton { border: none; }")
        self.toggle_button.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toggle_button.setArrowType(Qt.ArrowType.RightArrow)
        self.toggle_button.pressed.connect(self.on_pressed)

        self.toggle_animation = QParallelAnimationGroup(self)

        self.content_area = QScrollArea(maximumHeight=0, minimumHeight=0)
        self.content_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.content_area.setFrameShape(QFrame.Shape.NoFrame)

        Collapsible_widget_layout = QVBoxLayout(self)
        Collapsible_widget_layout.setSpacing(0)
        Collapsible_widget_layout.setContentsMargins(0, 0, 0, 0)
        Collapsible_widget_layout.addWidget(self.toggle_button)
        Collapsible_widget_layout.addWidget(self.content_area)

        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"minimumHeight"))
        self.toggle_animation.addAnimation(QPropertyAnimation(self, b"maximumHeight"))
        self.toggle_animation.addAnimation(QPropertyAnimation(self.content_area, b"maximumHeight"))

    @pyqtSlot()
    def on_pressed(self):
        checked = self.toggle_button.isChecked()
        self.toggle_button.setArrowType(Qt.ArrowType.DownArrow if not checked else Qt.ArrowType.RightArrow)
        self.toggle_animation.setDirection(QAbstractAnimation.Direction.Forward if not checked else QAbstractAnimation.Direction.Backward)
        self.toggle_animation.start()

    def setContentLayout(self, layout):
        Collapsible_widget_layout = self.content_area.layout()
        del Collapsible_widget_layout
        self.content_area.setLayout(layout)
        collapsed_height = (self.sizeHint().height() - self.content_area.maximumHeight())
        content_height = layout.sizeHint().height()
        for i in range(self.toggle_animation.animationCount()):
            animation = self.toggle_animation.animationAt(i)
            animation.setDuration(0) #Change value to control the speed of the drop-down animation
            animation.setStartValue(collapsed_height)
            animation.setEndValue(collapsed_height + content_height)

        content_animation = self.toggle_animation.animationAt(self.toggle_animation.animationCount() - 1)
        content_animation.setDuration(0) #Need to pass same value animation.setDuration(0) to work
        content_animation.setStartValue(0)
        content_animation.setEndValue(content_height)

if __name__ == "__main__":
    import sys
    import random

    app = QApplication(sys.argv)

    w = QMainWindow()
    w.setCentralWidget(QWidget())
    dock = QDockWidget("Collapsible Demo")
    w.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
    scroll = QScrollArea()
    dock.setWidget(scroll)
    content = QWidget()
    scroll.setWidget(content)
    scroll.setWidgetResizable(True)
    vlay = QVBoxLayout(content)
    for i in range(10):
        box = CollapsibleWidget("Collapsible Box Header-{}".format(i))
        vlay.addWidget(box)
        lay = QVBoxLayout()
        for j in range(8):
            label = QLabel("{}".format(j))
            color = QColor(*[random.randint(0, 255) for _ in range(3)])
            label.setStyleSheet(
                "background-color: {}; color : white;".format(color.name())
            )
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lay.addWidget(label)

        box.setContentLayout(lay)
    vlay.addStretch()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec())
