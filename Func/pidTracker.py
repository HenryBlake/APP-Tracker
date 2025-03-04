#This funcation will find the PID of Applications and return them to next step
import psutil
class pidTracker:
    def findPID(self,app_name):
        for process in psutil.process_iter(attrs=["pid","name"]):
            # print(f"Checking: {process.info}") 
            if process.info["name"] and app_name.lower() in process.info["name"]:
                # print(process.info["name"])
                return process.info["pid"]
        return None