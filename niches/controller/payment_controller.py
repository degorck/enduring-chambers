"""
Payment Controller Module
"""
import logging
import datetime
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.module_service import ModuleService
from niches.service.row_service import RowService
from niches.service.niche_service import NicheService
from niches.model.dto.module_dto import ModuleDto
from niches.model.dto.row_dto import RowDto
from niches.model.dto.niche_dto import NicheDto
from niches.model.dto.payment_dto import PaymentDto
from niches.service.payment_service import PaymentService
from niches.controller.error_controller import ErrorController
from niches.util.validator import validate_not_none, validate_not_zero
from niches.constant.constants import UserField, UserTypeKey

class PaymentController:
    """
    Payment controller class
    
    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__row = 0
        self.__module_service = ModuleService()
        self.__row_service = RowService()
        self.__niche_service = NicheService()
        self.__payment_service = PaymentService()
        self.__error_controller = ErrorController()
        self.__configure_combo_box_module()
        self.__configure_combo_box_row()
        self.__configure_combo_box_niche()
        self.__configure_table()
        self.__initialize_date_edit()
        self.__search_payment()
        self.__configure_actions()

    def __initialize_date_edit(self):
        today = datetime.datetime.now()
        today_qdate = QtCore.QDate(today.year, today.month, today.day)
        self.main_window.date_edit_payment_create_payment_date.setDate(today_qdate)
        self.main_window.date_edit_payment_modify_payment_date.setDate(today_qdate)

    def __configure_actions(self):
        self.main_window.combo_box_payments_module.currentIndexChanged.connect(
            self.__configure_combo_box_row)
        self.main_window.combo_box_payments_row.currentIndexChanged.connect(
            self.__configure_combo_box_niche)
        self.main_window.push_button_payment_create.clicked.connect(
            self.main_window.scroll_area_payment_create.show)
        self.main_window.push_button_payment_create_save.clicked.connect(
            self.__create_payment)
        self.main_window.combo_box_payment_niche.currentIndexChanged.connect(
            self.__search_payment)

    def __configure_combo_box_module(self):
        list_module_dto:list[ModuleDto] = self.__module_service.find_all_active()
        self.main_window.combo_box_payments_module.clear()
        self.main_window.combo_box_payments_module.addItem("", None)
        for module_dto in list_module_dto:
            self.main_window.combo_box_payments_module.addItem(
                module_dto.get_name(), module_dto)

    def __configure_combo_box_row(self):
        if self.main_window.combo_box_payments_module.currentData() is None:
            self.main_window.combo_box_payments_row.setCurrentText("")
            self.main_window.combo_box_payments_row.setEnabled(False)
        else:
            self.main_window.combo_box_payments_row.setEnabled(True)
            self.main_window.combo_box_payments_row.clear()
            self.main_window.combo_box_payments_row.addItem("", None)
            list_row_dto:list[RowDto] = self.__row_service.find_all_by_module_id(
                self.main_window.combo_box_payments_module.currentData().get_id())
            for row_dto in list_row_dto:
                self.main_window.combo_box_payments_row.addItem(
                    row_dto.get_name(), row_dto)

    def __configure_combo_box_niche(self):
        self.main_window.combo_box_payment_niche.clear()
        self.main_window.combo_box_payment_niche.addItem("", None)
        if self.main_window.combo_box_payments_row.currentData() is None:
            self.main_window.combo_box_payment_niche.setEnabled(False)
        else:
            self.main_window.combo_box_payment_niche.setEnabled(True)
            list_niche_dto = self.__niche_service.search_not_busy_niches_by_module_id_and_row_id(
                "",
                self.main_window.combo_box_payments_module.currentData().get_id(),
                self.main_window.combo_box_payments_row.currentData().get_id())
            for niche_dto in list_niche_dto:
                self.main_window.combo_box_payment_niche.addItem(
                    str(niche_dto.get_number()), niche_dto)

    def __configure_table(self):
        self.main_window.table_widget_payments.clear()
        self.main_window.table_widget_payments.setRowCount(self.__row)
        self.main_window.table_widget_payments.setColumnCount(7)
        self.main_window.table_widget_payments.setHorizontalHeaderLabels(("id",
                                                           "Nicho",
                                                           "Cantidad",
                                                           "Fecha de pago",
                                                           "Comentarios",
                                                           "Creado",
                                                           "Actualizado"))
        self.main_window.table_widget_payments.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.main_window.table_widget_payments.horizontalHeader().setMaximumSectionSize(500)
        self.main_window.table_widget_payments.resizeRowsToContents()
        self.main_window.table_widget_payments.resizeColumnsToContents()

    def __create_payment(self):
        try:
            validate_not_none(self.main_window.combo_box_payment_niche.currentData(),
                              UserField.NICHE)
            validate_not_zero(self.main_window.double_spin_box_payment_create_quantity.value(),
                              UserField.QUANTITY)

            q_date_payment_date = self.main_window.date_edit_payment_create_payment_date.date()
            payment_date = datetime.datetime(q_date_payment_date.year(),
                                             q_date_payment_date.month(),
                                             q_date_payment_date.day())

            payment_dto = PaymentDto()
            payment_dto.new_payment(
                self.main_window.combo_box_payment_niche.currentData(),
                self.main_window.double_spin_box_payment_create_quantity.value(),
                payment_date,
                self.main_window.plain_text_edit_payment_create_comments.toPlainText()
            )

            self.__payment_service.create_payment(payment_dto)
            self.__search_payment()
            self.__error_controller.handle_value_error("El pago se ha creado")
            self.__error_controller.show()
            self.main_window.scroll_area_payment_create.hide()
            # self.__clear_scroll_area_create_deceased()
            logging.debug("Se creó el pago: [%s]", payment_dto.to_string())

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()

    def __search_payment(self):
        list_payment_dto = []
        if self.main_window.get_logged_user_type_key() == UserTypeKey.ADMINISTRATOR.value:
            if self.main_window.combo_box_payment_niche.currentData() is None:
                self.main_window.combo_box_payment_niche.setCurrentText("")
                self.main_window.combo_box_payment_niche.setEnabled(False)
            else:
                self.main_window.combo_box_payment_niche.setEnabled(True)
                list_payment_dto = self.__payment_service.search_all_payments_by_niche_id(
                    self.main_window.combo_box_payment_niche.currentData().get_id())
        else:
            if self.main_window.combo_box_payment_niche.currentData() is None:
                self.main_window.combo_box_payment_niche.setCurrentText("")
                self.main_window.combo_box_payment_niche.setEnabled(False)
            else:
                self.main_window.combo_box_payment_niche.setEnabled(True)
                list_payment_dto = self.__payment_service.search_all_payments_by_niche_id(
                    self.main_window.combo_box_payment_niche.currentData().get_id())
        self.__row = len(list_payment_dto)
        self.__configure_table()
        row = 0
        total = 0.0

        for payment_dto in list_payment_dto:
            niche_str = (payment_dto.get_niche().get_row().get_module().get_name() + "-" +
                         payment_dto.get_niche().get_row().get_name() + "-" +
                         str(payment_dto.get_niche().get_number()))

            self.main_window.table_widget_payments.setItem(
                row,
                0,
                QtWidgets.QTableWidgetItem(
                str(payment_dto.get_id())))
            self.main_window.table_widget_payments.setItem(
                row,
                1,
                QtWidgets.QTableWidgetItem(
                niche_str))
            self.main_window.table_widget_payments.setItem(
                row,
                2,
                QtWidgets.QTableWidgetItem(
                str(payment_dto.get_quantity())))
            self.main_window.table_widget_payments.setItem(
                row,
                3,
                QtWidgets.QTableWidgetItem(
                    str(payment_dto.get_payment_date().strftime('%d/%b/%Y'))))
            self.main_window.table_widget_payments.setItem(
                row,
                4,
                QtWidgets.QTableWidgetItem(
                    payment_dto.get_comments()))
            self.main_window.table_widget_payments.setItem(
                row,
                5,
                QtWidgets.QTableWidgetItem(
                    str(payment_dto.get_created_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_payments.setItem(
                row,
                6,
                QtWidgets.QTableWidgetItem(
                    str(payment_dto.get_updated_at().strftime('%d/%b/%Y %H:%M'))))
            self.main_window.table_widget_payments.resizeColumnsToContents()
            self.main_window.table_widget_payments.resizeRowsToContents()
            total = total + payment_dto.get_quantity()
            self.main_window.label_payment_search_total_value.setText(str(total))
            row = row + 1