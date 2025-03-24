import psutil
class Trackers:
    def nameTracker(self,app_pid):
        try:
            process=psutil.Process(app_pid)
            return process.name()
        except psutil.NoSuchProcess:
            return None
        
    def pidTracker(self,app_name):
        for process in psutil.process_iter(attrs=["pid","name"]):
            # print(f"Checking: {process.info}") 
            if process.info["name"] and app_name.lower() in process.info["name"].lower():
                # print(process.info["name"])
                return process.info["pid"]
        return None
