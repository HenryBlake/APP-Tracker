import psutil
import json
import time
class AppDoc:
    def __init__(self):
        self.app_time=0
        self.json_path_name="app_log_doc/app_time_doc.json"
        self.app_list=[]
#Only use for save app name to list
    def writeAPP(self,app_name):
        data=self.readApp()
        try:
            with open(self.json_path_name,"w",encoding="utf-8") as file:
                # data=json.load(file)
                app_data={"name":app_name,"run_time":0.00}
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
        self.app_time= time.time()-psutil.Process(app_pid).create_time()
        return self.app_time
    
    def diffNameCheck(self,app_name):
         self.app_list=self.readApp()

         for app in self.app_list:
              if app_name in app["app_name"]:
                   print("app is exist")
              else:
                 self.writeAPP(app_name)
            #   print(app["app_name"])
#TODO:create a function that calculate the Time and another one to save time in file
    def timeCal(time1,time2):
         return
    
    def runTimeSave(run_time):
         return