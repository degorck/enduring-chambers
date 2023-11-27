"""
Module that controls the MainWindow
"""
import sys
from PySide6 import QtWidgets
from niches.view.ui.main_window import Ui_MainWindow
from niches.model.dto.UserDto import UserDto
from niches.constants.constants import UserField
from niches.controller.error_controller import ErrorController
from niches.service.user_service import UserService
from niches.service.user_type_service import UserTypeService
from niches.util.validator import validate_is_not_empty, validate_password
from niches.util.LoggingConfiguration import get_loging
from niches.constants.constants import HASHED_BOOLEAN_CONVERTER
logging = get_loging()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Class with the functionality of MainWindow

    Args:
        QtWidgets (QtWidgets.QMainWindow): Core QMainWindow
        Ui_MainWindow (Ui_MainWindow): Qt layer transformed to python code 
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__dependency_injection()
        self.scroll_area_create_user.hide()
        self.scroll_area_modify_user.hide()
        self.__row = 0
        self.__configure_combo_box()
        self.__configure_actions()
        self.__configure_table()
        logging.debug("System started")

    def __dependency_injection(self):
        self.__user_service = UserService()
        self.__user_type_service = UserTypeService()
        self.__loaded_user_dto = UserDto()
        self.__error_controller = ErrorController()

    def __configure_actions(self):
        self.push_button_create_user_create.clicked.connect(self.scroll_area_create_user.show)
        self.push_button_create_user_save_user.clicked.connect(self.__save_user)
        self.push_button_create_user_clean_user.clicked.connect(self.__clean_stacked_widget_users)
        self.push_button_users.clicked.connect(self.__set_stacked_widget_users)
        self.push_button_niches.clicked.connect(self.__set_stacked_widget_niches)
        self.push_button_deceased.clicked.connect(self.__set_stacked_widget_deceased)
        self.push_button_holders.clicked.connect(self.__set_stacked_widget_holders)
        self.push_button_my_account.clicked.connect(self.__set_stacked_widget_my_account)
        self.push_button_modify_user_save.clicked.connect(self.__update_user)
        self.push_button_modify_user_activate.clicked.connect(self.__activate)
        self.push_button_modify_user_deactivate.clicked.connect(self.__deactivate)
        self.line_edit_search_users.textChanged.connect(self.__search_users)
        self.table_widget_users.cellDoubleClicked.connect(self.__select_user)

    def __configure_combo_box(self):
        self.__list_user_type_dto = self.__user_type_service.find_all()
        self.__hash_list_user_type = {}
        for user_type_dto in self.__list_user_type_dto:
            self.combo_box_create_user_user_type.addItem(user_type_dto.get_name(), user_type_dto)
            self.combo_box_modify_user_user_type.addItem(user_type_dto.get_name(), user_type_dto)
            self.__hash_list_user_type[user_type_dto.get_id()] = user_type_dto.get_name()

    def __save_user(self):
        user_dto = UserDto()
        try:
            validate_is_not_empty(
                self.line_edit_create_user_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.line_edit_create_user_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.line_edit_create_user_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            validate_is_not_empty(
                self.line_edit_create_user_user_name.text(),
                UserField.USER_NAME)
            validate_is_not_empty(
                self.line_edit_create_user_password.text(),
                UserField.PASSWORD)
            validate_is_not_empty(
                self.line_edit_create_user_repeat_password.text(),
                UserField.PASSWORD)
            validate_password(self.line_edit_create_user_password.text(),
                                               self.line_edit_create_user_repeat_password.text())

            user_dto.new_user(
                self.line_edit_create_user_name.text(),
                self.line_edit_create_user_paternal_surname.text(),
                self.line_edit_create_user_maternal_surname.text(),
                int(self.combo_box_create_user_user_type.currentData().get_id()),
                self.line_edit_create_user_user_name.text(),
                self.line_edit_create_user_password.text()
            )

            self.__user_service.create_user(user_dto)
            self.__clean_stacked_widget_users()
            self.scroll_area_create_user.hide()
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha creado exitosamente")
            self.__error_controller.show()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
        logging.debug("User created")

    def __clean_stacked_widget_users(self):
        self.line_edit_create_user_name.clear()
        self.line_edit_create_user_paternal_surname.clear()
        self.line_edit_create_user_maternal_surname.clear()
        self.line_edit_create_user_user_name.clear()
        self.line_edit_create_user_password.clear()
        self.line_edit_create_user_repeat_password.clear()

    def __set_stacked_widget_users(self):
        self.scroll_area_create_user.hide()
        self.scroll_area_modify_user.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(True)
        self.stacked_widget.setCurrentIndex(1)
        logging.debug("Users stacked widget selected")

    def __set_stacked_widget_niches(self):
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.stacked_widget.setCurrentIndex(4)
        logging.debug("Nichess stacked widget selected")

    def __set_stacked_widget_deceased(self):
        self.push_button_deceased.setChecked(True)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.stacked_widget.setCurrentIndex(2)
        logging.debug("Deceased stacked widget selected")

    def __set_stacked_widget_holders(self):
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(True)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.stacked_widget.setCurrentIndex(3)
        logging.debug("Holders stacked widget selected")

    def __set_stacked_widget_my_account(self):
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(True)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.stacked_widget.setCurrentIndex(5)
        logging.debug("My account stacked widget selected")

    def __configure_table(self):
        self.table_widget_users.clear()
        self.table_widget_users.setRowCount(self.__row)
        self.table_widget_users.setColumnCount(8)
        self.table_widget_users.setHorizontalHeaderLabels(("Nombre de Usuario",
                                                           "Nombre",
                                                           "Apellido Paterno",
                                                           "Apellido Materno",
                                                           "Tipo de usuario",
                                                           "Activo",
                                                           "Creado",
                                                           "Actualizado"))
        self.table_widget_users.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget_users.resizeColumnsToContents()

    def __search_users(self):
        list_user_dto = self.__user_service.search_users(self.line_edit_search_users.text())
        self.__row = len(list_user_dto)
        self.__configure_table()
        row = 0

        for user_dto in list_user_dto:
            self.table_widget_users.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(user_dto.get_user_name())))
            self.table_widget_users.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                user_dto.get_name()))
            self.table_widget_users.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                user_dto.get_paternal_surname()))
            self.table_widget_users.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                user_dto.get_maternal_surname()))
            self.table_widget_users.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                    self.__hash_list_user_type[user_dto.get_user_type_id()]))
            self.table_widget_users.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                HASHED_BOOLEAN_CONVERTER[str(user_dto.is_active())]))
            self.table_widget_users.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                    str(user_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.table_widget_users.setItem(
                row,
                7,
                QtWidgets.QTableWidgetItem(
                    str(user_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            row = row + 1

    def __select_user(self):
        row = self.table_widget_users.currentRow()
        user_name = self.table_widget_users.item(row, 0).text()
        self.scroll_area_modify_user.show()
        self.__load_user(user_name)

    def __load_user(self, user_name:str):
        self.__loaded_user_dto = self.__user_service.find_user_by_user_name(user_name)
        user_type_dto = self.__user_type_service.find_by_id(
            (self.__loaded_user_dto.get_user_type_id()))
        self.line_edit_modify_user_name.setText(self.__loaded_user_dto.get_name())
        self.line_edit_modify_user_paternal_surname.setText(
            self.__loaded_user_dto.get_paternal_surname())
        self.line_edit_modify_user_maternal_surname.setText(
            self.__loaded_user_dto.get_maternal_surname())
        self.combo_box_modify_user_user_type.setCurrentText(user_type_dto.get_name())

    def __update_user(self):
        try:
            validate_is_not_empty(
                self.line_edit_modify_user_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.line_edit_modify_user_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.line_edit_modify_user_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            self.__loaded_user_dto.set_name(self.line_edit_modify_user_name.text())
            self.__loaded_user_dto.set_paternal_surname(
                self.line_edit_modify_user_paternal_surname.text())
            self.__loaded_user_dto.set_maternal_surname(
                self.line_edit_modify_user_maternal_surname.text())
            self.__loaded_user_dto.set_user_type_id(
                self.combo_box_modify_user_user_type.currentData().get_id())
            print(self.__loaded_user_dto)

            self.__user_service.modify_user(self.__loaded_user_dto)
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha modificado exitosamente")
            self.__error_controller.show()
            self.scroll_area_modify_user.hide()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__user_service.reactivate_user(self.__loaded_user_dto.get_id())
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha activado")
            self.__error_controller.show()
            self.scroll_area_modify_user.hide()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__user_service.deactivate_user(self.__loaded_user_dto.get_id())
            self.__search_users()
            self.__error_controller.handle_value_error("El usuario se ha desactivado")
            self.__error_controller.show()
            self.scroll_area_modify_user.hide()

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
