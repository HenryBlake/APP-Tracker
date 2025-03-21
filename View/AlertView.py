from PyQt6.QtWidgets import QDialog


class AlertView(QDialog):
    def __init__(self,title):
        super().__init__()
        self.setMaximumSize(80,45)
        self.setWindowTitle(title)
        self.exec()
    