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
#Window container

# app_window=MainWindow().initWindow()
app_window=MainWindow()
app_window.show()
#Excute the window
sys.exit(app.exec())