import sys
from PySide6 import QtWidgets
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from Ui_Login import Ui_Login
from Encryptor import Encryptor
from UserDao import UserDao
from UserMapper import UserMapper
from UserDto import UserDto
from User import User
from ErrorController import ErrorController
from Validator import Validator
from Constants import *

class LoginController(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.__user_dao = UserDao()
        self.__encryptor = Encryptor()
        self.__user_mapper = UserMapper()
        self.__error_controller = ErrorController()
        self.__validator = Validator()
        self.push_button_login.clicked.connect(self.__login)
        self.push_button_guest.clicked.connect(self.__guest)
        self.line_edit_password.returnPressed.connect(self.__login)
    
    def __login(self):
        user_dto = UserDto()
        user = User()
        try:
            self.__validator.validate_is_not_empty(self.line_edit_user.text(), UserField.USER_NAME)
            self.__validator.validate_is_not_empty(self.line_edit_password.text(), UserField.PASSWORD)
            user = self.__user_dao.find_by_user_name(self.line_edit_user.text())
            user_dto = self.__user_mapper.user_to_user_dto(user)
            if user_dto.get_user_name() == self.line_edit_user.text() and self.__encryptor.check_password(self.line_edit_password.text(), user.get_password()):
                print("Login")
                self.close()
            else:
                self.__error_controller.handle_exception_error("Error en login. Verifica tu usuario y contraseña")
                self.__error_controller.show()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
        
        except TypeError as e:
            self.__error_controller.handle_exception_error("El usuario no existe.")
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

            
    
    def __guest(self):
        print("guest")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginController()
    window.show()
    sys.exit(app.exec())
