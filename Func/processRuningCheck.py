import psutil
class processRuningCheck:
    def process_check(self,app_pid):
        if app_pid==None:
            print("The process is not runing!")
        else:
            print(f"The {app_pid} is runing right now!")
            
    