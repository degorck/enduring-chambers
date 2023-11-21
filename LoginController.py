import sys
from PySide6 import QtWidgets
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
import repackage
repackage.up()
from view.Login import Ui_Login

class LoginController(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.push_button_login.clicked.connect(self.login)
        self.push_button_guest.clicked.connect(self.guest)
        self.line_edit_password.returnPressed.connect(self.login)
    
    def login(self):
        print(self.line_edit_user.text())
        print(self.line_edit_password.text())
        print("login")
    
    def guest(self):
        print("guest")

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = LoginController()
    window.show()
    sys.exit(app.exec())
