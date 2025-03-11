import sys
from PyQt6.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QVBoxLayout
from View.ClickBtn import ClickBtn
from View.InputText import InputText

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # self.window=None
        layout=QVBoxLayout()
        self.app_title="Apptracker"
        self.setWindowTitle(self.app_title)
        self.resize(320,160)
        self.save_btn=ClickBtn("Save")
        self.in_text=InputText("Write your app here.")

        layout.addWidget(self.in_text)
        layout.addWidget(self.save_btn)
        self.setLayout(layout)

    # def initWindow(self):
    #     self.window.setWindowTitle(self.app_title)
    #     self.window.resize(320,160)
    #     return self.window