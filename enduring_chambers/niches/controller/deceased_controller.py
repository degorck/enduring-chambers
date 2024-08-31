"""
Deceased Controller Module
"""
import logging
import datetime
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from niches.view.ui.main_window import Ui_MainWindow
from niches.model.dto.deceased_dto import DeceasedDto
from niches.service.remain_type_service import RemainTypeService
from niches.service.module_service import ModuleService
from niches.service.row_service import RowService
from niches.service.niche_service import NicheService
from niches.service.deceased_service import DeceasedService
from niches.util.drag_and_drop_create_util import DragAndDropCreateUtil
from niches.util.drag_and_drop_modify_util import DragAndDropModifyUtil
from niches.constant.constants import FieldName, UserTypeKey, HASHED_BOOLEAN_CONVERTER_IS_ACTIVE
from niches.constant.constants import STARTS_LOGGING_CONSTANT, ENDS_LOGGING_CONSTANT
from niches.util.ftp_util import send_image, delete_image, download_image
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
        self.__row = 0
        self.__drag_and_drop_util_create_deceased = DragAndDropCreateUtil(main_window)
        self.__drag_and_drop_util_modify_deceased = DragAndDropModifyUtil(main_window)
        self.__remain_type_service = RemainTypeService()
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__niche_service = NicheService()
        self.__deceased_service = DeceasedService()
        self.__error_controller = ErrorController()
        self.__loaded_deceased_dto = DeceasedDto()
        self.__configure_actions()
        self.__configure_combo_box_remain_type()
        self.__configure_combo_box_module()
        self.__configure_combo_box_row_create()
        self.__initialize_date_edit()
        self.__configure_table()
        self.__search_deceased()
        logging.debug("Deceased controller initialized")

    def __initialize_date_edit(self):
        today = datetime.datetime.now()
        today_qdate = QtCore.QDate(today.year, today.month, today.day)
        self.main_window.date_edit_create_deceased_birth_date.setDate(today_qdate)
        self.main_window.date_edit_create_deceased_death_date.setDate(today_qdate)
        self.main_window.date_edit_modify_deceased_birth_date.setDate(today_qdate)
        self.main_window.date_edit_modify_deceased_death_date.setDate(today_qdate)
        logging.debug("Date edit initialized")

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
        self.main_window.line_edit_search_deceased.editingFinished.connect(self.__search_deceased)
        self.main_window.table_widget_deceased.cellDoubleClicked.connect(self.__select_deceased)
        self.main_window.push_button_modify_deceased_image.clicked.connect(
            self.__show_modify_deceased_image_widget)
        self.main_window.push_button_modify_deceased_save.clicked.connect(
            self.__update_deceased)
        self.main_window.check_box_create_deceased_birth_date.stateChanged.connect(
            self.__date_edit_create_deceased_birth_date_change)
        self.main_window.check_box_create_deceased_death_date.stateChanged.connect(
            self.__date_edit_create_deceased_death_date_change)
        self.main_window.check_box_modify_deceased_birth_date.stateChanged.connect(
            self.__date_edit_modify_deceased_birth_date_change)
        self.main_window.check_box_modify_deceased_death_date.stateChanged.connect(
            self.__date_edit_modify_deceased_death_date_change)
        self.main_window.push_button_create_deceased_clean.clicked.connect(
            self.__clean_stacked_widget_deceased)
        self.main_window.push_button_modify_deceased_active.clicked.connect(
            self.__activate)
        self.main_window.push_button_modify_deceased_deactivate.clicked.connect(
            self.__deactivate)
        logging.debug("Deceased controller actions configured")

    def __show_create_deceased_image_widget(self):
        self.__drag_and_drop_util_create_deceased.show()
        self.__drag_and_drop_util_create_deceased.open_window_configuration()
        logging.debug("Show create image widget")

    def __show_modify_deceased_image_widget(self):
        self.__drag_and_drop_util_modify_deceased.show()
        self.__drag_and_drop_util_modify_deceased.open_window_configuration()
        logging.debug("Show modify image widget")

    def __configure_combo_box_remain_type(self):
        list_remain_type_dto = self.__remain_type_service.find_all()
        for remain_type_dto in list_remain_type_dto:
            self.main_window.combo_box_create_deceased_remain_type.addItem(
                remain_type_dto.get_name(), remain_type_dto)
            self.main_window.combo_box_modify_deceased_remain_type.addItem(
                remain_type_dto.get_name(), remain_type_dto)
        logging.debug("Combo box remain type configured")

    def __configure_combo_box_module(self):
        self.main_window.combo_box_create_deceased_module.addItem("", None)
        self.main_window.combo_box_modify_deceased_module.addItem("", None)
        list_module_dto = self.__module_service.find_all_active()
        for module_dto in list_module_dto:
            self.main_window.combo_box_create_deceased_module.addItem(
                module_dto.get_name(), module_dto)
            self.main_window.combo_box_modify_deceased_module.addItem(
                module_dto.get_name(), module_dto)
        logging.debug("Combo box module configured")

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
        logging.debug("Combo box row create configured")

    def __configure_combo_box_row_modify(self):
        self.main_window.combo_box_modify_deceased_row.clear()
        self.main_window.combo_box_modify_deceased_row.addItem("", None)
        if self.main_window.combo_box_modify_deceased_module.currentData() is None:
            self.main_window.combo_box_modify_deceased_row.setCurrentText("")
            self.main_window.combo_box_modify_deceased_row.setEnabled(False)
        else:
            self.main_window.combo_box_modify_deceased_row.setEnabled(True)
            list_row_dto = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_modify_deceased_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_modify_deceased_row.addItem(
                    row_dto.get_name(), row_dto)
        logging.debug("Combo box row modify configured")

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
        logging.debug("Combo box niche create configured")

    def __configure_combo_box_niche_modify(self):
        self.main_window.combo_box_modify_deceased_niche.clear()
        self.main_window.combo_box_modify_deceased_niche.addItem("", None)
        if self.main_window.combo_box_modify_deceased_row.currentData() is None:
            self.main_window.combo_box_modify_deceased_niche.setEnabled(False)
        else:
            self.main_window.combo_box_modify_deceased_niche.setEnabled(True)
            list_niche_dto = self.__niche_service.search_niches_by_module_id_and_row_id(
                "",
                self.main_window.combo_box_modify_deceased_module.currentData().get_id(),
                self.main_window.combo_box_modify_deceased_row.currentData().get_id())
            for niche_dto in list_niche_dto:
                self.main_window.combo_box_modify_deceased_niche.addItem(
                    str(niche_dto.get_number()), niche_dto)
        logging.debug("Combo box niche modify configured")

    def __create_deceased(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_create_deceased_name.text(),
                                  FieldName.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_create_deceased_paternal_surname.text(),
                FieldName.PATERNAL_SURNAME)
            validate_not_none(self.main_window.combo_box_create_deceased_niche.currentData(),
                              FieldName.NICHE)
            deceased_dto = DeceasedDto()
            if self.main_window.check_box_create_deceased_birth_date.isChecked():
                birth_date = None
            else:
                q_date_birth_date = self.main_window.date_edit_create_deceased_birth_date.date()
                birth_date = datetime.datetime(q_date_birth_date.year(), q_date_birth_date.month(),
                                           q_date_birth_date.day())
            if self.main_window.check_box_create_deceased_death_date.isChecked():
                death_date = None
            else:
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
            self.__niche_service.occupy_niche(deceased_dto.get_niche().get_id())
            self.__search_deceased()
            self.__error_controller.handle_value_error("El difunto se ha creado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_user.hide()
            self.main_window.scroll_area_create_deceased.hide()
            self.__clear_scroll_area_create_deceased()
            logging.debug("Se guardó el difunto [%s]", deceased_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
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
        logging.debug("Clear scroll area create deceased")

    def __search_deceased(self):
        if self.main_window.get_logged_user_type_key() == UserTypeKey.ADMINISTRATOR.value:
            list_deceased_dto = self.__deceased_service.search_all_deceased(
                self.main_window.line_edit_search_deceased.text())
        else:
            list_deceased_dto = self.__deceased_service.search_all_deceased(
                self.main_window.line_edit_search_deceased.text())
        self.__row = len(list_deceased_dto)
        self.__configure_table()
        row = 0

        for deceased_dto in list_deceased_dto:
            if deceased_dto.get_niche().get_holder() is None:
                holder_name = "Sin titular"
            else:
                if deceased_dto.get_niche().get_holder().get_paternal_surname() is None:
                    paternal_surname = ""
                else:
                    paternal_surname = deceased_dto.get_niche().get_holder().get_paternal_surname()
                if deceased_dto.get_niche().get_holder().get_maternal_surname() is None:
                    maternal_surname = ""
                else:
                    maternal_surname = deceased_dto.get_niche().get_holder().get_maternal_surname()
                if deceased_dto.get_birth_date() is None:
                    birth_date = "Desconocido"
                else:
                    birth_date = str(deceased_dto.get_birth_date().strftime('%d/%b/%Y'))
                if deceased_dto.get_death_date() is None:
                    death_date = "Desconocido"
                else:
                    death_date = str(deceased_dto.get_death_date().strftime('%d/%b/%Y'))

                holder_name = (deceased_dto.get_niche().get_holder().get_name() + " " +
                               paternal_surname + " " +
                               maternal_surname)
            self.main_window.table_widget_deceased.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(deceased_dto.get_id())))
            self.main_window.table_widget_deceased.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                deceased_dto.get_name()))
            self.main_window.table_widget_deceased.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                deceased_dto.get_paternal_surname()))
            self.main_window.table_widget_deceased.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                deceased_dto.get_maternal_surname()))
            self.main_window.table_widget_deceased.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                   birth_date))
            self.main_window.table_widget_deceased.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                    death_date))
            self.main_window.table_widget_deceased.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                    deceased_dto.get_remain_type().get_name()))
            self.main_window.table_widget_deceased.setItem(
                row,
                7,
                QtWidgets.QTableWidgetItem(
                    deceased_dto.get_niche().get_row().get_module().get_name()))
            self.main_window.table_widget_deceased.setItem(
                row,
                8,
                QtWidgets.QTableWidgetItem(
                    deceased_dto.get_niche().get_row().get_name()))
            self.main_window.table_widget_deceased.setItem(
                row,
                9,
                QtWidgets.QTableWidgetItem(
                    str(deceased_dto.get_niche().get_number())))
            self.main_window.table_widget_deceased.setItem(
                row,
                10,
                QtWidgets.QTableWidgetItem(
                    deceased_dto.get_book()))
            self.main_window.table_widget_deceased.setItem(
                row,
                11,
                QtWidgets.QTableWidgetItem(
                    deceased_dto.get_sheet()))
            self.main_window.table_widget_deceased.setItem(
                row,
                12,
                QtWidgets.QTableWidgetItem(
                    holder_name))
            self.main_window.table_widget_deceased.setItem(
                row,
                13,
                QtWidgets.QTableWidgetItem(
                    HASHED_BOOLEAN_CONVERTER_IS_ACTIVE[str(deceased_dto.is_active())]))
            self.main_window.table_widget_deceased.setItem(
                row,
                14,
                QtWidgets.QTableWidgetItem(
                    str(deceased_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_deceased.setItem(
                row,
                15,
                QtWidgets.QTableWidgetItem(
                    str(deceased_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_deceased.resizeColumnsToContents()
            self.main_window.table_widget_deceased.resizeRowsToContents()
            row = row + 1
        logging.debug("Search all deceased")

    def __configure_table(self):
        self.main_window.table_widget_deceased.clear()
        self.main_window.table_widget_deceased.setRowCount(self.__row)
        self.main_window.table_widget_deceased.setColumnCount(16)
        self.main_window.table_widget_deceased.setHorizontalHeaderLabels(("id",
                                                           "Nombre",
                                                           "Apellido Paterno",
                                                           "Apellido Materno",
                                                           "Fecha de Nacimiento",
                                                           "Fecha de Defunción",
                                                           "Tipo de restos",
                                                           "Módulo",
                                                           "Fila",
                                                           "Número",
                                                           "Libro",
                                                           "Foja",
                                                           "Titular",
                                                           "Activo",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_deceased.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_deceased.horizontalHeader().setMaximumSectionSize(500)
        self.main_window.table_widget_deceased.resizeRowsToContents()
        self.main_window.table_widget_deceased.resizeColumnsToContents()
        logging.debug("Table configured")

    def __select_deceased(self):
        row = self.main_window.table_widget_deceased.currentRow()
        deceased_id = int(self.main_window.table_widget_deceased.item(row, 0).text())
        self.main_window.scroll_area_modify_deceased.show()
        self.__load_deceased(deceased_id)
        logging.debug("Select deceased")

    def __load_deceased(self, deceased_id:int):
        deceased_dto = self.__deceased_service.find_by_id(deceased_id)
        self.__loaded_deceased_dto.existing_deceased(
            deceased_dto.get_id(),
            deceased_dto.get_name(),
            deceased_dto.get_paternal_surname(),
            deceased_dto.get_maternal_surname(),
            deceased_dto.get_birth_date(),
            deceased_dto.get_death_date(),
            deceased_dto.get_remain_type(),
            deceased_dto.get_niche(),
            deceased_dto.get_book(),
            deceased_dto.get_sheet(),
            deceased_dto.get_image_route(),
            deceased_dto.is_active(),
            deceased_dto.get_created_at(),
            deceased_dto.get_updated_at()
        )
        try:
            if (self.__loaded_deceased_dto.get_image_route() is None) or (
                self.__loaded_deceased_dto.get_image_route() == ""):
                tmp_image_path = None
                self.main_window.label_modify_deceased_image.clear()
                self.main_window.label_modify_deceased_image.setText("Sin imagen")
            else:
                tmp_image_path = download_image(self.__loaded_deceased_dto.get_image_route())

        except Exception as e:
            tmp_image_path = None
            self.main_window.label_modify_deceased_image.clear()
            self.main_window.label_modify_deceased_image.setText("Sin imagen")
            self.__error_controller.handle_exception_error("Al parecer, " +
                                    f'la imagen destino no existe\n Error : [{e}]')
            logging.error(e)
            self.__error_controller.show()

        if tmp_image_path is None:
            pass
        else:
            self.__load_modify_image(tmp_image_path)

        self.main_window.line_edit_modify_deceased_name.setText(
            self.__loaded_deceased_dto.get_name())
        self.main_window.line_edit_modify_deceased_paternal_surname.setText(
            self.__loaded_deceased_dto.get_paternal_surname())
        self.main_window.line_edit_modify_deceased_maternal_surname.setText(
            self.__loaded_deceased_dto.get_maternal_surname())
        self.main_window.combo_box_modify_deceased_remain_type.setCurrentText(
            self.__loaded_deceased_dto.get_remain_type().get_name())
        self.main_window.combo_box_modify_deceased_module.setCurrentText(
            self.__loaded_deceased_dto.get_niche().get_row().get_module().get_name())
        self.main_window.combo_box_modify_deceased_row.setCurrentText(
            self.__loaded_deceased_dto.get_niche().get_row().get_name())
        self.main_window.combo_box_modify_deceased_niche.setCurrentText(
            str(self.__loaded_deceased_dto.get_niche().get_number()))
        self.main_window.plain_text_edit_modify_deceased_book.setPlainText(
            self.__loaded_deceased_dto.get_book())
        self.main_window.plain_text_edit_modify_deceased_sheet.setPlainText(
            self.__loaded_deceased_dto.get_sheet())
        birth_date = self.__loaded_deceased_dto.get_birth_date()
        if birth_date is not None:
            birth_qdate = QtCore.QDate(birth_date.year, birth_date.month, birth_date.day)
            self.main_window.date_edit_modify_deceased_birth_date.setDate(birth_qdate)
            self.main_window.check_box_modify_deceased_birth_date.setChecked(False)
        else:
            self.main_window.check_box_modify_deceased_birth_date.setChecked(True)
        death_date = self.__loaded_deceased_dto.get_death_date()
        if death_date is not None:
            death_qdate = QtCore.QDate(death_date.year, death_date.month, death_date.day)
            self.main_window.date_edit_modify_deceased_death_date.setDate(death_qdate)
            self.main_window.check_box_modify_deceased_death_date.setChecked(False)
        else:
            self.main_window.check_box_modify_deceased_death_date.setChecked(True)
        logging.debug("Se cargó el difunto [%s]", self.__loaded_deceased_dto.to_string())

    def __load_modify_image(self, file_path):
        self.main_window.label_modify_deceased_image.setPixmap(QPixmap("." + file_path).scaled(
            170, 200, Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))
        logging.debug("Se cargó la imagen [%s]", file_path)

    def __update_deceased(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_modify_deceased_name.text(),
                                  FieldName.NAME)
            validate_is_not_empty(
                self.main_window.line_edit_modify_deceased_paternal_surname.text(),
                FieldName.PATERNAL_SURNAME)
            validate_not_none(self.main_window.combo_box_modify_deceased_niche.currentData(),
                              FieldName.NICHE)
            if self.main_window.check_box_modify_deceased_birth_date.isChecked():
                birth_date = None
            else:
                q_date_birth_date = self.main_window.date_edit_modify_deceased_birth_date.date()
                birth_date = datetime.datetime(q_date_birth_date.year(), q_date_birth_date.month(),
                                           q_date_birth_date.day())
            if self.main_window.check_box_modify_deceased_death_date.isChecked():
                death_date = None
            else:
                q_death_birth_date = self.main_window.date_edit_modify_deceased_death_date.date()
                death_date = datetime.datetime(q_death_birth_date.year(), q_death_birth_date.month(),
                                           q_death_birth_date.day())
            image_route_loaded = self.__drag_and_drop_util_modify_deceased.get_file_path() if (
                self.__drag_and_drop_util_modify_deceased.get_file_path() is not None) else None

            if image_route_loaded is not None:
                image_route = send_image(image_route_loaded)
                if (self.__loaded_deceased_dto.get_image_route() is None) or(
                    self.__loaded_deceased_dto.get_image_route() == ""):
                    pass
                else:
                    delete_image(self.__loaded_deceased_dto.get_image_route())
            else:
                if (self.__loaded_deceased_dto.get_image_route() is None) or (
                    self.__loaded_deceased_dto.get_image_route() == ""):
                    image_route = None
                else:
                    image_route = self.__loaded_deceased_dto.get_image_route()

            deceased_dto = DeceasedDto()
            deceased_dto.set_id(self.__loaded_deceased_dto.get_id())
            deceased_dto.set_name(self.main_window.line_edit_modify_deceased_name.text())
            deceased_dto.set_paternal_surname(
                self.main_window.line_edit_modify_deceased_paternal_surname.text())
            deceased_dto.set_maternal_surname(
                self.main_window.line_edit_modify_deceased_maternal_surname.text())
            deceased_dto.set_birth_date(birth_date)
            deceased_dto.set_death_date(death_date)
            deceased_dto.set_remain_type(
                self.main_window.combo_box_modify_deceased_remain_type.currentData())
            deceased_dto.set_niche(
                self.main_window.combo_box_modify_deceased_niche.currentData())
            deceased_dto.set_book(
                self.main_window.plain_text_edit_modify_deceased_book.toPlainText())
            deceased_dto.set_sheet(
                self.main_window.plain_text_edit_modify_deceased_sheet.toPlainText())
            deceased_dto.set_image_route(image_route)

            self.__deceased_service.modify_deceased(deceased_dto)

            self.__loaded_deceased_dto.existing_deceased(
                deceased_dto.get_id(),
                deceased_dto.get_name(),
                deceased_dto.get_paternal_surname(),
                deceased_dto.get_maternal_surname(),
                deceased_dto.get_birth_date(),
                deceased_dto.get_death_date(),
                deceased_dto.get_remain_type(),
                deceased_dto.get_niche(),
                deceased_dto.get_book(),
                deceased_dto.get_sheet(),
                deceased_dto.get_image_route(),
                deceased_dto.is_active(),
                deceased_dto.get_created_at(),
                deceased_dto.get_updated_at()
            )
            self.__search_deceased()
            self.__error_controller.handle_value_error("El difunto se ha modificado exitosamente")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_deceased.hide()
            logging.debug("El difunto se ha modificado exitosamente")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __date_edit_create_deceased_birth_date_change(self):
        self.main_window.date_edit_create_deceased_birth_date.setEnabled(
            not self.main_window.check_box_create_deceased_birth_date.isChecked())

    def __date_edit_create_deceased_death_date_change(self):
        self.main_window.date_edit_create_deceased_death_date.setEnabled(
            not self.main_window.check_box_create_deceased_death_date.isChecked())
    
    def __date_edit_modify_deceased_birth_date_change(self):
        self.main_window.date_edit_modify_deceased_birth_date.setEnabled(
            not self.main_window.check_box_modify_deceased_birth_date.isChecked())

    def __date_edit_modify_deceased_death_date_change(self):
        self.main_window.date_edit_modify_deceased_death_date.setEnabled(
            not self.main_window.check_box_modify_deceased_death_date.isChecked())

    def __clean_stacked_widget_deceased(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.main_window.line_edit_create_deceased_name.clear()
        self.main_window.line_edit_create_deceased_paternal_surname.clear()
        self.main_window.line_edit_create_deceased_maternal_surname.clear()
        self.main_window.check_box_create_deceased_birth_date.setChecked(False)
        self.main_window.check_box_create_deceased_death_date.setChecked(False)
        self.main_window.combo_box_create_deceased_remain_type.setCurrentIndex(0)
        self.main_window.combo_box_create_deceased_module.setCurrentIndex(0)
        self.main_window.plain_text_edit_create_deceased_book.clear()
        self.main_window.plain_text_edit_create_deceased_sheet.clear()
        logging.debug(ENDS_LOGGING_CONSTANT)
    
    def __activate(self):
        try:
            self.__deceased_service.activate_holder(self.__loaded_deceased_dto.get_id())
            self.__search_deceased()
            self.__error_controller.handle_value_error("El difunto se ha activado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_deceased.hide()
            logging.debug("El difunto se ha activado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def __deactivate(self):
        try:
            self.__deceased_service.deactivate_deceased(self.__loaded_deceased_dto.get_id())
            self.__search_deceased()
            self.__error_controller.handle_value_error("El difunto se ha desactivado")
            self.__error_controller.show()
            self.main_window.scroll_area_modify_deceased.hide()
            logging.debug("El difunto se ha desactivado")

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
