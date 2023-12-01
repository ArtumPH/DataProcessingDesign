import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QSlider
from PyQt6.QtCore import Qt

class ScaleTableApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget(3, 3)
        self.populate_table()

        self.scale_label = QLabel('Scale Factor:')
        
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(1, 200)
        self.slider.setValue(100)
        self.slider.valueChanged.connect(self.update_scaling)

        self.original_font_size = self.table_widget.font().pointSize()

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.scale_label)
        layout.addWidget(self.slider)

        self.setLayout(layout)
        self.setWindowTitle('Scale Table App')
        self.setGeometry(100, 100, 400, 300)

    def populate_table(self):
        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = QTableWidgetItem(f'Row {row} Col {col}')
                self.table_widget.setItem(row, col, item)

    def update_scaling(self):
        scale_factor = self.slider.value() / 100.0  # Adjust the division factor based on your needs
        self.scale_table(scale_factor)

    def scale_table(self, factor):
        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, col)
                if item is not None:
                    font = item.font()
                    new_point_size = max(int(self.original_font_size * factor), 1)
                    font.setPointSize(new_point_size)
                    item.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scale_table_app = ScaleTableApp()
    scale_table_app.show()
    sys.exit(app.exec())
