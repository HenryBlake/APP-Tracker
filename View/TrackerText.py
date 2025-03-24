from PyQt6.QtWidgets import QLabel
class TrackerText(QLabel):
    def __init__(self):
        super().__init__()
        self.setText("Hello World!")
        self.app_name="Steam"
        self.app_run_time=None
        self.app_pid=0
    
    def getTrackerText(self):
        self.setText(
            # f"App name: {self.app_name}\nRun time: {self.app_run_time[0]} Days {self.app_run_time[1]} Hours {self.app_run_time[2]} Minutes\nPID: {self.app_pid}"
            f"App name: {self.app_name}\nRun time: {self.app_run_time}\nPID: {self.app_pid}"

        )

    def getTotalTrackerText(self):
        self.setText(
            # f"App name: {self.app_name}\nRun time: {self.app_run_time[0]} Days {self.app_run_time[1]} Hours {self.app_run_time[2]} Minutes\nPID: {self.app_pid}"
            f"App name: {self.app_name}\nTotal Run time: {self.app_run_time}\nPID: {self.app_pid}"

        )
    
    def setAppInfo(self,name,time,pid):
        self.app_name=name
        self.app_run_time=time
        self.app_pid=pid
    