'''Module that controls login window'''
import logging
from PySide6 import QtWidgets
from niches.view.Ui_Login import Ui_Login
from niches.util.Encryptor import Encryptor
from niches.model.dao.UserDao import UserDao
from niches.model.mapper.UserMapper import UserMapper
from niches.model.dto.UserDto import UserDto
from niches.model.entity.User import User
from niches.controller.error_controller import ErrorController
from niches.util.Validator import Validator
from niches.util.Constants import UserTypeKey, UserField
from niches.util.Constants import LOGIN_ERROR
from niches.util.Constants import USER_NOT_EXIST
from niches.model.mapper.UserTypeMapper import UserTypeMapper
from niches.model.dao.UserTypeDao import UserTypeDao
from niches.model.dto.UserTypeDto import UserTypeDto

class LoginController(QtWidgets.QDialog, Ui_Login):
    '''Class with the functionality of login window'''
    def __init__(self):
        super(LoginController, self).__init__()
        self.setupUi(self)
        self.__user_type_key = UserTypeKey.NOT_LOGGED.value
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
            self.__validator.validate_is_not_empty(self.line_edit_user.text(),
                                                   UserField.USER_NAME)
            self.__validator.validate_is_not_empty(self.line_edit_password.text(),
                                                   UserField.PASSWORD)
            user = self.__user_dao.find_active_user_by_user_name(self.line_edit_user.text())
            user_dto = self.__user_mapper.user_to_user_dto(user)
            if (user_dto.get_user_name() == self.line_edit_user.text() 
                and 
                self.__encryptor.check_password(self.line_edit_password.text(), user.get_password())
                and user_dto is not None):
                user_type_dto = UserTypeDto()
                user_type_dto = self.__user_type_mapper.user_type_to_user_type_dto(
                    self.__user_type_dao.find_by_id(user_dto.get_user_type_id()))
                print(user_type_dto.get_key())
                self.__user_type_key = user_type_dto.get_key()
                self.close()
            else:
                self.__error_controller.handle_exception_error(LOGIN_ERROR)
                self.__error_controller.show()
        except ValueError as ve:
            logging.exception(ve)
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()        
        except TypeError as e:
            logging.exception(e)
            self.__error_controller.handle_exception_error(USER_NOT_EXIST)
            self.__error_controller.show()
        except Exception as e:
            logging.exception(e)
            self.__error_controller.handle_exception_error(USER_NOT_EXIST)
            self.__error_controller.show()
    def __set_windows_by_user_type(self, user_type_key:str):
        self.__user_type_key = user_type_key
    def get_logged_user_type_key(self):
        '''Returns user_type_key'''
        return self.__user_type_key
    def __guest(self):
        self.__user_type_key = UserTypeKey.GUEST.value
        self.close()
