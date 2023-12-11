"""
User Controller Module
"""
from PySide6 import QtWidgets
from niches.model.dto.user_dto import UserDto
from niches.util.validator import validate_is_not_empty, validate_password
from niches.constant.constants import UserField, UserTypeKey, HASHED_BOOLEAN_CONVERTER_IS_ACTIVE
from niches.controller.error_controller import ErrorController
from niches.service.user_service import UserService
from niches.service.user_type_service import UserTypeService
from niches.util.logging_configuration import get_loging
from niches.view.ui.main_window import Ui_MainWindow
logging = get_loging()

class UserController:
    """
    User controller class
    Args:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__error_controller = ErrorController()
        self.__user_service = UserService()
        self.__user_type_service = UserTypeService()
        self.__row = 0
        self.__configure_combo_box()
        self.__configure_actions()

    def __configure_actions(self):
        self.main_window.push_button_create_user_create.clicked.connect(
            self.main_window.scroll_area_create_user.show)
        self.main_window.push_button_create_user_save_user.clicked.connect(self.__save_user)
        self.main_window.line_edit_search_users.textChanged.connect(self.__search_users)
        self.main_window.push_button_create_user_clean_user.clicked.connect(
            self.__clean_stacked_widget_users)
        self.main_window.push_button_users.clicked.connect(self.__set_stacked_widget_users)
        self.main_window.push_button_modify_user_save.clicked.connect(self.__update_user)
        self.main_window.push_button_modify_user_activate.clicked.connect(self.__activate)
        self.main_window.push_button_modify_user_deactivate.clicked.connect(self.__deactivate)
        self.main_window.table_widget_users.cellDoubleClicked.connect(self.__select_user)

    def __clean_stacked_widget_users(self):
        self.main_window.line_edit_create_user_name.clear()
        self.main_window.line_edit_create_user_paternal_surname.clear()
        self.main_window.line_edit_create_user_maternal_surname.clear()
        self.main_window.line_edit_create_user_user_name.clear()
        self.main_window.line_edit_create_user_password.clear()
        self.main_window.line_edit_create_user_repeat_password.clear()

    def __search_users(self):
        if self.main_window.get_logged_user_type_key() == UserTypeKey.ADMINISTRATOR.value:
            list_user_dto = self.__user_service.search_users(
                self.main_window.line_edit_search_users.text())
        else:
            list_user_dto = self.__user_service.search_active_users(
                self.main_window.line_edit_search_users.text())
        self.__row = len(list_user_dto)
        self.__configure_table()
        row = 0

        for user_dto in list_user_dto:
            self.main_window.table_widget_users.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(user_dto.get_user_name())))
            self.main_window.table_widget_users.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                user_dto.get_name()))
            self.main_window.table_widget_users.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                user_dto.get_paternal_surname()))
            self.main_window.table_widget_users.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                user_dto.get_maternal_surname()))
            self.main_window.table_widget_users.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                    self.__hash_list_user_type[user_dto.get_user_type_id()]))
            self.main_window.table_widget_users.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                HASHED_BOOLEAN_CONVERTER_IS_ACTIVE[str(user_dto.is_active())]))
            self.main_window.table_widget_users.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                    str(user_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_users.setItem(
                row,
                7,
                QtWidgets.QTableWidgetItem(
                    str(user_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_users.resizeColumnsToContents()
            row = row + 1

    def __configure_combo_box(self):
        self.__list_user_type_dto = self.__user_type_service.find_all()
        self.__hash_list_user_type = {}
        for user_type_dto in self.__list_user_type_dto:
            self.main_window.combo_box_create_user_user_type.addItem(
                user_type_dto.get_name(), user_type_dto)
            self.main_window.combo_box_modify_user_user_type.addItem(
                user_type_dto.get_name(), user_type_dto)
            self.__hash_list_user_type[user_type_dto.get_id()] = user_type_dto.get_name()

    def __configure_table(self):
        self.main_window.table_widget_users.clear()
        self.main_window.table_widget_users.setRowCount(self.__row)
        self.main_window.table_widget_users.setColumnCount(8)
        self.main_window.table_widget_users.setHorizontalHeaderLabels(("Nombre de Usuario",
                                                           "Nombre",
                                                           "Apellido Paterno",
                                                           "Apellido Materno",
                                                           "Tipo de usuario",
                                                           "Activo",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_users.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_users.resizeColumnsToContents()

    def __save_user(self):
        user_dto = UserDto()
        try:
            validate_is_not_empty(
                self.main_window.line_edit_create_user_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_user_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_user_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_user_user_name.text(),
                UserField.USER_NAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_user_password.text(),
                UserField.PASSWORD)
            validate_is_not_empty(
                self.main_window.line_edit_create_user_repeat_password.text(),
                UserField.PASSWORD)
            validate_password(self.main_window.line_edit_create_user_password.text(),
                              self.main_window.line_edit_create_user_repeat_password.text())

            user_dto.new_user(
                self.main_window.line_edit_create_user_name.text(),
                self.main_window.line_edit_create_user_paternal_surname.text(),
                self.main_window.line_edit_create_user_maternal_surname.text(),
                int(self.main_window.combo_box_create_user_user_type.currentData().get_id()),
                self.main_window.line_edit_create_user_user_name.text(),
                self.main_window.line_edit_create_user_password.text()
            )

            self.__user_service.create_user(user_dto)
            self.__clean_stacked_widget_users()
            self.main_window.scroll_area_create_user.hide()
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("User created")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __clean_stacked_widget_users(self):
        self.main_window.line_edit_create_user_name.clear()
        self.main_window.line_edit_create_user_paternal_surname.clear()
        self.main_window.line_edit_create_user_maternal_surname.clear()
        self.main_window.line_edit_create_user_user_name.clear()
        self.main_window.line_edit_create_user_password.clear()
        self.main_window.line_edit_create_user_repeat_password.clear()

    def __set_stacked_widget_users(self):
        self.__search_users()
        self.main_window.scroll_area_create_user.hide()
        self.main_window.scroll_area_modify_user.hide()
        self.main_window.push_button_deceased.setChecked(False)
        self.main_window.push_button_holders.setChecked(False)
        self.main_window.push_button_my_account.setChecked(False)
        self.main_window.push_button_niches.setChecked(False)
        self.main_window.push_button_users.setChecked(True)
        self.main_window.stacked_widget.setCurrentIndex(1)
        logging.debug("Users stacked widget selected")

    def __select_user(self):
        row = self.main_window.table_widget_users.currentRow()
        user_name = self.main_window.table_widget_users.item(row, 0).text()
        self.main_window.scroll_area_modify_user.show()
        self.__load_user(user_name)

    def __load_user(self, user_name:str):
        user_dto = self.__user_service.find_user_by_user_name(user_name)
        self.main_window.set_loaded_user_dto(user_dto)
        user_type_dto = self.__user_type_service.find_by_id(
            (self.main_window.get_loaded_user_dto().get_user_type_id()))
        self.main_window.line_edit_modify_user_name.setText(
            self.main_window.get_loaded_user_dto().get_name())
        self.main_window.line_edit_modify_user_paternal_surname.setText(
            self.main_window.get_loaded_user_dto().get_paternal_surname())
        self.main_window.line_edit_modify_user_maternal_surname.setText(
            self.main_window.get_loaded_user_dto().get_maternal_surname())
        self.main_window.combo_box_modify_user_user_type.setCurrentText(user_type_dto.get_name())

    def __update_user(self):
        try:
            validate_is_not_empty(
                self.main_window.line_edit_modify_user_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_user_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_user_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            user_dto = UserDto()
            user_dto = self.main_window.get_loaded_user_dto()
            user_dto.set_name(self.main_window.line_edit_modify_user_name.text())
            user_dto.set_paternal_surname(
                self.main_window.line_edit_modify_user_paternal_surname.text())
            user_dto.set_maternal_surname(
                self.main_window.line_edit_modify_user_maternal_surname.text())
            user_dto.set_user_type_id(
                self.main_window.combo_box_modify_user_user_type.currentData().get_id())

            self.__user_service.modify_user(user_dto)
            self.main_window.set_loaded_user_dto(user_dto)
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_user.hide()
            logging.debug("El usuario se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__user_service.reactivate_user(self.main_window.get_loaded_user_dto().get_id())
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha activado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_user.hide()
            logging.debug("El usuario se ha activado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__user_service.deactivate_user(self.main_window.get_loaded_user_dto().get_id())
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha desactivado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_user.hide()
            logging.debug("El usuario se ha desactivado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
