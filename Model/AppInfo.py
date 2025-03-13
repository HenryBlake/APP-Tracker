import json
class AppInfo:
    def __init__(self):
        self.app_name="Steam.exe"
        self.app_run_time=0
        self.json_path_name="Model/app_time_doc.json"

    def nameSetter(self,name):
        self.app_name=name
    
    def timeSetter(self,time):
        self.app_run_time=time

    def nameGetter(self):
       try: 
           with open(self.json_path_name,"r",encoding="utf-8") as file:
                data=json.load(file)
                return data
       except FileNotFoundError:
                return "The file is not found!"
       except json.JSONDecodeError:
                return "Decoder ERROR!"
    
    
    def timeGetter(self):
        return self.app_run_time