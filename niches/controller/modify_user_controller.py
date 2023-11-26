"""
Module that controls ModifyUser widget
"""
from PySide6 import QtWidgets
from niches.view.Ui_ModifyUser import Ui_ModifyUser
from niches.controller.error_controller import ErrorController
from niches.model.dao.UserDao import UserDao
from niches.model.dto.UserDto import UserDto
from niches.model.mapper.UserMapper import UserMapper
from niches.model.dao.UserTypeDao import UserTypeDao
from niches.model.dto.UserTypeDto import UserTypeDto
from niches.model.mapper.UserTypeMapper import UserTypeMapper
from niches.util.Constants import UserField
from niches.util.Validator import Validator

class ModifyUserController(QtWidgets.QWidget, Ui_ModifyUser):
    """
    Class with the functionality of ModifyUser widget

    Args:
        QtWidgets (QtWidgets.QWidget): Core QWidget
        Ui_ModifyUser (Ui_ModifyUser): Qt layer transformed to python code 
    """
    def __init__(self):
        super(ModifyUserController, self).__init__()
        self.setupUi(self)
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()
        self.__user_type_dao = UserTypeDao()
        self.__user_type_mapper = UserTypeMapper()
        self.__error_controller = ErrorController()
        self.__validator = Validator()
        self.__list_user_type = self.__user_type_dao.find_all()
        self.__user_id = 0
        for user_type in self.__list_user_type:
            self.combo_box_user_type.addItem(user_type.get_name(), user_type)
        self.push_button_save.clicked.connect(self.__update)
        self.push_button_deactivate.clicked.connect(self.__deactivate)
        self.push_button_activate.clicked.connect(self.__activate)

    def __deactivate(self):
        try:
            self.__user_dao.deactivate_user(self.__user_id)
            self.__error_controller.handle_value_error("El usuario se ha desactivado")
            self.__error_controller.show()
            self.close()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__user_dao.reactivate_user(self.__user_id)
            self.__error_controller.handle_value_error("El usuario se ha activado")
            self.__error_controller.show()
            self.close()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __update(self):
        user_dto = UserDto()
        try:
            self.__validator.validate_is_not_empty(self.line_edit_name.text(),
                                                   UserField.NAME)
            self.__validator.validate_is_not_empty(self.line_edit_paternal_surname.text(),
                                                   UserField.PATERNAL_SURNAME)
            self.__validator.validate_is_not_empty(self.line_edit_maternal_surname.text(),
                                                   UserField.MATERNAL_SURNAME)
            user_dto = self.__user_mapper.user_to_user_dto(
                self.__user_dao.find_by_id(self.__user_id))
            user_dto.set_name(self.line_edit_name.text())
            user_dto.set_paternal_surname(self.line_edit_paternal_surname.text())
            user_dto.set_maternal_surname(self.line_edit_maternal_surname.text())
            user_dto.set_user_type_id(self.combo_box_user_type.currentData().get_id())
            print(user_dto)

            self.__user_dao.modify_user(self.__user_mapper.user_dto_to_user(user_dto))
            #self.__clean()
            self.__error_controller.handle_value_error("El usuario se ha modificado exitosamente")
            self.__error_controller.show()
            self.close()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def load_user(self, id:int):
        """
        Loads the user on widget searching by its id
        """
        self.__user_id = id
        user_dto = UserDto()
        user_dto = self.__user_mapper.user_to_user_dto(self.__user_dao.find_by_id(id))
        user_type_dto = UserTypeDto()
        user_type_dto = self.__user_type_mapper.user_type_to_user_type_dto(
            self.__user_type_dao.find_by_id(user_dto.get_user_type_id()))
        self.line_edit_name.setText(user_dto.get_name())
        self.line_edit_paternal_surname.setText(user_dto.get_paternal_surname())
        self.line_edit_maternal_surname.setText(user_dto.get_maternal_surname())
        self.combo_box_user_type.setCurrentText(user_type_dto.get_name())
