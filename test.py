import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class PlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.figure, self.ax = Figure(), Figure().add_subplot()
        self.canvas = FigureCanvas(self.figure)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.canvas)

        self.plot_data()

    def plot_data(self):
        # Example data: a sine wave
        x = np.linspace(0, 2 * np.pi, 100)
        y = np.sin(x)

        # Plot the data
        self.ax.plot(x, y)

        # Set labels and title
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Matplotlib Plot in PyQt6')

        # Draw the plot
        self.canvas.draw()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = PlotWidget()
        self.setCentralWidget(self.central_widget)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('PyQt6 and Matplotlib Plot Example')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
