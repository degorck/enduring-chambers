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
        self.__error_controller = ErrorController()
        self.__configure_combo_box_niches()
        self.__configure_combo_box_holders()
        self.__configure_actions()

    def __configure_combo_box_niches(self):
        list_module_dto:list[ModuleDto] = self.__module_service.find_all()
        self.main_window.combo_box_niches_module.addItem("", None)
        for module_dto in list_module_dto:
            self.main_window.combo_box_niches_module.addItem(
                module_dto.get_name(), module_dto)


    def __configure_combo_box_rows(self):
        if self.main_window.combo_box_niches_module.currentData() is None:
            self.main_window.combo_box_niches_row.setEnabled(False)
            self.main_window.combo_box_create_niche_row.setEnabled(False)
        else:
            self.main_window.combo_box_niches_row.setEnabled(True)
            self.main_window.combo_box_niches_row.clear()
            self.main_window.combo_box_create_niche_row.setEnabled(True)
            self.main_window.combo_box_create_niche_row.clear()
            list_row_dto:list[RowDto] = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_niches_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_niches_row.addItem(
                    row_dto.get_name(), row_dto)
                self.main_window.combo_box_create_niche_row.addItem(
                    row_dto.get_name(), row_dto)

    def __configure_combo_box_holders(self):
        self.main_window.combo_box_create_niche_holder.clear()
        self.main_window.combo_box_create_niche_holder.addItem("", None)
        list_holder_dto:list[HolderDto] = self.__holder_service.search_active_holders(
            self.main_window.line_edit_create_niche_holder_search.text())
        x = 0
        for holder_dto in list_holder_dto:
            full_name = (holder_dto.get_name() + " " +
                         holder_dto.get_paternal_surname() + " " +
                         holder_dto.get_maternal_surname())
            self.main_window.combo_box_create_niche_holder.addItem(full_name, holder_dto)
            self.main_window.combo_box_create_niche_holder.setItemData(x,
                holder_dto.get_phone() + " - " + full_name, QtCore.Qt.ToolTipRole)
            x = x + 1

    def __configure_actions(self):
        self.main_window.combo_box_niches_module.currentIndexChanged.connect(
            self.__configure_combo_box_rows)
        self.main_window.line_edit_create_niche_holder_search.textChanged.connect(
            self.__configure_combo_box_holders)
        self.main_window.push_button_create_niches_create.clicked.connect(
            self.main_window.scroll_area_create_niche.show)
        self.main_window.push_button_create_niche_save_niche.clicked.connect(
            self.__save_niche)

    def __save_niche(self):
        niche_dto = NicheDto()
        print("Save niche")
        try:
            if self.main_window.combo_box_create_niche_holder.currentData() is None:
                holder_dto:HolderDto = None
            else:
                holder_dto:HolderDto = self.main_window.combo_box_create_niche_holder.currentData()
            niche_dto.new_niche(
                self.main_window.combo_box_create_niche_row.currentData(),
                self.main_window.spin_box_create_niche_number.value(),
                self.main_window.check_box_create_niche_is_busy.isChecked(),
                self.main_window.check_box_create_niche_is_paid_off.isChecked(),
                holder_dto
            )
            self.__niche_service.create_niche(niche_dto)
            #self.__clean_stacked_widget_users()
            #self.main_window.scroll_area_create_user.hide()
            #self.__search_users()
            self.__error_controller.handle_value_error("El nicho se ha creado exitosamente")
            self.__error_controller.show()
            logging.debug("Niche created")
        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
