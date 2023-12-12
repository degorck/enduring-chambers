"""
Deceased Controller Module
"""
import logging
from niches.view.ui.main_window import Ui_MainWindow
from niches.model.dto.deceased_dto import DeceasedDto


class DeceasedController:
    """
    Deceased controller class

    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__configure_actions()

    def __configure_actions(self):
        self.main_window.push_button_create_deceased_create.clicked.connect(
            self.main_window.scroll_area_create_deceased.show)
        self.main_window.push_button_create_deceased_save_deceased.clicked.connect(
            self.__create_deceased)

    def __create_deceased(self):
        deceased = DeceasedDto()
        deceased.new_deceased(
            "Diego",
            "Martínez",
            "Terrones",
            None,
            None,
            None,
            None,
            "Book",
            "sheet",
            "route"
        )
        logging.debug("Se guardó el difunto [%s]", deceased.to_string())
