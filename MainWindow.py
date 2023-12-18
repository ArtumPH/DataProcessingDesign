# MainWindow.py
import sys
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import QAction, QFileSystemModel
from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget, 
                             QVBoxLayout, QHBoxLayout, QMenu,
                             QMenuBar, QStatusBar, QDockWidget,
                             QTreeView, QTabWidget, QLabel,
                             QTextEdit, QFileDialog, QGridLayout,
                             QScrollArea)
from TableWidget import ExcelTableWidget
from Buttons import Button_With_Image
from ComboBoxes import ExcelComboBoxes
from TextEdit import ExcelTextEdit
from ListWidget import ExcelListWidget
from CollapsibleWidgets import CollapsibleWidget
#from Menubar_functions import Menu_Open

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Data Analysis")
        self.setGeometry(200, 150, 1500, 800)

        self.table_widget = ExcelTableWidget()
        self.tab_widget = self.create_tab_widget()
        self.selected_data_display_text = ExcelTextEdit()
    # Plot Area Widgets
        self.plot_scroll_area = QScrollArea()
        self.plot_scroll_area_content=QWidget()
        
        self.pairwise_data_choose_layout = QGridLayout()
        self.statistical_distributions_choose_layout = QGridLayout()
        self.gridded_data_choose_layout = QGridLayout()
        self.irregularly_gridded_data_choose_layout = QGridLayout()
        self.three_d_and_volumetric_data_choose_layout = QGridLayout()

        self.pairwise_data_choose_widget = CollapsibleWidget("Pairwise data",self)
        self.statistical_distributions_choose_widget = CollapsibleWidget("Statistical distributions",self)
        self.gridded_data_choose_widget = CollapsibleWidget("Gridded data",self)
        self.irregularly_gridded_data_choose_widget = CollapsibleWidget("Irregularly gridded data",self)
        self.three_d_and_volumetric_data_choose_widget = CollapsibleWidget("3D and volumetric data",self)

        # Pairwise data plots Choose Buttons
        self.plot_x_y_button = Button_With_Image(self,"GrassTexture.jpg") # Replace with the actual path to image
        self.scatter_x_y_button = Button_With_Image(self,"GrassTexture.jpg")
        self.bar_x_height_button = Button_With_Image(self,"GrassTexture.jpg")
        self.stem_x_y_button = Button_With_Image(self,"GrassTexture.jpg")
        self.fill_between_x_y1_y2_Button = Button_With_Image(self,"GrassTexture.jpg")
        self.stackplot_x_y_button = Button_With_Image(self,"GrassTexture.jpg")
        self.stairs_values_button = Button_With_Image(self,"GrassTexture.jpg")

        # Statistical distributions plots Choose Buttons
        self.hist_x_button = Button_With_Image(self,"GrassTexture.jpg")
        self.boxplot_x_button = Button_With_Image(self,"GrassTexture.jpg")
        self.errorbar_x_y_yerr_xerr_button = Button_With_Image(self,"GrassTexture.jpg")
        self.violinplot_D_button= Button_With_Image(self,"GrassTexture.jpg")
        self.eventplot_D_button = Button_With_Image(self,"GrassTexture.jpg")
        self.hist2d_x_y_button = Button_With_Image(self,"GrassTexture.jpg")
        self.hexbin_x_y_C_button = Button_With_Image(self,"GrassTexture.jpg")
        self.pie_x_button = Button_With_Image(self,"GrassTexture.jpg")
        self.ecdf_x_button = Button_With_Image(self,"GrassTexture.jpg")

        # Gridded data plots Choose Buttons
        self.imshow_Z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.pcolormesh_X_Y_Z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.contour_X_Y_Z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.contourf_X_Y_Z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.barbs_X_Y_U_V_button = Button_With_Image(self,"GrassTexture.jpg")
        self.quiver_X_Y_U_V_button = Button_With_Image(self,"GrassTexture.jpg")
        self.streamplot_X_Y_U_V_button = Button_With_Image(self,"GrassTexture.jpg")

        # Irregularly gridded data plots Choose Buttons
        self.tricontour_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.tricontourf_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.trisurf_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.triplot_x_y_button = Button_With_Image(self,"GrassTexture.jpg")

        # 3D and volumetric data plots Choose Buttons
        self.scatter3D_xs_ys_zs_button = Button_With_Image(self,"GrassTexture.jpg")
        self.plot_surface_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.plot_trisurf_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
        self.voxels_x_y_z_filled_button = Button_With_Image(self,"GrassTexture.jpg")
        self.plot_wireframe_x_y_z_button = Button_With_Image(self,"GrassTexture.jpg")
    #----------------------------------------------------------------------------

        # Central tab widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)
        self.layout.addWidget(self.tab_widget)
        '''
        self.excel_load_button = Excel_Load_Button(self.table_widget)
        self.layout.addWidget(self.excel_load_button.load_button)
        
        self.excel_read_button = Excel_read_seleced_data_Button(self.table_widget,self.selected_data_display_text)
        self.layout.addWidget(self.excel_read_button.read_button)
        
        self.text_edit = ExcelTextEdit()
        self.layout.addWidget(self.text_edit)
        
        self.comboboxes = ExcelComboBoxes()
        self.layout.addWidget(self.comboboxes.x_axis_combobox)
        self.layout.addWidget(self.comboboxes.y_axis_combobox)
        
        self.list_widget = ExcelListWidget()
        self.layout.addWidget(self.list_widget)
        '''

        #----------------------------------------------------------------------------

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        # Actions
        new_action = QAction("New Tab", self)
        new_action.triggered.connect(self.create_new_tab)
        file_menu.addAction(new_action)

        open_action = QAction("Open File...", self)
        open_action.triggered.connect(lambda: self.load_excel(self.table_widget))
        file_menu.addAction(open_action)

        read_action = QAction("Read Selected Data", self)
        read_action.triggered.connect(lambda: self.read_selected_data(self.table_widget,self.selected_data_display_text))
        file_menu.addAction(read_action)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)

        edit_menu = menubar.addMenu("Edit")
        view_menu = menubar.addMenu("View")

        # Toolbar
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.addAction(new_action)
        toolbar.addAction(open_action)
        toolbar.addAction(read_action)
        toolbar.addAction(save_action)

        # Status bar
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_label = QLabel("Ready")
        status_bar.addWidget(status_label)

        # Docked widget for file explorer
        explorer_dock = QDockWidget("Explorer", self)
        explorer_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        explorer_tree = self.create_file_explorer()
        explorer_dock.setWidget(explorer_tree)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, explorer_dock)
        
        # Docked widget for Plot types Area
        plot_types_dock = QDockWidget("Plot", self)
        plot_types_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        plot_types_dock.setWidget(self.plot_scroll_area)
        self.plot_scroll_area.setWidget(self.plot_scroll_area_content)
        self.plot_scroll_area.setWidgetResizable(True)
        self.plot_type_layout=QVBoxLayout(self.plot_scroll_area_content)

#####################################From here to fix the problem#####################################                

        self.plot_type_layout.addWidget(self.pairwise_data_choose_widget)
        self.plot_type_layout.addWidget(self.statistical_distributions_choose_widget)
        self.plot_type_layout.addWidget(self.gridded_data_choose_widget)
        self.plot_type_layout.addWidget(self.irregularly_gridded_data_choose_widget)
        self.plot_type_layout.addWidget(self.three_d_and_volumetric_data_choose_widget)

        self.pairwise_data_choose_layout.addWidget(self.plot_x_y_button,0,0)
        self.pairwise_data_choose_layout.addWidget(self.scatter_x_y_button,0,1)
        self.pairwise_data_choose_layout.addWidget(self.bar_x_height_button,0,2)
        self.pairwise_data_choose_layout.addWidget(self.stem_x_y_button,0,3)
        self.pairwise_data_choose_layout.addWidget(self.fill_between_x_y1_y2_Button,0,4)
        self.pairwise_data_choose_layout.addWidget(self.stackplot_x_y_button,1,0)
        self.pairwise_data_choose_layout.addWidget(self.stairs_values_button,1,1)

        self.statistical_distributions_choose_layout.addWidget(self.hist_x_button,0,0)
        self.statistical_distributions_choose_layout.addWidget(self.boxplot_x_button,0,1)
        self.statistical_distributions_choose_layout.addWidget(self.errorbar_x_y_yerr_xerr_button,0,2)
        self.statistical_distributions_choose_layout.addWidget(self.violinplot_D_button,0,3)
        self.statistical_distributions_choose_layout.addWidget(self.eventplot_D_button,0,4)
        self.statistical_distributions_choose_layout.addWidget(self.hist2d_x_y_button,1,0)
        self.statistical_distributions_choose_layout.addWidget(self.hexbin_x_y_C_button,1,1)
        self.statistical_distributions_choose_layout.addWidget(self.pie_x_button,1,2)
        self.statistical_distributions_choose_layout.addWidget(self.ecdf_x_button,1,3)

        self.gridded_data_choose_layout.addWidget(self.imshow_Z_button,0,0)
        self.gridded_data_choose_layout.addWidget(self.pcolormesh_X_Y_Z_button,0,1)
        self.gridded_data_choose_layout.addWidget(self.contour_X_Y_Z_button,0,2)
        self.gridded_data_choose_layout.addWidget(self.contourf_X_Y_Z_button,0,3)
        self.gridded_data_choose_layout.addWidget(self.barbs_X_Y_U_V_button,0,4)
        self.gridded_data_choose_layout.addWidget(self.quiver_X_Y_U_V_button,1,0)
        self.gridded_data_choose_layout.addWidget(self.streamplot_X_Y_U_V_button,1,1)

        self.irregularly_gridded_data_choose_layout.addWidget(self.tricontour_x_y_z_button,0,0)
        self.irregularly_gridded_data_choose_layout.addWidget(self.tricontourf_x_y_z_button,0,1)
        self.irregularly_gridded_data_choose_layout.addWidget(self.trisurf_x_y_z_button,0,2)
        self.irregularly_gridded_data_choose_layout.addWidget(self.triplot_x_y_button,0,3)

        self.three_d_and_volumetric_data_choose_layout.addWidget(self.scatter3D_xs_ys_zs_button,0,0)
        self.three_d_and_volumetric_data_choose_layout.addWidget(self.plot_surface_x_y_z_button,0,1)
        self.three_d_and_volumetric_data_choose_layout.addWidget(self.plot_trisurf_x_y_z_button,0,2)
        self.three_d_and_volumetric_data_choose_layout.addWidget(self.voxels_x_y_z_filled_button,0,3)
        self.three_d_and_volumetric_data_choose_layout.addWidget(self.plot_wireframe_x_y_z_button,0,4)

        self.pairwise_data_choose_widget.setContentLayout(self.pairwise_data_choose_layout)
        self.statistical_distributions_choose_widget.setContentLayout(self.statistical_distributions_choose_layout)
        self.gridded_data_choose_widget.setContentLayout(self.gridded_data_choose_layout)
        self.irregularly_gridded_data_choose_widget.setContentLayout(self.irregularly_gridded_data_choose_layout)
        self.three_d_and_volumetric_data_choose_widget.setContentLayout(self.three_d_and_volumetric_data_choose_layout)

        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, plot_types_dock)

        # Docked widget for loaded data table Area
        data_load_dock = QDockWidget("Loaded data", self)
        data_load_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        data_load_dock.setWidget(self.selected_data_display_text)
        data_load_dock.setMinimumSize(500,500)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, data_load_dock)

        # Docked widget for After use
        after_use_dock = QDockWidget("After use", self)
        after_use_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetFloatable | QDockWidget.DockWidgetFeature.DockWidgetMovable)
        #after_use_dock.setWidget(self.)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, after_use_dock)

        # Combine docked widgets
        self.tabifyDockWidget(data_load_dock, plot_types_dock)

        # Raise docked widgets(Needs after combine docked widgets to work)
        data_load_dock.raise_()

        # Add context menu
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.on_context_menu)

    # Add load_excel method
    def load_excel(self, table_widget):
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Excel File", "", "Excel Files (*.xlsx);;All Files (*)")

        if file_name:
            table_widget.load_data_from_excel(file_name)

    #Add read_selected_data method
    def read_selected_data(self, table_widget, text_edit):
        selected_data_matrix, selected_data_columns = table_widget.get_selected_data()

        if selected_data_matrix is not None:
            dispaly_text=table_widget.display_selected_data(selected_data_matrix, selected_data_columns)
            text_edit.display_selected_data(dispaly_text)
            

    # Add on_context_menu method
    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(self.mapToGlobal(pos))

    def create_tab_widget(self):
        tab_widget = QTabWidget(self)
        tab_widget.setTabsClosable(True)
        tab_widget.setMovable(True)
        tab_widget.tabCloseRequested.connect(self.close_tab)

        # Create initial tab
        tab_widget.addTab(self.table_widget, "Untitled")

        return tab_widget

    def create_new_tab(self):
        text_editor = QTextEdit(self.tab_widget)
        self.tab_widget.addTab(text_editor, "Untitled")

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

    def create_file_explorer(self):
        explorer_tree = QTreeView()
        model = QFileSystemModel()
        
        # Set the root path to the current directory
        model.setRootPath(QDir.currentPath())

        explorer_tree.setModel(model)
        explorer_tree.setRootIndex(model.index(QDir.currentPath()))
        explorer_tree.setColumnWidth(0, 200)
        explorer_tree.setHeaderHidden(True)
        explorer_tree.clicked.connect(self.file_explorer_clicked)

        return explorer_tree

    def file_explorer_clicked(self, index):
        model = self.sender().model()
        file_path = model.filePath(index)
        status_label = self.statusBar().findChild(QLabel)
        status_label.setText(f"Selected: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
