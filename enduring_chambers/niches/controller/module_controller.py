"""
Module Controller Module
"""
import logging
from PySide6 import QtWidgets
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.model.dto.module_dto import ModuleDto
from niches.constant.constants import HASHED_BOOLEAN_CONVERTER_IS_ACTIVE, UserField
from niches.util.validator import validate_is_not_empty
from niches.controller.error_controller import ErrorController

class ModuleController:
    """
    My Account controller class
    
    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.__row = 0
        self.__loaded_module_dto = ModuleDto()
        self.main_window = main_window
        self.__module_service = ModuleService()
        self.__error_controller = ErrorController()
        self.__configure_table()
        self.__search_module()
        self.__configure_actions()

    def  __configure_actions(self):
        self.main_window.table_widget_modules.cellDoubleClicked.connect(self.__select_module)
        self.main_window.push_button_module_create.clicked.connect(
            self.main_window.scroll_area_create_module.show)
        self.main_window.push_button_create_module_save.clicked.connect(self.__create_module)
        self.main_window.push_button_modify_module_save.clicked.connect(self.__modify_module)
        self.main_window.push_button_modify_module_activate.clicked.connect(
            self.__activate)
        self.main_window.push_button_modify_module_deactivate.clicked.connect(
            self.__deactivate)

    def __configure_table(self):
        self.main_window.table_widget_modules.clear()
        self.main_window.table_widget_modules.setRowCount(self.__row)
        self.main_window.table_widget_modules.setColumnCount(5)
        self.main_window.table_widget_modules.setHorizontalHeaderLabels(("id",
                                                           "Nombre",
                                                           "Activo",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_modules.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_modules.horizontalHeader().setMaximumSectionSize(500)
        self.main_window.table_widget_modules.resizeRowsToContents()
        self.main_window.table_widget_modules.resizeColumnsToContents()

    def __search_module(self):
        list_module_dto = []
        list_module_dto = self.__module_service.find_all()
        self.__row = len(list_module_dto)
        self.__configure_table()
        row = 0

        for module_dto in list_module_dto:
            self.main_window.table_widget_modules.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(module_dto.get_id())))
            self.main_window.table_widget_modules.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                module_dto.get_name()))
            self.main_window.table_widget_modules.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                    HASHED_BOOLEAN_CONVERTER_IS_ACTIVE[str(module_dto.is_active())]))
            self.main_window.table_widget_modules.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                    str(module_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_modules.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                    str(module_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_modules.resizeColumnsToContents()
            self.main_window.table_widget_modules.resizeRowsToContents()
            row = row + 1

    def __select_module(self):
        row = self.main_window.table_widget_modules.currentRow()
        module_id = int(self.main_window.table_widget_modules.item(row, 0).text())
        self.main_window.scroll_area_modify_module.show()
        self.__load_module(module_id)

    def __load_module(self, module_id:int):
        module_dto = self.__module_service.find_by_id(module_id)
        self.__loaded_module_dto.existing_module(
            module_dto.get_id(),
            module_dto.get_name(),
            module_dto.is_active(),
            module_dto.get_created_at(),
            module_dto.get_updated_at()
        )
        self.main_window.line_edit_modify_module_name.setText(self.__loaded_module_dto.get_name())

    def __create_module(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_create_module_name.text(),
                                  UserField.NAME)
            module_dto = ModuleDto()
            module_dto.new_module(
                self.main_window.line_edit_create_module_name.text()
            )

            self.__module_service.create_module(module_dto)
            self.main_window.line_edit_create_module_name.clear()
            self.main_window.scroll_area_create_module.hide()
            self.__search_module()
            self.__error_controller.handle_value_error("El módulo se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("Módulo creado [%s]", module_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __modify_module(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_modify_module_name.text(),
                                  UserField.NAME)

            self.__loaded_module_dto.set_name(
                self.main_window.line_edit_modify_module_name.text())
            self.__module_service.modify_module(self.__loaded_module_dto)
            self.__search_module()
            self.main_window.line_edit_modify_module_name.clear()
            self.__error_controller.handle_value_error("El módulo se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_module.hide()
            logging.debug("El módulo se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__module_service.reactivate_module(self.__loaded_module_dto.get_id())
            self.__search_module()
            self.__error_controller.handle_value_error("El módulo se ha activado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_module.hide()
            logging.debug("El módulo se ha activado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__module_service.deactivate_module(self.__loaded_module_dto.get_id())
            self.__search_module()
            self.__error_controller.handle_value_error("El módulo se ha desactivado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_module.hide()
            logging.debug("El módulo se ha desactivado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()
