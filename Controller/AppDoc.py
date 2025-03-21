import psutil,json,time,asyncio
from View.AlertView import AlertView

class AppDoc:
    def __init__(self):
        self.app_time=0
        self.json_path_name="Model/app_time_doc.json"
        self.app_list=[]
        self.current_time=0
        self.last_time=0

#Check if there are apps with same names
    def process_check(self,app_pid):
        if app_pid==None:
            # print("The process is not runing!")
            return "The process is not runing!"
        else:
            print(f"The {app_pid} is runing right now!")
#TODO:Create a function for normalize the Time and another one to chcek the content is not null or wrong.