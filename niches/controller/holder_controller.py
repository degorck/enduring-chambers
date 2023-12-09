"""
Holder Controller Module
"""
import logging
from PySide6 import QtWidgets
from niches.view.ui.main_window import Ui_MainWindow
from niches.util.validator import validate_is_not_empty, validate_phone_number
from niches.constants.constants import UserField, UserTypeKey, HASHED_BOOLEAN_CONVERTER_IS_ACTIVE
from niches.model.dto.holder_dto import HolderDto
from niches.service.holder_service import HolderService
from niches.controller.error_controller import ErrorController

class HolderController:
    """
    Holder controller class
    Args:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__holder_service = HolderService()
        self.__error_controller = ErrorController()
        self.__row = 0
        self.__loaded_holder_dto = HolderDto()
        self.__search_holders()
        self.__configure_actions()

    def __configure_actions(self):
        self.main_window.push_button_create_holder_create.clicked.connect(
            self.main_window.scroll_area_create_holder.show)
        self.main_window.push_button_create_holder_save_holder.clicked.connect(self.__save_holder)
        self.main_window.line_edit_search_holders.textChanged.connect(self.__search_holders)
        self.main_window.push_button_create_holder_clean_holder.clicked.connect(
            self.__clean_stacked_widget_holders)
        self.main_window.push_button_modify_holder_save.clicked.connect(self.__update_holder)
        self.main_window.push_button_modify_holder_activate.clicked.connect(self.__activate)
        self.main_window.push_button_modify_holder_deactivate.clicked.connect(self.__deactivate)
        self.main_window.table_widget_holders.cellDoubleClicked.connect(self.__select_holder)

    def __save_holder(self):
        holder_dto = HolderDto()
        try:
            validate_is_not_empty(
                self.main_window.line_edit_create_holder_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_holder_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_holder_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_holder_phone.text(),
                UserField.PHONE)
            validate_phone_number(self.main_window.line_edit_create_holder_phone.text())

            holder_dto.new_holder(
                self.main_window.line_edit_create_holder_name.text(),
                self.main_window.line_edit_create_holder_paternal_surname.text(),
                self.main_window.line_edit_create_holder_maternal_surname.text(),
                self.main_window.line_edit_create_holder_phone.text()
            )
            logging.info(holder_dto.to_string())

            self.__holder_service.create_holder(holder_dto)
            self.__clean_stacked_widget_holders()
            self.main_window.scroll_area_create_holder.hide()
            self.__search_holders()
            self.__error_controller.handle_value_error("El titular se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("Holder created")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __clean_stacked_widget_holders(self):
        self.main_window.line_edit_create_holder_name.clear()
        self.main_window.line_edit_create_holder_paternal_surname.clear()
        self.main_window.line_edit_create_holder_maternal_surname.clear()
        self.main_window.line_edit_create_holder_phone.clear()

    def __configure_table(self):
        self.main_window.table_widget_holders.clear()
        self.main_window.table_widget_holders.setRowCount(self.__row)
        self.main_window.table_widget_holders.setColumnCount(8)
        self.main_window.table_widget_holders.setHorizontalHeaderLabels(("id",
                                                           "Nombre",
                                                           "Apellido Paterno",
                                                           "Apellido Materno",
                                                           "Teléfono",
                                                           "Activo",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_holders.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_holders.resizeColumnsToContents()

    def __search_holders(self):
        if self.main_window.get_logged_user_type_key() == UserTypeKey.ADMINISTRATOR.value:
            list_holder_dto:list[HolderDto] = self.__holder_service.search_holders(
                self.main_window.line_edit_search_holders.text())
        else:
            list_holder_dto:list[HolderDto] = self.__holder_service.search_active_holders(
                self.main_window.line_edit_search_holders.text())
        self.__row = len(list_holder_dto)
        self.__configure_table()
        row = 0

        for holder_dto in list_holder_dto:
            self.main_window.table_widget_holders.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(holder_dto.get_id())))
            self.main_window.table_widget_holders.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                holder_dto.get_name()))
            self.main_window.table_widget_holders.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                holder_dto.get_paternal_surname()))
            self.main_window.table_widget_holders.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                holder_dto.get_maternal_surname()))
            self.main_window.table_widget_holders.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                holder_dto.get_phone()))
            self.main_window.table_widget_holders.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                HASHED_BOOLEAN_CONVERTER_IS_ACTIVE[str(holder_dto.is_active())]))
            self.main_window.table_widget_holders.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                str(holder_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_holders.setItem(
                row,
                7,
                QtWidgets.QTableWidgetItem(
                str(holder_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_holders.resizeColumnsToContents()
            row = row + 1

    def __select_holder(self):
        row = self.main_window.table_widget_holders.currentRow()
        holder_id = int(self.main_window.table_widget_holders.item(row, 0).text())
        self.main_window.scroll_area_modify_holder.show()
        self.__load_holder(holder_id)

    def __load_holder(self, holder_id:int):
        holder_dto = self.__holder_service.find_by_id(holder_id)
        self.__loaded_holder_dto.existing_holder(
            holder_dto.get_id(),
            holder_dto.get_name(),
            holder_dto.get_paternal_surname(),
            holder_dto.get_maternal_surname(),
            holder_dto.get_phone(),
            holder_dto.is_active(),
            holder_dto.get_created_at(),
            holder_dto.get_updated_at()
        )
        self.main_window.line_edit_modify_holder_name.setText(
            holder_dto.get_name())
        self.main_window.line_edit_modify_holder_paternal_surname.setText(
            holder_dto.get_paternal_surname())
        self.main_window.line_edit_modify_holder_maternal_surname.setText(
            holder_dto.get_maternal_surname())
        self.main_window.line_edit_modify_holder_phone.setText(holder_dto.get_phone())

    def __update_holder(self):
        try:
            validate_is_not_empty(
                self.main_window.line_edit_modify_holder_name.text(),
                UserField.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_holder_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_holder_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_holder_phone.text(),
                UserField.PHONE)
            holder_dto = HolderDto()
            holder_dto = self.__loaded_holder_dto
            holder_dto.set_name(self.main_window.line_edit_modify_holder_name.text())
            holder_dto.set_paternal_surname(
                self.main_window.line_edit_modify_holder_paternal_surname.text())
            holder_dto.set_maternal_surname(
                self.main_window.line_edit_modify_holder_maternal_surname.text())
            holder_dto.set_phone(
                self.main_window.line_edit_modify_holder_phone.text())

            self.__holder_service.modify_holder(holder_dto)
            self.__loaded_holder_dto.existing_holder(
                holder_dto.get_id(),
                holder_dto.get_name(),
                holder_dto.get_paternal_surname(),
                holder_dto.get_maternal_surname(),
                holder_dto.get_phone(),
                holder_dto.is_active(),
                holder_dto.get_created_at(),
                holder_dto.get_updated_at()
            )
            self.__search_holders()
            self.__error_controller.handle_value_error("El usuario se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_holder.hide()
            logging.debug("El titular se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__holder_service.reactivate_holder(self.__loaded_holder_dto.get_id())
            self.__search_holders()
            self.__error_controller.handle_value_error("El titular se ha activado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_holder.hide()
            logging.debug("El titular se ha activado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__holder_service.deactivate_holder(self.__loaded_holder_dto.get_id())
            self.__search_holders()
            self.__error_controller.handle_value_error("El titular se ha desactivado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_holder.hide()
            logging.debug("El titular se ha desactivado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
