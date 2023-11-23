import sys
from PySide6 import QtWidgets
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from niches.view.Ui_Login import Ui_Login
from niches.util.Encryptor import Encryptor
from niches.model.dao.UserDao import UserDao
from niches.model.mapper.UserMapper import UserMapper
from niches.model.dto.UserDto import UserDto
from niches.model.entity.User import User
from niches.controller.ErrorController import ErrorController
from niches.util.Validator import Validator
from niches.util.Constants import *
from niches.model.mapper.UserTypeMapper import UserTypeMapper
from niches.model.dao.UserTypeDao import UserTypeDao
from niches.model.dto.UserTypeDto import UserTypeDto

class LoginController(QtWidgets.QDialog, Ui_Login):
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.__user_type_key = UserTypeKey.GUEST
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()
        self.__encryptor = Encryptor()
        self.__user_type_dao = UserTypeDao()
        self.__user_type_mapper = UserTypeMapper()
        self.__error_controller = ErrorController()
        self.__validator = Validator()
        self.push_button_login.clicked.connect(self.__login)
        self.push_button_guest.clicked.connect(self.__guest)
        self.line_edit_password.returnPressed.connect(self.__login)
        self.__set_windows_by_user_type(self.__user_type_key)
    
    def __login(self):
        user_dto = UserDto()
        user = User()
        try:
            self.__validator.validate_is_not_empty(self.line_edit_user.text(), UserField.USER_NAME)
            self.__validator.validate_is_not_empty(self.line_edit_password.text(), UserField.PASSWORD)
            user = self.__user_dao.find_by_user_name(self.line_edit_user.text())
            user_dto = self.__user_mapper.user_to_user_dto(user)
            if user_dto.get_user_name() == self.line_edit_user.text() and self.__encryptor.check_password(self.line_edit_password.text(), user.get_password()):
                user_type_dto = UserTypeDto()
                user_type_dto = self.__user_type_mapper.user_type_to_user_type_dto(self.__user_type_dao.find_by_id(user_dto.get_user_type_id()))
                print(user_type_dto.get_key())
                self.__user_type_key = user_type_dto.get_key()
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

    def __set_windows_by_user_type(self, user_type_key:str):
        self.__user_type_key = user_type_key

    def get_logged_user_type_key(self):
        return self.__user_type_key

    
    def __guest(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginController()
    window.show()
    sys.exit(app.exec())
