from PyQt6.QtWidgets import QWidget,QHBoxLayout,QLabel
from View.ListView import ListView
from Model.AppInfo import AppInfo
from View.TrackerText import TrackerText
class AppInfoView(QWidget):
    def __init__(self): 
      super().__init__()
      info_layout=QHBoxLayout()
      self.app_info=AppInfo()
    #   widget=QWidget()
      self.app_list=ListView()
      self.app_info_label=TrackerText()
      info_layout.addWidget(self.app_list)
      info_layout.addWidget(self.app_info_label)
    #   widget.setLayout(info_layout)
      self.setLayout(info_layout)
      self.load_apps()
      
    def load_apps(self):
       for index in self.app_info.appInfoGetter():
         self.app_list.addItem(index["app_name"])

    def appListGetter(self):
       return self.app_list
    
    def infoLableGetter(self):
       return self.app_info_label
