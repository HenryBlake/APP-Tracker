from PyQt6.QtWidgets import QApplication,QWidget
import sys
import asyncio
import psutil
import time
from Func.pidTracker import pidTracker
from Func.processRuningCheck import processRuningCheck
from Func.nameTracker import nameTracker
from Func.appDoc import AppDoc

# app=QApplication(sys.argv)
# window=QWidget()
# window.show()
# app.exec()
#Init area
pid_tracker=pidTracker()
name_tracker=nameTracker()
runingCheck=processRuningCheck()
appDoc=AppDoc()
#Init area ends


app_name="steam.exe"
app_name=input("Please Input Your App'name: ")
if input("Do you want to save app?").lower() == "y":
    # print(appDoc.readApp())
    appDoc.diffNameCheck(app_name)
else:
    print("")
app_pid=pid_tracker.findPID(app_name)
# runingCheck.process_check(app_pid)

#Test if we can read the list of apps
# app_list=appDoc.readApp()
# print(app_list)

async def testFunc(app_pid):
    while True:
        if psutil.pid_exists(app_pid):
            print(f"{app_name} is runing, has been runing for {appDoc.createionTime(app_pid)} seconds")
            # print(time.time() - psutil.Process(app_pid).create_time())
        else:
            print(f"the {app_name} is not runing")
        await asyncio.sleep(5)
#Start Aysnc
# asyncio.run(testFunc(app_pid))
     