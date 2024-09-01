"""
Row Controller Module
"""
import logging
from PySide6 import QtWidgets
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.service.row_service import RowService
from niches.model.dto.module_dto import ModuleDto
from niches.model.dto.row_dto import RowDto
from niches.constant.constants import HASHED_BOOLEAN_CONVERTER_IS_ACTIVE, FieldName
from niches.util.validator import validate_is_not_empty, validate_not_none
from niches.controller.error_controller import ErrorController

class RowController:
    """
    My Account controller class
    
    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__row = 0
        self.__loaded_row_dto = RowDto()
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__error_controller = ErrorController()
        self.__configure_combo_box_module()
        self.__configure_table()
        self.__search_row()
        self.__configure_actions()
        logging.debug("Row controller initializes")

    def __configure_combo_box_module(self):
        list_module_dto:list[ModuleDto] = self.__module_service.find_all_active()
        self.main_window.combo_box_row_module.clear()
        self.main_window.combo_box_row_module.addItem("", None)
        for module_dto in list_module_dto:
            self.main_window.combo_box_row_module.addItem(
                module_dto.get_name(), module_dto)
        logging.debug("Combo box module configured")

    def  __configure_actions(self):
        self.main_window.combo_box_row_module.currentIndexChanged.connect(self.__search_row)
        self.main_window.push_button_row_create.clicked.connect(
            self.main_window.scroll_area_create_row.show)
        self.main_window.push_button_create_row_save.clicked.connect(self.__create_row)
        self.main_window.push_button_modify_row_save.clicked.connect(self.__modify_row)
        self.main_window.table_widget_rows_search.cellDoubleClicked.connect(self.__select_row)
        self.main_window.push_button_rows.clicked.connect(self.__configure_combo_box_module)
        logging.debug("Row controller actions configured")

    def __configure_table(self):
        self.main_window.table_widget_rows_search.clear()
        self.main_window.table_widget_rows_search.setRowCount(self.__row)
        self.main_window.table_widget_rows_search.setColumnCount(4)
        self.main_window.table_widget_rows_search.setHorizontalHeaderLabels(("id",
                                                           "Nombre",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_rows_search.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_rows_search.horizontalHeader().setMaximumSectionSize(500)
        self.main_window.table_widget_rows_search.resizeRowsToContents()
        self.main_window.table_widget_rows_search.resizeColumnsToContents()
        logging.debug("Table rows configured")

    def __search_row(self):
        list_row_dto = []
        if self.main_window.combo_box_row_module.currentData() is None:
            list_row_dto = []
        else:
            list_row_dto = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_row_module.currentData().get_id())
        self.__row = len(list_row_dto)
        self.__configure_table()
        row = 0

        for row_dto in list_row_dto:
            self.main_window.table_widget_rows_search.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(row_dto.get_id())))
            self.main_window.table_widget_rows_search.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                    row_dto.get_name()))
            self.main_window.table_widget_rows_search.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                    str(row_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_rows_search.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                    str(row_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_rows_search.resizeColumnsToContents()
            self.main_window.table_widget_rows_search.resizeRowsToContents()
            row = row + 1
        logging.debug("Rows searched [%s]", list_row_dto)

    def __create_row(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_create_row_name.text(),
                                  FieldName.NAME)
            validate_not_none(self.main_window.combo_box_row_module.currentData(),
                              FieldName.MODULE)
            row_dto = RowDto()
            row_dto.new_row(
                self.main_window.line_edit_create_row_name.text(),
                self.main_window.combo_box_row_module.currentData()
            )

            self.__row_service.create_row(row_dto)
            self.main_window.line_edit_create_row_name.clear()
            self.main_window.scroll_area_create_row.hide()
            self.__search_row()
            self.__error_controller.handle_value_error("La fila se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("Fila creado [%s]", row_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __modify_row(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_modify_row_name.text(),
                                  FieldName.NAME)

            self.__loaded_row_dto.set_name(
                self.main_window.line_edit_modify_row_name.text())
            self.__row_service.modify_row(self.__loaded_row_dto)
            self.__search_row()
            self.main_window.line_edit_modify_row_name.clear()
            self.__error_controller.handle_value_error("La fila se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_row.hide()
            logging.debug("La fila se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __select_row(self):
        row = self.main_window.table_widget_rows_search.currentRow()
        row_id = int(self.main_window.table_widget_rows_search.item(row, 0).text())
        self.main_window.scroll_area_modify_row.show()
        self.__load_row(row_id)
        logging.debug("Row selected [%s]", row_id)

    def __load_row(self, row_id:int):
        row_dto = self.__row_service.find_by_id(row_id)
        self.__loaded_row_dto.existing_row(
            row_dto.get_id(),
            row_dto.get_name(),
            row_dto.get_module(),
            row_dto.get_created_at(),
            row_dto.get_updated_at()
        )
        self.main_window.line_edit_modify_row_name.setText(self.__loaded_row_dto.get_name())
        logging.debug("Row loaded [%s]", row_id)

    def __modify_row(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_modify_row_name.text(),
                                  FieldName.NAME)

            self.__loaded_row_dto.set_name(
                self.main_window.line_edit_modify_row_name.text())
            self.__row_service.modify_row(self.__loaded_row_dto)
            self.__search_row()
            self.main_window.line_edit_modify_row_name.clear()
            self.__error_controller.handle_value_error("La fila se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_row.hide()
            logging.debug("La fila se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()
