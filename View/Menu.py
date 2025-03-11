from PyQt6.QtWidgets import QApplication,QLabel,QLineEdit,QPushButton

class Menu:
    def __init__(self):
        super().__init__
        
    def inputText(self,input_hint):
        input_text=QLineEdit(input_hint)
        return input_text
    def setButton(self,btn_text):
        btn=QPushButton(btn_text)
        return btn
#There are four elements in this menu
#1.A textfield to allow user to input process name;
#2.A text to show the name and other informaton of process that choosed by user;
#3.A button that refresh the text to let it show the process;
#4.A button that save how much time this process spend;
    