from PyQt6.QtWidgets import QApplication,QWidget
import sys
import asyncio
import psutil
import time
from Controller.AppDoc import AppDoc
from View.MainWindow import MainWindow

#Init area

appDoc=AppDoc()
app=QApplication(sys.argv)
#TODO: Lean and Create the GUI.
#Window container

# app_window=MainWindow().initWindow()
app_window=MainWindow()
app_window.show()
#Excute the window
sys.exit(app.exec())

#TODO(Refactor):Refactor appDoc,name and pid tracker files.Merge the name and pid tracker into one file.