from PyQt6.QtWidgets import QApplication,QWidget
import sys
import asyncio
import psutil
import time
from Controller.AppDoc import AppDoc
from View.MainWindow import MainWindow
from View.Menu import Menu

#Init area

appDoc=AppDoc()
app=QApplication(sys.argv)
main_window=MainWindow()
#TODO: Lean and Create the GUI.
#Window container

app_window=main_window.initWindow()
app_window.show()
#Excute the window
sys.exit(app.exec())

#TODO(Refactor):Refactor appDoc,name and pid tracker files.Merge the name and pid tracker into one file.