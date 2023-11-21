import sys
from typing import Optional
from PySide6 import QtWidgets
import PySide6.QtCore as QtCore
import PySide6.QtCore
import PySide6.QtWidgets as QtWidgets
import PySide6.QtWidgets
import repackage
repackage.up()
from view.user.CreateUser import Ui_CreateUser

class CreateUserController(QtWidgets.QWidget, Ui_CreateUser):
    def __init__(self):
        super(CreateUserController, self).__init__()
        self.setupUi(self)

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = CreateUserController()
    window.show()
    sys.exit(app.exec())