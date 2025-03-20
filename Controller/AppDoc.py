import psutil
import json
import time
import asyncio

class AppDoc:
    def __init__(self):
        self.app_time=0
        self.json_path_name="Model/app_time_doc.json"
        self.app_list=[]
        self.current_time=0
        self.last_time=0
    
    def createionTime(self,app_pid):
        create_time= psutil.Process(app_pid).create_time()
        return create_time
    
    def diffNameCheck(self,app_name,app_list):
         for app in app_list:
              if app_name in app["app_name"]:
                   return
              else:
                print("app exsits")
                #  self.writeAPP(app_name)
            #   print(app["app_name"])
               

# current-(last-create)=run_time 
#return the time period since last saved time.
    def timeCal(self,app_pid):
          self.last_time=self.current_time
        # print(f"The last time:{self.last_time}")
          self.current_time=time.time()-self.createionTime(app_pid)
          print(f"The current time:{self.current_time}")
          self.app_time=self.current_time-self.last_time
          print(f"The run time:{self.app_time}")
          print(f"The last time:{self.last_time}")
          return self.app_time
    
    
#Check if there are apps with same names
    def process_check(self,app_pid):
        if app_pid==None:
            print("The process is not runing!")
        else:
            print(f"The {app_pid} is runing right now!")
#TODO:Create a function for normalize the Time and another one to chcek the content is not null or wrong.