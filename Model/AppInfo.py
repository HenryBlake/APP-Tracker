import json
from View.AlertView import AlertView
from Controller.Trackers import Trackers
import json
class AppInfo:
    def __init__(self):
        self.app_name="Steam.exe"
        self.app_run_time=0
        self.app_pid=0
        self.json_path_name="./app_time_doc.json"

    def appInfoSetter(self,name,run_time,pid):
        self.app_name=name
        self.app_run_time=run_time
        self.app_pid=pid
        data=self.appInfoGetter()

        for index in data:
             if self.app_name and self.app_name.lower() in index["app_name"].lower():
                  index["run_time"]=self.app_run_time
                  index["pid"]=self.app_pid
        try:
           with open(self.json_path_name,"w",encoding="utf-8") as file:
               json.dump(data,file,indent=4)
        except FileNotFoundError:
                return "The file is not found!"
        except json.JSONDecodeError:
                return "Decoder ERROR!"
    
    def appInfoGetter(self):
       try: 
           with open(self.json_path_name,"r",encoding="utf-8") as file:
                data=json.load(file) 
                return data
       except FileNotFoundError:
                 print("The file is not found! Creating a new one...")
                 with open(self.json_path_name, "w", encoding="utf-8") as file:
                  json.dump([], file)  # write an empty list to create a valid JSON file
                 return []
       except json.JSONDecodeError:
                return "Decoder ERROR!"
       
    def appInfoCreator(self,app_name,data):
         try:
           with open(self.json_path_name,"w",encoding="utf-8") as file:
                 pid=Trackers().pidTracker(app_name)
                 app_data={"app_name":app_name,"run_time":0.00,"pid":pid}
                 data.append(app_data)
                 json.dump(data,file,indent=4)
                 print(f"Writing {app_name}")
         except FileNotFoundError:
                    return "The file is not found!"
         except json.JSONDecodeError:
                    return "Decoder ERROR!"        
         print(f"{app_name} is recoeded")
    
    def appNameCheck(self,app_name,data):
         if any(index["app_name"].lower() in app_name.lower() for index in data):
             return True
         else:
             return False
#TODO:Create the function that could remove the app information in app_time_doc        
    def appInfoDelete():
          return
