import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from niches.view.Ui_CreateUser import Ui_CreateUser
from niches.model.dto.UserDto import UserDto
from niches.util.Constants import UserField
from niches.controller.ErrorController import ErrorController
from niches.model.dao.UserTypeDao import UserTypeDao
from niches.model.dao.UserDao import UserDao
from niches.model.mapper.UserMapper import UserMapper
from niches.util.Validator import Validator

class CreateUserController(QtWidgets.QWidget, Ui_CreateUser):
    def __init__(self):
        super(CreateUserController, self).__init__()
        self.setupUi(self)
        self.push_button_save.clicked.connect(self.__save_user)
        self.push_button_clean.clicked.connect(self.__clean)
        self.__user_type_dao = UserTypeDao()
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()
        self.__error_controller = ErrorController()
        self.__validator = Validator()
        self.__list_user_type = self.__user_type_dao.find_all()
        for user_type in self.__list_user_type:
            self.combo_box_user_type.addItem(user_type.get_name(), user_type)
        #self.combo_box_user_type.set

    def __clean(self):
        self.line_edit_name.clear()
        self.line_edit_paternal_surname.clear()
        self.line_edit_maternal_surname.clear()
        self.line_edit_user_name.clear()
        self.line_edit_password.clear()
        self.line_edit_repeat_password.clear()

    def __save_user(self):
        user_dto = UserDto()
        try: 
            self.__validator.validate_is_not_empty(self.line_edit_name.text(), UserField.NAME)
            self.__validator.validate_is_not_empty(self.line_edit_paternal_surname.text(), UserField.PATERNAL_SURNAME)
            self.__validator.validate_is_not_empty(self.line_edit_maternal_surname.text(), UserField.MATERNAL_SURNAME)
            self.__validator.validate_is_not_empty(self.line_edit_user_name.text(), UserField.USER_NAME)
            self.__validator.validate_is_not_empty(self.line_edit_password.text(), UserField.PASSWORD)
            self.__validator.validate_is_not_empty(self.line_edit_repeat_password.text(), UserField.PASSWORD)
            self.__validator.validate_password(self.line_edit_password.text(), self.line_edit_repeat_password.text())
            
            user_dto.new_user(
                self.line_edit_name.text(),
                self.line_edit_paternal_surname.text(),
                self.line_edit_maternal_surname.text(),
                int(self.combo_box_user_type.currentData().get_id()),
                self.line_edit_user_name.text(),
                self.line_edit_password.text()
            )

            self.__user_dao.create_user(self.__user_mapper.user_dto_to_user(user_dto))
            self.__clean()
            self.__error_controller.handle_value_error("El usuario se ha creado exitosamente")
            self.__error_controller.show()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
        
        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()