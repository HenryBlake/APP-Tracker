class AppInfo:
    def __init__(self):
        self.app_name="Steam.exe"
        self.app_run_time=0

    def nameSetter(self,name):
        self.app_name=name
    
    def timeSetter(self,time):
        self.app_run_time=time

    def nameGetter(self):
        return self.app_name
    
    def timeGetter(self):
        return self.app_run_time