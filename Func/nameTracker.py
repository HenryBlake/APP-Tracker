import psutil
class nameTracker:
    def findName(self,app_pid):
        try:
            process=psutil.Process(app_pid)
            return process.name()
        except psutil.NoSuchProcess:
            return None