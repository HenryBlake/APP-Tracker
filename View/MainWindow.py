import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout,QListWidget,QMainWindow
from View.ClickBtn import ClickBtn
from View.InputText import InputText
from View.AnyText import AnyText
from Model.AppInfo import AppInfo
from Controller.AppDoc import AppDoc
from Controller.Timers import Timers
from Controller.Trackers import Trackers
from View.ListView import ListView
from View.AlertView import AlertView

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
        self.app_list=ListView()
        self.alter_view=None
        self.app_list.itemClicked.connect(self.list_clicked)
        self.save_btn=ClickBtn("Save")
        # self.gen_text=AnyText("Test Content!")
        self.in_text=InputText("Write your app here.")
        self.save_btn.clicked.connect(self.btn_clicked)
       
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
         self.app_list.addItem(index["app_name"])
   
    def btn_clicked(self):
      return self.save_btn_clicked(self.app_info,self.app_list,self.in_text)

    def save_btn_clicked(self,app_info,app_list,in_text):
       data=app_info.appInfoGetter()
       app_name=in_text.text()
       if app_info.appNameCheck(app_name,data)==False:
          app_info.appInfoCreator(app_name,data)
          app_list.addItem(app_name)
          in_text.setText("")
       else:
         #  print("app exsits")
          return AlertView("app exsits")

    def closeEvent(self, a0):
       self.app_info.appInfoSetter("steam",200)
       return super().closeEvent(a0)   
#TODO:Once user click it,show the run time
    def list_clicked(self):
       app_name=self.app_list.currentItem().text()
       app_pid=Trackers().pidTracker(app_name) 
       if app_pid==None:
            # print("The process is not runing!")
            return AlertView("The process is not runing!")
       else:
                     
      #  print(app_pid)
        print(Timers().timeCal(app_pid))
      # print(self.app_list.currentItem().text())
#TODO:When user double cilcked it,show alert and chooes weather it will be deleted.
    def list_double_clicked(self):
       return