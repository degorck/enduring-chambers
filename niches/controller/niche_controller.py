"""
Niche Controller Module
"""
import logging
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.model.dto.module_dto import ModuleDto

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
        self.__configure_combo_box()
        self.__configure_actions()

    def __configure_combo_box(self):
        list_module_dto:list[ModuleDto] = self.__module_service.find_all()
        self.main_window.combo_box_niches_module.addItem("", None)
        for module_dto in list_module_dto:
            self.main_window.combo_box_niches_module.addItem(
                module_dto.get_name(), module_dto)

    def __configure_actions(self):
        logging.debug("Niche contrller configured")
