import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout,QListWidget
from View.ClickBtn import ClickBtn
from View.InputText import InputText
from View.AnyText import AnyText
from Model.AppInfo import AppInfo

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.app_info=AppInfo()
        # self.window=None
        layout=QVBoxLayout()
        self.app_title="Apptracker"
        self.setWindowTitle(self.app_title)
        self.resize(320,160)
        self.app_list=QListWidget()
        self.save_btn=ClickBtn("Save")
        # self.gen_text=AnyText("Test Content!")
        self.in_text=InputText("Write your app here.")
        # self.save_btn.clicked.connect()
       
        layout.addWidget(self.app_list)      
        # layout.addWidget(self.gen_text)
        layout.addWidget(self.in_text)
        layout.addWidget(self.save_btn)
        self.setLayout(layout)
        self.load_apps()
    
    def load_apps(self):
       for index in self.app_info.nameGetter():
         self.app_list.addItem(index["app_name"])
        #  print("btn clicked")
    
   
        
       

    # def initWindow(self):
    #     self.window.setWindowTitle(self.app_title)
    #     self.window.resize(320,160)
    #     return self.window