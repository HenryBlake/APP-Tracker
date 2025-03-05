import psutil
import json
import time
class AppDoc:
    def __init__(self):
        self.app_time=0
        self.json_path_name="app_log_doc/app_time_doc.json"
        self.app_list={}

    def writeAPP(self,app_name):
        print(f"Writing {app_name}")

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
        #  for app_name in self.app_list["app_name"]:
        #     if app_name and app_name.lower() in self.app_list["app_name"].lower():
        #       print("app exsists!")
        #     else:
        #       self.writeAPP(app_name)
        #  return None
         if app_name.lower() in self.app_list.values():
              print("app exsists")
         else :
              self.writeAPP(app_name)