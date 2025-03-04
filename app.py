from PyQt6.QtWidgets import QApplication,QWidget
import sys
import asyncio
import psutil
from Func.pidTracker import pidTracker
from Func.processRuningCheck import processRuningCheck
from Func.nameTracker import nameTracker
# app=QApplication(sys.argv)
# window=QWidget()
# window.show()
# app.exec()
#Init area
pid_tracker=pidTracker()
name_tracker=nameTracker()
runingCheck=processRuningCheck()
#Init area ends


app_name="steam.exe"
app_name=input("Please Input Your App'name: ")
app_pid=pid_tracker.findPID(app_name)
# runingCheck.process_check(app_pid)
async def testFunc(app_pid):
    while True:
        if psutil.pid_exists(app_pid):
            print(f"{app_name} is runing")
        else:
            print(f"the {app_name} is not runing")
        await asyncio.sleep(5)

asyncio.run(testFunc(app_pid))
# runingCheck.process_check(app_pid)
# print(app_pid)
# for process in psutil.process_iter(attrs=["pid","name"]):
#     print(process.info)
# for process in psutil.process_iter(attrs=["pid","name"]):
#             # print(f"Checking: {process.info}") 
#         if process.info["name"] and app_name.lower() in process.info["name"]:
#             print (process.info["pid"])
     