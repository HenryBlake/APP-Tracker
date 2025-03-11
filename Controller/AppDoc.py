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
#Only use for save app name to list
    def writeAPP(self,app_name):
        data=self.readApp()
        try:
            with open(self.json_path_name,"w",encoding="utf-8") as file:
                # data=json.load(file)
                app_data={"app_name":app_name,"run_time":0.00}
                data.append(app_data)
                json.dump(data,file,indent=4)
                # print(data)
                print(f"Writing {app_name}")
        except FileNotFoundError:
                print("The file is not found!")
        except json.JSONDecodeError:
                print("Decoder ERROR!")
        print(f"{app_name} is recoeded")

#Only use for read app name to list
    def readApp(self):
         try: 
            with open(self.json_path_name,"r",encoding="utf-8") as file:
                data=json.load(file)
                return data
         except FileNotFoundError:
                print("The file is not found!")
         except json.JSONDecodeError:
                print("Decoder ERROR!")
    
    def createionTime(self,app_pid):
        create_time= psutil.Process(app_pid).create_time()
        return create_time
    
    def diffNameCheck(self,app_name):
         self.app_list=self.readApp()

         for app in self.app_list:
              if app_name in app["app_name"]:
                   print("app is exist")
              else:
                 self.writeAPP(app_name)
            #   print(app["app_name"])
#TODO:create a function that calculate the Time and another one to record time in file
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
    
    def runTimeSave(self,run_time):
         return
#Check if there are apps with same names
    def process_check(self,app_pid):
        if app_pid==None:
            print("The process is not runing!")
        else:
            print(f"The {app_pid} is runing right now!")