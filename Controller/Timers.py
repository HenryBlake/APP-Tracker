#TODO:merge the timecal and other functions about time into  this class
import time,psutil
class Timers():
    def __init__(self):
     self.app_time=0
     self.current_time=0
     self.last_time=0
# current-(last-create)=run_time 
    def timeCal(self,app_pid):
     self.last_time=self.current_time
     self.current_time=time.time()-self.createionTime(app_pid)
     print(f"The current time:{self.current_time}")
     self.app_time=self.current_time-self.last_time
     print(f"The run time:{self.app_time}")
     print(f"The last time:{self.last_time}")
     return self.app_time
    
    def createionTime(self,app_pid):
     create_time= psutil.Process(app_pid).create_time()
     return create_time
