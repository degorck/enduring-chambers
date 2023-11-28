"""
Holder Controller Module
"""
import logging
from niches.view.ui.main_window import Ui_MainWindow
from niches.util.validator import validate_is_not_empty, UserField
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
        self.__configure_actions()

    def __configure_actions(self):
        self.main_window.push_button_create_holder_create.clicked.connect(
            self.main_window.scroll_area_create_holder.show)
        self.main_window.push_button_create_holder_save_holder.clicked.connect(self.__save_holder)

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

            holder_dto.new_holder(
                self.main_window.line_edit_create_holder_name.text(),
                self.main_window.line_edit_create_holder_paternal_surname.text(),
                self.main_window.line_edit_create_holder_maternal_surname.text(),
                self.main_window.line_edit_create_holder_phone.text()
            )

            self.__holder_service.create_holder(holder_dto)
            self.__clean_stacked_widget_holders()
            self.main_window.scroll_area_create_holder.hide()
            #self.__search_users()
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
