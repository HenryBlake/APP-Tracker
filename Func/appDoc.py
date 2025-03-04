import psutil
import json
class AppDoc:
    def writeAPP(self,app_list):
        for name in app_list:
            return json.dump(app_list)
    def readApp(self,app_list_doc):
        for name in app_list_doc:
            return json.load(app_list_doc)
