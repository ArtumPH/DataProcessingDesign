# Buttons.py
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtGui import QIcon

#Plot_Diagram_Buttons
class Button_With_Image(QPushButton):
    def __init__(self, parent, image_path):
        super().__init__(parent)
        self.setFlat(True)
        self.setStyleSheet("border: none;")
        self.icon = QIcon(image_path)
        self.setIcon(self.icon)
        self.setIconSize(self.icon.actualSize(self.size()))
        #self.setIconSize(self.size())
        #self.clicked.connect(self.on_click)
    '''
    def on_click(self):
        print('Image Button Clicked')
    '''
        
#Excel_Buttons
class Excel_Load_Button:
    def __init__(self, table_widget):
        self.load_button = QPushButton('Load Excel')
        self.load_button.clicked.connect(lambda: self.load_excel(table_widget))

    def load_excel(self, table_widget):
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            table_widget.load_data_from_excel(file_name)

class Excel_read_seleced_data_Button:
    def __init__(self, table_widget,text_edit):
        self.read_button = QPushButton('Read Selected Data')
        
        self.read_button.clicked.connect(lambda: self.read_selected_data(table_widget,text_edit))

    def read_selected_data(self, table_widget, text_edit):
        selected_data_matrix, selected_data_columns = table_widget.get_selected_data()

        if selected_data_matrix is not None:
            dispaly_text=table_widget.display_selected_data(selected_data_matrix, selected_data_columns)
            text_edit.display_selected_data(dispaly_text)
            