from PyQt6.QtWidgets import QLineEdit

class InputText(QLineEdit):
    def __init__(self,placeholder):
      super().__init__()
      self.setPlaceholderText(placeholder)
