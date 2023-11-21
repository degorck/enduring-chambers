import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
import repackage
repackage.up()
from view.user.CreateUser import Ui_CreateUser
from model.dto.UserDto import UserDto
from constants.Constants import *
from ErrorController import ErrorController

class CreateUserController(QtWidgets.QWidget, Ui_CreateUser):
    def __init__(self):
        super(CreateUserController, self).__init__()
        self.setupUi(self)
        self.push_button_save.clicked.connect(self.save_user)
    
    def save_user(self):
        user_dto = UserDto()
        try: 
            self.validate_is_not_empty(self.line_edit_name.text(), UserField.NAME)
            self.validate_is_not_empty(self.line_edit_paternal_surname.text(), UserField.PATERNAL_SURNAME)
            self.validate_is_not_empty(self.line_edit_maternal_surname.text(), UserField.MATERNAL_SURNAME)
            self.validate_is_not_empty(self.line_edit_user_name.text(), UserField.USER_NAME)
            self.validate_is_not_empty(self.line_edit_password.text(), UserField.PASSWORD)
            self.validate_is_not_empty(self.line_edit_repeat_password.text(), UserField.PASSWORD)
            
            user_dto.new_user(
            self.line_edit_name.text(),
            self.line_edit_name.text(),
            self.line_edit_maternal_surname.text(),
            1,
            self.label_user_name.text()
            )
            print(user_dto.get_name())
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
            raise ValueError("El campo " + name + " no debe estar vacío") 

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = CreateUserController()
    window.show()
    error_controller = ErrorController()
    sys.exit(app.exec())