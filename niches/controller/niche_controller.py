"""
Niche Controller Module
"""
import logging
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.model.dto.module_dto import ModuleDto
from niches.service.row_service import RowService
from niches.model.dto.row_dto import RowDto

class NicheController:
    """
    Niche controller class
    Args:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__row = 0
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__configure_combo_box_niches()
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
        else:
            self.main_window.combo_box_niches_row.setEnabled(True)
            self.main_window.combo_box_niches_row.clear()
            list_row_dto:list[RowDto] = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_niches_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_niches_row.addItem(
                    row_dto.get_name(), row_dto)


    def __configure_actions(self):
        self.main_window.combo_box_niches_module.currentIndexChanged.connect(
            self.__configure_combo_box_rows)
