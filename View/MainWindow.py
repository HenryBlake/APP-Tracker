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
from View.AppInfoView import AppInfoView
from View.TrackerText import TrackerText

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.app_info=AppInfo()
        self.app_doc=AppDoc()
        self.app_info_view=AppInfoView()
        # self.window=None
        layout=QVBoxLayout()
        widget=QWidget()
        self.app_title="Apptracker"
        self.setWindowTitle(self.app_title)
        self.resize(320,160)
        self.app_list=self.app_info_view.appListGetter()
        self.app_tracker_text=self.app_info_view.infoLableGetter()
        self.alter_view=None
        self.app_list.itemClicked.connect(self.list_clicked)
        self.app_list.itemDoubleClicked.connect(self.list_double_clicked)
        self.save_btn=ClickBtn("Save")
        # self.gen_text=AnyText("Test Content!")
        self.in_text=InputText("Write your app here.")
        self.save_btn.clicked.connect(self.btn_clicked)
        #Append widgets here
        layout.addWidget(self.app_info_view)
      #   layout.addWidget(self.app_tracker_text)
      #   layout.addWidget(self.app_list)      
        # layout.addWidget(self.gen_text)
        layout.addWidget(self.in_text)
        layout.addWidget(self.save_btn)
       
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # self.setLayout(layout)
      #   self.load_apps()
    
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
       
    def aoutoSaveTime(self):
      data=self.app_info.appInfoGetter()
      for index in data:
        pid=Trackers().pidTracker(index["app_name"])
        if pid!=None:
          if pid==index["pid"]:
            time=Timers().timeCal(pid)
            self.app_info.appInfoSetter(index["app_name"],int(time),index["pid"])
            print("pid is same")
          if pid!=index["pid"]:
            time=index["run_time"]+Timers().timeCal(pid)
            self.app_info.appInfoSetter(index["app_name"],int(time),pid)
            print("pid is different")
#TODO:if pid equals pid berfore then document time=this time if not then plus them.
    def closeEvent(self, a0):
      #  data=self.app_info.appInfoGetter()
      #  for index in data:
      #     pid=Trackers().pidTracker(index["app_name"])
      #     if pid!=None:
      #      if pid==index["pid"]:
      #       time=Timers().timeCal(pid)
      #       self.app_info.appInfoSetter(index["app_name"],int(time),index["pid"])
      #       print("pid is same")
          
      #      if pid!=index["pid"]:
      #       time=index["run_time"]+Timers().timeCal(pid)
      #       self.app_info.appInfoSetter(index["app_name"],int(time),pid)
      #       print("pid is different")
       self.aoutoSaveTime()
       return super().closeEvent(a0)   

    def list_clicked(self):
       app_name=self.app_list.currentItem().text()
       app_pid=Trackers().pidTracker(app_name) 
       if app_pid==None:
            return AlertView("The process is not runing!")
       else:
        time=Timers().timeCal(app_pid)
        format_time=self.app_doc.timeCovertor(time)
        self.app_tracker_text.setAppInfo(app_name,format_time,app_pid)
        self.app_tracker_text.getTrackerText()
      # print(self.app_list.currentItem().text())
#Show the total run time
    def list_double_clicked(self):
       self.aoutoSaveTime()
       app_name=self.app_list.currentItem().text()
       app_pid=Trackers().pidTracker(app_name)
       for index in self.app_info.appInfoGetter():
          if app_name in index["app_name"]:
             format_time=self.app_doc.timeCovertor(index["run_time"])
             self.app_tracker_text.setAppInfo(app_name,format_time,app_pid)
             self.app_tracker_text.getTotalTrackerText()
      #  return AlertView("cant find app")
    
