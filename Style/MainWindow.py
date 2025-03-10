import sys
from PyQt6.QtWidgets import QApplication,QWidget

class MainWindow():
    def __init__(self):
        super().__init__
        self.window=None
        self.app_title="Apptracker"
        self.initWindow()

    def initWindow(self):
        self.window=QWidget()
        self.window.setWindowTitle(self.app_title)
        self.window.resize(160,80)
        return self.window
        
        
