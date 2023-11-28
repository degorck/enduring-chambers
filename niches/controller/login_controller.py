'''Module that controls login window'''
import logging
from PySide6 import QtWidgets
from niches.view.Ui_Login import Ui_Login
from niches.util.encryptor import Encryptor
from niches.model.dao.user_dao import UserDao
from niches.model.mapper.user_mapper import UserMapper
from niches.model.dto.user_dto import UserDto
from niches.model.entity.user import User
from niches.controller.error_controller import ErrorController
from niches.util.validator import validate_is_not_empty
from niches.constants.constants import UserTypeKey, UserField
from niches.constants.constants import LOGIN_ERROR
from niches.constants.constants import USER_NOT_EXIST
from niches.model.mapper.user_type_mapper import UserTypeMapper
from niches.model.dao.user_type_dao import UserTypeDao
from niches.model.dto.user_type_dto import UserTypeDto

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
        self.__logged_user_dto = UserDto()
        self.push_button_login.clicked.connect(self.__login)
        self.push_button_guest.clicked.connect(self.__guest)
        self.line_edit_password.returnPressed.connect(self.__login)
        self.__set_windows_by_user_type(self.__user_type_key)

    def __login(self):
        user_dto = UserDto()
        user = User()
        try:
            validate_is_not_empty(self.line_edit_user.text(),
                                                   UserField.USER_NAME)
            validate_is_not_empty(self.line_edit_password.text(),
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
                self.__logged_user_dto.existing_user(
                    user_dto.get_id(),
                    user_dto.get_name(),
                    user_dto.get_paternal_surname(),
                    user_dto.get_maternal_surname(),
                    user_dto.get_user_type_id(),
                    user_dto.get_user_name()
                )
                self.__logged_user_dto.set_password(user_dto.get_password())
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

    def get_logged_user(self):
        '''Returns logged_user_dto'''
        return self.__logged_user_dto

    def __guest(self):
        self.__user_type_key = UserTypeKey.GUEST.value
        self.close()
