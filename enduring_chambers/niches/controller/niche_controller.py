"""
Niche Controller Module
"""
import logging
from PySide6 import QtWidgets, QtCore
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.service.holder_service import HolderService
from niches.service.niche_service import NicheService
from niches.model.dto.module_dto import ModuleDto
from niches.service.row_service import RowService
from niches.model.dto.row_dto import RowDto
from niches.model.dto.holder_dto import HolderDto
from niches.model.dto.niche_dto import NicheDto
from niches.controller.error_controller import ErrorController
from niches.constant.constants import UserTypeKey, HASHED_BOOLEAN_CONVERTER_IS_ACTIVE
from niches.constant.constants import HASHED_BOOLEAN_CONVERTER_IS_PAID_OFF
from niches.constant.constants import HASHED_BOOLEAN_CONVERTER_IS_BUSY
from niches.util.validator import validate_not_none

class NicheController:
    """
    Niche controller class
    
    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__row = 0
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__holder_service = HolderService()
        self.__niche_service = NicheService()
        self.__loaded_niche_dto = NicheDto()
        self.__error_controller = ErrorController()
        self.main_window.scroll_area_modify_niche.hide()
        self.main_window.scroll_area_create_niche.hide()
        self.__configure_combo_box_niches_module()
        self.__configure_combo_box_holders()
        self.__configure_combo_box_holders_modify()
        self.__configure_actions()
        self.__search_niches()

    def __configure_combo_box_niches_module(self):
        list_module_dto:list[ModuleDto] = self.__module_service.find_all_active()
        self.main_window.combo_box_niches_module.clear()
        self.main_window.combo_box_niches_module.addItem("", None)
        for module_dto in list_module_dto:
            self.main_window.combo_box_niches_module.addItem(
                module_dto.get_name(), module_dto)


    def __configure_combo_box_rows(self):
        if self.main_window.combo_box_niches_module.currentData() is None:
            self.main_window.combo_box_niches_row.setEnabled(False)
        else:
            self.main_window.combo_box_niches_row.setEnabled(True)
            self.main_window.combo_box_niches_row.clear()
            self.main_window.combo_box_niches_row.addItem("", None)
            list_row_dto:list[RowDto] = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_niches_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_niches_row.addItem(
                    row_dto.get_name(), row_dto)

    def __configure_combo_box_holders(self):
        self.main_window.combo_box_create_niche_holder.clear()
        self.main_window.combo_box_create_niche_holder.addItem("", None)
        list_holder_dto:list[HolderDto] = self.__holder_service.search_active_holders(
            self.main_window.line_edit_create_niche_holder_search.text())
        x = 1
        for holder_dto in list_holder_dto:
            full_name = ("[" + str(holder_dto.get_id()) + "] " + holder_dto.get_name() + " " +
                         holder_dto.get_paternal_surname() + " " +
                         holder_dto.get_maternal_surname())
            self.main_window.combo_box_create_niche_holder.addItem(full_name, holder_dto)
            self.main_window.combo_box_create_niche_holder.setItemData(x,
                holder_dto.get_phone() + " - " + full_name, QtCore.Qt.ToolTipRole)
            x = x + 1
        if self.main_window.line_edit_create_niche_holder_search.text() == "":
            self.main_window.combo_box_create_niche_holder.setCurrentIndex(0)
        else:
            self.main_window.combo_box_create_niche_holder.setCurrentIndex(1)

    def __configure_combo_box_holders_modify(self):
        self.main_window.combo_box_modify_niche_holder.clear()
        self.main_window.combo_box_modify_niche_holder.addItem("", None)
        list_holder_dto:list[HolderDto] = self.__holder_service.search_active_holders(
            self.main_window.line_edit_modify_niche_search_holder.text())
        x = 1
        for holder_dto in list_holder_dto:
            full_name = ("[" + str(holder_dto.get_id()) + "] " + holder_dto.get_name() + " " +
                         holder_dto.get_paternal_surname() + " " +
                         holder_dto.get_maternal_surname())
            self.main_window.combo_box_modify_niche_holder.addItem(full_name, holder_dto)
            self.main_window.combo_box_modify_niche_holder.setItemData(x,
                holder_dto.get_phone() + " - " + full_name, QtCore.Qt.ToolTipRole)
            x = x + 1
        if self.main_window.line_edit_modify_niche_search_holder.text() == "":
            self.main_window.combo_box_modify_niche_holder.setCurrentIndex(0)
        else:
            self.main_window.combo_box_modify_niche_holder.setCurrentIndex(1)

    def __configure_actions(self):
        self.main_window.combo_box_niches_module.currentIndexChanged.connect(
            self.__configure_combo_box_rows)
        self.main_window.line_edit_create_niche_holder_search.textChanged.connect(
            self.__configure_combo_box_holders)
        self.main_window.push_button_create_niches_create.clicked.connect(
            self.main_window.scroll_area_create_niche.show)
        self.main_window.push_button_create_niche_save_niche.clicked.connect(
            self.__save_niche)
        self.main_window.combo_box_niches_module.currentIndexChanged.connect(
            self.__search_niches)
        self.main_window.combo_box_niches_row.currentIndexChanged.connect(
            self.__search_niches)
        self.main_window.line_edit_search_niches.textChanged.connect(
            self.__search_niches)
        self.main_window.table_widget_niches.cellDoubleClicked.connect(self.__select_niche)
        self.main_window.line_edit_modify_niche_search_holder.textChanged.connect(
            self.__configure_combo_box_holders_modify)
        self.main_window.push_button_modify_niche_save.clicked.connect(self.__update_niche)
        self.main_window.push_button_modify_niche_activate.clicked.connect(self.__activate)
        self.main_window.push_button_modify_niche_deactivate.clicked.connect(self.__deactivate)
        self.main_window.push_button_create_niche_clean.clicked.connect(
            self.__clean_stacked_widget_niches)
        self.main_window.push_button_niches.clicked.connect(self.__reload)

    def __reload(self):
        self.__configure_combo_box_holders()
        self.__configure_combo_box_holders_modify()
        self.__configure_combo_box_niches_module()
        self.__configure_combo_box_rows()

    def __save_niche(self):
        niche_dto = NicheDto()
        try:
            validate_not_none(self.main_window.combo_box_niches_module.currentData(), "Modulo")
            validate_not_none(self.main_window.combo_box_niches_row.currentData(), "Fila")
            if self.main_window.combo_box_create_niche_holder.currentData() is None:
                holder_dto:HolderDto = None
            else:
                holder_dto:HolderDto = self.main_window.combo_box_create_niche_holder.currentData()
            niche_dto.new_niche(
                self.main_window.combo_box_niches_row.currentData(),
                self.main_window.spin_box_create_niche_number.value(),
                self.main_window.check_box_create_niche_is_busy.isChecked(),
                self.main_window.check_box_create_niche_is_paid_off.isChecked(),
                holder_dto
            )
            self.__niche_service.create_niche(niche_dto)
            self.__clean_stacked_widget_niches()
            self.main_window.scroll_area_create_niche.hide()
            self.__search_niches()
            self.__error_controller.handle_value_error("El nicho se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("Niche created [%s]", niche_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __configure_table(self):
        self.main_window.table_widget_niches.clear()
        self.main_window.table_widget_niches.setRowCount(self.__row)
        self.main_window.table_widget_niches.setColumnCount(10)
        self.main_window.table_widget_niches.setHorizontalHeaderLabels(("id",
                                                                        "Modulo",
                                                                        "Fila",
                                                                        "Número",
                                                                        "Titular",
                                                                        "Ocupado",
                                                                        "Pagado",
                                                                        "Activo",
                                                                        "Creado",
                                                                        "Actualizado"))
        self.main_window.table_widget_niches.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_niches.resizeColumnsToContents()

    def __search_niches(self):
        if self.main_window.combo_box_niches_row.currentData() is None:
            row_id = 0
        else:
            row_id = self.main_window.combo_box_niches_row.currentData().get_id()

        if self.main_window.get_logged_user_type_key() == UserTypeKey.ADMINISTRATOR.value:
            if self.main_window.combo_box_niches_module.currentData() is None:
                list_niche_dto = self.__niche_service.search_niches(
                    self.main_window.line_edit_search_niches.text())
            else:
                if self.main_window.combo_box_niches_row.currentData() is None:
                    list_niche_dto = self.__niche_service.search_niches_by_module_id(
                        self.main_window.line_edit_search_niches.text(),
                        self.main_window.combo_box_niches_module.currentData().get_id())
                else:
                    list_niche_dto = self.__niche_service.search_niches_by_module_id_and_row_id(
                        self.main_window.line_edit_search_niches.text(),
                        self.main_window.combo_box_niches_module.currentData().get_id(),
                        row_id)
                    self.main_window.spin_box_create_niche_number.setValue(len(
                        self.__niche_service.search_niches_by_module_id_and_row_id(
                            "",
                            self.main_window.combo_box_niches_module.currentData().get_id(),
                            self.main_window.combo_box_niches_row.currentData().get_id())) + 1)

        else:
            if self.main_window.combo_box_niches_module.currentData() is None:
                list_niche_dto = self.__niche_service.search_niches(
                    self.main_window.line_edit_search_niches.text())
            else:
                if self.main_window.combo_box_niches_row.currentData() is None:
                    list_niche_dto = self.__niche_service.search_niches_by_module_id(
                        self.main_window.line_edit_search_niches.text(),
                        self.main_window.combo_box_niches_module.currentData().get_id())
                else:
                    list_niche_dto = self.__niche_service.search_niches_by_module_id_and_row_id(
                        self.main_window.line_edit_search_niches.text(),
                        self.main_window.combo_box_niches_module.currentData().get_id(),
                        row_id)
                    self.main_window.spin_box_create_niche_number.setValue(len(
                        self.__niche_service.search_niches_by_module_id_and_row_id(
                            "",
                            self.main_window.combo_box_niches_module.currentData().get_id(),
                            self.main_window.combo_box_niches_row.currentData().get_id())) + 1)

        self.__row = len(list_niche_dto)
        self.__configure_table()
        row = 0

        for niche_dto in list_niche_dto:
            if niche_dto.get_holder() is None:
                holder_name = "Sin titular"
            else:
                holder_name = (niche_dto.get_holder().get_name() + " " +
                               niche_dto.get_holder().get_paternal_surname() + " " +
                               niche_dto.get_holder().get_maternal_surname())

            self.main_window.table_widget_niches.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(niche_dto.get_id())))
            self.main_window.table_widget_niches.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                niche_dto.get_row().get_module().get_name()))
            self.main_window.table_widget_niches.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                    niche_dto.get_row().get_name()))
            self.main_window.table_widget_niches.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                    str(niche_dto.get_number())))
            self.main_window.table_widget_niches.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                    holder_name))
            self.main_window.table_widget_niches.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                    HASHED_BOOLEAN_CONVERTER_IS_BUSY[str(niche_dto.is_busy())]))
            self.main_window.table_widget_niches.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                    HASHED_BOOLEAN_CONVERTER_IS_PAID_OFF[str(niche_dto.is_paid_off())]))
            self.main_window.table_widget_niches.setItem(
                row,
                7,
                QtWidgets.QTableWidgetItem(
                    HASHED_BOOLEAN_CONVERTER_IS_ACTIVE[str(niche_dto.is_active())]))
            self.main_window.table_widget_niches.setItem(
                row,
                8,
                QtWidgets.QTableWidgetItem(
                    str(niche_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_niches.setItem(
                row,
                9,
                QtWidgets.QTableWidgetItem(
                    str(niche_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_niches.resizeColumnsToContents()
            row = row + 1

    def __select_niche(self):
        row = self.main_window.table_widget_niches.currentRow()
        niche_id = int(self.main_window.table_widget_niches.item(row, 0).text())
        self.main_window.scroll_area_modify_niche.show()
        self.__load_niche(niche_id)

    def __load_niche(self, niche_id:int):
        niche_dto = self.__niche_service.find_by_id(niche_id)
        self.__loaded_niche_dto = niche_dto
        if self.__loaded_niche_dto.get_holder() is None:
            holder_name = ""
        else:
            holder_name = ("[" + str(self.__loaded_niche_dto.get_holder().get_id()) + "] " +
                           self.__loaded_niche_dto.get_holder().get_name() + " " +
                           self.__loaded_niche_dto.get_holder().get_paternal_surname() + " " +
                           self.__loaded_niche_dto.get_holder().get_maternal_surname())
        self.main_window.check_box_modify_niche_is_busy.setChecked(
            self.__loaded_niche_dto.is_busy())
        self.main_window.check_box_modify_niche_paid_off.setChecked(
            self.__loaded_niche_dto.is_paid_off())
        self.main_window.combo_box_modify_niche_holder.setCurrentText(holder_name)
        self.main_window.label_modify_niche_name.setText(
            self.__loaded_niche_dto.get_row().get_module().get_name() + "-" +
            self.__loaded_niche_dto.get_row().get_name() + "-" +
            str(self.__loaded_niche_dto.get_number()))

    def __update_niche(self):
        try:
            if self.main_window.combo_box_modify_niche_holder.currentData() is None:
                holder_dto = None
            else:
                holder_dto = self.main_window.combo_box_modify_niche_holder.currentData()

            self.__loaded_niche_dto.set_holder(holder_dto)
            self.__loaded_niche_dto.set_is_busy(
                self.main_window.check_box_modify_niche_is_busy.isChecked())
            self.__loaded_niche_dto.set_is_paid_off(
                self.main_window.check_box_modify_niche_paid_off.isChecked())
            self.__niche_service.modify_niche(self.__loaded_niche_dto)
            self.__search_niches()
            self.__error_controller.handle_value_error("El nicho se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_niche.hide()
            logging.debug("El nicho se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __activate(self):
        try:
            self.__niche_service.reactivate_niche(self.__loaded_niche_dto.get_id())
            self.__search_niches()
            self.__error_controller.handle_value_error("El nicho se ha activado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_niche.hide()
            logging.debug("El niche se ha activado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__niche_service.deactivate_niche(self.__loaded_niche_dto.get_id())
            self.__search_niches()
            self.__error_controller.handle_value_error("El nicho se ha desactivado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_niche.hide()
            logging.debug("El nicho se ha desactivado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __clean_stacked_widget_niches(self):
        self.main_window.combo_box_modify_niche_holder.setCurrentIndex(0)
        self.main_window.check_box_create_niche_is_busy.setChecked(False)
        self.main_window.check_box_create_niche_is_paid_off.setChecked(False)
        self.main_window.line_edit_create_niche_holder_search.clear()
