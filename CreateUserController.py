import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
#import dto.UserDto as UserDto
from UserDto import UserDto
from Constants import *
from ErrorController import ErrorController
from CreateUser import Ui_CreateUser
from UserTypeDao import UserTypeDao
from UserDao import UserDao
from UserMapper import UserMapper

class CreateUserController(QtWidgets.QWidget, Ui_CreateUser):
    def __init__(self):
        super(CreateUserController, self).__init__()
        self.setupUi(self)
        self.push_button_save.clicked.connect(self.save_user)
        self.push_button_clean.clicked.connect(self.clean)
        self.__user_type_dao = UserTypeDao()
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()
        self.__list_user_type = self.__user_type_dao.find_all()
        for user_type in self.__list_user_type:
            self.combo_box_user_type.addItem(user_type.get_name(), user_type)
        #self.combo_box_user_type.set

    def clean(self):
        self.line_edit_name.clear()
        self.line_edit_paternal_surname.clear()
        self.line_edit_maternal_surname.clear()
        self.line_edit_user_name.clear()
        self.line_edit_password.clear()
        self.line_edit_repeat_password.clear()

    def save_user(self):
        user_dto = UserDto()
        try: 
            self.validate_is_not_empty(self.line_edit_name.text(), UserField.NAME)
            self.validate_is_not_empty(self.line_edit_paternal_surname.text(), UserField.PATERNAL_SURNAME)
            self.validate_is_not_empty(self.line_edit_maternal_surname.text(), UserField.MATERNAL_SURNAME)
            self.validate_is_not_empty(self.line_edit_user_name.text(), UserField.USER_NAME)
            self.validate_is_not_empty(self.line_edit_password.text(), UserField.PASSWORD)
            self.validate_is_not_empty(self.line_edit_repeat_password.text(), UserField.PASSWORD)
            self.validate_password(self.line_edit_password.text(), self.line_edit_repeat_password.text())
            
            user_dto.new_user(
                self.line_edit_name.text(),
                self.line_edit_paternal_surname.text(),
                self.line_edit_maternal_surname.text(),
                int(self.combo_box_user_type.currentData().get_id()),
                self.line_edit_user_name.text()
            )

            self.__user_dao.create_user(self.__user_mapper.user_dto_to_user(user_dto))
            self.clean()
            error_controller.handle_value_error("El usuario se ha creado exitosamente")
            error_controller.show()

        except ValueError as ve:
            error_controller.handle_value_error(ve)
            error_controller.show()
        
        except Exception as e:
            error_controller.handle_exception_error(e)
            error_controller.show()
        
    def validate_is_not_empty(self, string:str, name:UserField):
        if len(string) != 0:
            pass
        else:
            raise ValueError(THE_FIELD_LABEL + name + SHOULD_NOT_BE_EMPTY_LABEL)
        
    def validate_password(self, password, repeated_password):
        if password == repeated_password:
            pass
        else:
            raise ValueError("Las contraseñas deben ser iguales")
        
        if len(password) >= 10:
            pass
        else:
            raise ValueError("La contraseña debe tener al menos 10 caracteres")

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = CreateUserController()
    window.show()
    error_controller = ErrorController()
    sys.exit(app.exec())