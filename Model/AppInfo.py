import json
class AppInfo:
    def __init__(self):
        self.app_name="Steam.exe"
        self.app_run_time=0
        self.json_path_name="Model/app_time_doc.json"

    def appInfoSetter(self,name,run_time):
        self.app_name=name
        self.app_run_time=run_time
        data=self.appInfoGetter()

        for index in data:
             if self.app_name and self.app_name.lower() in index["app_name"].lower():
                  index["run_time"]=self.app_run_time
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
                return "The file is not found!"
       except json.JSONDecodeError:
                return "Decoder ERROR!"
       
    def appInfoCreator(self,app_name,data):
         try:
           with open(self.json_path_name,"w",encoding="utf-8") as file:
                 app_data={"app_name":app_name,"run_time":0.00}
                 data.append(app_data)
                 json.dump(data,file,indent=4)
                 print(f"Writing {app_name}")
         except FileNotFoundError:
                    return "The file is not found!"
         except json.JSONDecodeError:
                    return "Decoder ERROR!"        
         print(f"{app_name} is recoeded")
    
    def appNameCheck(self,app_name,data):
         if any(entry["app_name"].lower() in app_name.lower() for entry in data):
             return True
         else:
             return False
#TODO:Create the function that could remove the app infro in app_time_doc        
    def appInfoDelete():
          return