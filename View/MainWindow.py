import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout,QListWidget,QMainWindow
from View.ClickBtn import ClickBtn
from View.InputText import InputText
from View.AnyText import AnyText
from Model.AppInfo import AppInfo
from Controller.AppDoc import AppDoc

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_info=AppInfo()
        self.app_doc=AppDoc()
        # self.window=None
        layout=QVBoxLayout()
        widget=QWidget()
        self.app_title="Apptracker"
        self.setWindowTitle(self.app_title)
        self.resize(320,160)
        self.app_list=QListWidget()
        self.save_btn=ClickBtn("Save")
        # self.gen_text=AnyText("Test Content!")
        self.in_text=InputText("Write your app here.")
        # self.save_btn.clicked.connect(slot=self.btn_clicked)
       
        layout.addWidget(self.app_list)      
        # layout.addWidget(self.gen_text)
        layout.addWidget(self.in_text)
        layout.addWidget(self.save_btn)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # self.setLayout(layout)
        self.load_apps()
    
    def load_apps(self):
       for index in self.app_info.appInfoGetter():
        #  if index["app_name"].lower() == "steam":
        #     print(index["run_time"])
         self.app_list.addItem(index["app_name"])
    
    def btn_clicked(self):
       return self.app_info.appInfoSetter("steam",150)
   
    def closeEvent(self, a0):
       self.app_info.appInfoSetter("steam",200)
       return super().closeEvent(a0)   
    