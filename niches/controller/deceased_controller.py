"""
Deceased Controller Module
"""
import logging
import datetime
from PySide6 import QtCore
from niches.view.ui.main_window import Ui_MainWindow
from niches.model.dto.deceased_dto import DeceasedDto
from niches.service.remain_type_service import RemainTypeService
from niches.service.module_service import ModuleService
from niches.service.row_service import RowService
from niches.service.niche_service import NicheService
from niches.service.deceased_service import DeceasedService
from niches.util.drag_and_drop_util import DragAndDropUtil
from niches.constant.constants import UserField
from niches.util.ftp_util import send_image, delete_image, dowloand_image
from niches.util.validator import validate_is_not_empty, validate_not_none
from niches.controller.error_controller import ErrorController

class DeceasedController:
    """
    Deceased controller class

    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__drag_and_drop_util_create_deceased = DragAndDropUtil(main_window)
        self.__remain_type_service = RemainTypeService()
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__niche_service = NicheService()
        self.__deceased_service = DeceasedService()
        self.__error_controller = ErrorController()
        self.__configure_actions()
        self.__configure_combo_box_remain_type()
        self.__configure_combo_box_module()
        self.__configure_combo_box_row_create()
        self.__initialize_date_edit()

    def __initialize_date_edit(self):
        today = datetime.datetime.now()
        today_qdate = QtCore.QDate(today.year, today.month, today.day)
        self.main_window.date_edit_create_deceased_birth_date.setDate(today_qdate)
        self.main_window.date_edit_create_deceased_death_date.setDate(today_qdate)
        self.main_window.date_edit_modify_deceased_birth_date.setDate(today_qdate)
        self.main_window.date_edit_modify_deceased_death_date.setDate(today_qdate)

    def __configure_actions(self):
        self.main_window.push_button_create_deceased_create.clicked.connect(
            self.main_window.scroll_area_create_deceased.show)
        self.main_window.push_button_create_deceased_save_deceased.clicked.connect(
            self.__create_deceased)
        self.main_window.combo_box_create_deceased_module.currentIndexChanged.connect(
            self.__configure_combo_box_row_create)
        self.main_window.combo_box_modify_deceased_module.currentIndexChanged.connect(
            self.__configure_combo_box_row_modify)
        self.main_window.combo_box_create_deceased_row.currentIndexChanged.connect(
            self.__configure_combo_box_niche_create)
        self.main_window.combo_box_modify_deceased_row.currentIndexChanged.connect(
            self.__configure_combo_box_niche_modify)
        self.main_window.label_create_deceased_image.setMaximumWidth(175)
        self.main_window.push_button_create_deceased_image.clicked.connect(
            self.__show_create_deceased_image_widget)

    def __show_create_deceased_image_widget(self):
        self.__drag_and_drop_util_create_deceased.show()
        self.__drag_and_drop_util_create_deceased.open_window_configuration()

    def __configure_combo_box_remain_type(self):
        list_remain_type_dto = self.__remain_type_service.find_all()
        for remain_type_dto in list_remain_type_dto:
            self.main_window.combo_box_create_deceased_remain_type.addItem(
                remain_type_dto.get_name(), remain_type_dto)
            self.main_window.combo_box_modify_deceased_remain_type.addItem(
                remain_type_dto.get_name(), remain_type_dto)

    def __configure_combo_box_module(self):
        self.main_window.combo_box_create_deceased_module.addItem("", None)
        self.main_window.combo_box_modify_deceased_module.addItem("", None)
        list_module_dto = self.__module_service.find_all_active()
        for module_dto in list_module_dto:
            self.main_window.combo_box_create_deceased_module.addItem(
                module_dto.get_name(), module_dto)
            self.main_window.combo_box_modify_deceased_module.addItem(
                module_dto.get_name(), module_dto)

    def __configure_combo_box_row_create(self):
        self.main_window.combo_box_create_deceased_row.clear()
        self.main_window.combo_box_create_deceased_row.addItem("", None)
        if self.main_window.combo_box_create_deceased_module.currentData() is None:
            self.main_window.combo_box_create_deceased_row.setEnabled(False)
        else:
            self.main_window.combo_box_create_deceased_row.setEnabled(True)
            list_row_dto = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_create_deceased_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_create_deceased_row.addItem(
                    row_dto.get_name(), row_dto)

    def __configure_combo_box_row_modify(self):
        self.main_window.combo_box_modify_deceased_row.clear()
        self.main_window.combo_box_modify_deceased_row.addItem("", None)
        if self.main_window.combo_box_modify_deceased_module.currentData() is None:
            self.main_window.combo_box_modify_deceased_row.setEnabled(False)
        else:
            self.main_window.combo_box_modify_deceased_row.setEnabled(True)
            list_row_dto = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_modify_deceased_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_modify_deceased_row.addItem(
                    row_dto.get_name(), row_dto)

    def __configure_combo_box_niche_create(self):
        self.main_window.combo_box_create_deceased_niche.clear()
        self.main_window.combo_box_create_deceased_niche.addItem("", None)
        if self.main_window.combo_box_create_deceased_row.currentData() is None:
            self.main_window.combo_box_create_deceased_niche.setEnabled(False)
        else:
            self.main_window.combo_box_create_deceased_niche.setEnabled(True)
            list_niche_dto = self.__niche_service.search_not_busy_niches_by_module_id_and_row_id(
                "",
                self.main_window.combo_box_create_deceased_module.currentData().get_id(),
                self.main_window.combo_box_create_deceased_row.currentData().get_id())
            for niche_dto in list_niche_dto:
                self.main_window.combo_box_create_deceased_niche.addItem(
                    str(niche_dto.get_number()), niche_dto)

    def __configure_combo_box_niche_modify(self):
        self.main_window.combo_box_modify_deceased_niche.clear()
        self.main_window.combo_box_modify_deceased_niche.addItem("", None)
        if self.main_window.combo_box_modify_deceased_row.currentData() is None:
            self.main_window.combo_box_modify_deceased_niche.setEnabled(False)
        else:
            self.main_window.combo_box_modify_deceased_niche.setEnabled(True)
            list_niche_dto = self.__niche_service.search_not_busy_niches_by_module_id_and_row_id(
                "",
                self.main_window.combo_box_modify_deceased_module.currentData().get_id(),
                self.main_window.combo_box_modify_deceased_row.currentData().get_id())
            for niche_dto in list_niche_dto:
                self.main_window.combo_box_modify_deceased_niche.addItem(
                    str(niche_dto.get_number()), niche_dto)

    def __create_deceased(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_create_deceased_name.text(),
                                  UserField.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_deceased_paternal_surname.text(),
                UserField.PATERNAL_SURNAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_deceased_maternal_surname.text(),
                UserField.MATERNAL_SURNAME)
            validate_not_none(self.main_window.combo_box_create_deceased_niche.currentData(),
                              UserField.NICHE)
            deceased_dto = DeceasedDto()
            q_date_birth_date = self.main_window.date_edit_create_deceased_birth_date.date()
            birth_date = datetime.datetime(q_date_birth_date.year(), q_date_birth_date.month(),
                                           q_date_birth_date.day())
            q_date_death_date = self.main_window.date_edit_create_deceased_death_date.date()
            death_date = datetime.datetime(q_date_death_date.year(), q_date_death_date.month(),
                                           q_date_death_date.day())
            image_route_loaded = self.__drag_and_drop_util_create_deceased.get_file_path() if (
                self.__drag_and_drop_util_create_deceased.get_file_path() is not None) else None

            if image_route_loaded is not None:
                image_route = send_image(image_route_loaded)
            else:
                image_route = None

            deceased_dto.new_deceased(
                self.main_window.line_edit_create_deceased_name.text(),
                self.main_window.line_edit_create_deceased_paternal_surname.text(),
                self.main_window.line_edit_create_deceased_maternal_surname.text(),
                birth_date,
                death_date,
                self.main_window.combo_box_create_deceased_remain_type.currentData(),
                self.main_window.combo_box_create_deceased_niche.currentData(),
                self.main_window.plain_text_edit_create_deceased_book.toPlainText(),
                self.main_window.plain_text_edit_create_deceased_sheet.toPlainText(),
                image_route
            )
            self.__deceased_service.create_deceased(deceased_dto)
            self.main_window.scroll_area_create_deceased.hide()
            self.__clear_scroll_area_create_deceased()
            logging.debug("Se guardó el difunto [%s]", deceased_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __clear_scroll_area_create_deceased(self):
        self.main_window.line_edit_create_deceased_name.clear()
        self.main_window.line_edit_create_deceased_paternal_surname.clear()
        self.main_window.line_edit_create_deceased_maternal_surname.clear()
        self.main_window.combo_box_create_deceased_module.setCurrentText("")
        self.main_window.label_create_deceased_image.clear()
        self.main_window.plain_text_edit_create_deceased_book.clear()
        self.main_window.plain_text_edit_create_deceased_sheet.clear()
        self.__initialize_date_edit()
        self.__drag_and_drop_util_create_deceased.open_window_configuration()
