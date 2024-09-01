"""
Module that controls the MainWindow
"""
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from niches.view.ui.main_window import Ui_MainWindow
from niches.model.dto.user_dto import UserDto
from niches.util.logging_configuration import get_loging
from niches.constant.constants import UserTypeKey
from niches.controller.login_controller import LoginController
from niches.controller.user_controller import UserController
from niches.controller.my_account_controller import MyAccountController
from niches.controller.holder_controller import HolderController
from niches.controller.niche_controller import NicheController
from niches.controller.deceased_controller import DeceasedController
from niches.controller.payment_controller import PaymentController
from niches.controller.module_controller import ModuleController
from niches.controller.row_controller import RowController
from niches.util.wheel_event_filter import WheelEventFilter
from niches.util.delete_old_log_files_util import delete_old_logs
from niches.constant.constants import STARTS_LOGGING_CONSTANT, ENDS_LOGGING_CONSTANT
logging = get_loging()

class EnduringChambers(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Class with the functionality of MainWindow

    Args:
        QtWidgets (QtWidgets.QMainWindow): Core QMainWindow
        Ui_MainWindow (Ui_MainWindow): Qt layer transformed to python code 
    """
    def __init__(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        super().__init__()
        self.setupUi(self)
        delete_old_logs()
        self.__login_controller = LoginController()
        self.__loaded_user_dto = UserDto()
        self.__logged_user_dto = UserDto()
        self.__user_type_key = UserTypeKey.NOT_LOGGED.value
        self.scroll_area_create_user.hide()
        self.scroll_area_modify_user.hide()
        self.scroll_area_create_holder.hide()
        self.scroll_area_modify_holder.hide()
        self.scroll_area_create_deceased.hide()
        self.scroll_area_modify_deceased.hide()
        self.__user_controller = UserController(self)
        self.__my_account_controller = MyAccountController(self)
        self.__holder_controller = HolderController(self)
        self.__niche_controller = NicheController(self)
        self.__deceased_controller = DeceasedController(self)
        self.__payment_controller = PaymentController(self)
        self.__module_controller = ModuleController(self)
        self.__row_controller = RowController(self)
        self.__configure_actions()
        self.__configure_windows_by_user_type()
        self.show()
        self.__login_controller.show()
        logging.debug(ENDS_LOGGING_CONSTANT)

    def get_logged_user_type_key(self):
        """
        Returns
            user_type_key : str
                The logged user type key
        """
        logging.debug("User type key: %s", self.__user_type_key)
        return self.__user_type_key

    def set_loaded_user_dto(self, user_dto:UserDto):
        """
        Sets the loaded UsetDto
        Args:
            user_dto : UserDto
                The user_dto to be set
        """
        self.__loaded_user_dto.existing_user(
            user_dto.get_id(),
            user_dto.get_name(),
            user_dto.get_paternal_surname(),
            user_dto.get_maternal_surname(),
            user_dto.get_user_type_id(),
            user_dto.get_user_name()
        )
        logging.debug("Loaded user dto: %s", self.__loaded_user_dto)

    def get_loaded_user_dto(self):
        """
        Returns
            loaded_user_dto : UserDto
                The loaded UserDto
        """
        logging.debug("Loaded user dto: %s", self.__loaded_user_dto)
        return self.__loaded_user_dto

    def get_logged_user_dto(self):
        """
        Returns
            logged_user_dto : UserDto
                The loaded UserDto
        """
        logging.debug("Logged user dto: %s", self.__logged_user_dto)
        return self.__logged_user_dto

    def __configure_actions(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.push_button_niches.clicked.connect(self.__set_stacked_widget_niches)
        self.push_button_deceased.clicked.connect(self.__set_stacked_widget_deceased)
        self.push_button_holders.clicked.connect(self.__set_stacked_widget_holders)
        self.push_button_payments.clicked.connect(self.__set_stacked_widget_payments) 
        self.__login_controller.push_button_login.clicked.connect(
            self.__configure_windows_by_user_type)
        self.__login_controller.line_edit_password.returnPressed.connect(
            self.__configure_windows_by_user_type)
        self.__login_controller.push_button_guest.clicked.connect(
            self.__configure_windows_by_user_type)
        self.push_button_my_account_logout.clicked.connect(self.__logout)
        self.push_button_modules.clicked.connect(self.__set_stacked_widget_modules)
        self.push_button_modules_return.clicked.connect(self.__set_stacked_widget_niches)
        self.push_button_rows.clicked.connect(self.__set_stacked_widget_rows)
        self.push_button_rows_return.clicked.connect(self.__set_stacked_widget_niches)
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __configure_windows_by_user_type(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.__user_type_key = self.__login_controller.get_logged_user_type_key()
        self.__logged_user_dto = self.__login_controller.get_logged_user()
        self.label_welcome_user_name.setText(self.__logged_user_dto.get_user_name())
        self.label_my_account_your_user_name.setText(self.__logged_user_dto.get_user_name())
        match self.__user_type_key:
            case UserTypeKey.GUEST.value:
                self.__configure_guest_window()
            case UserTypeKey.ADMINISTRATOR.value:
                self.__configure_administrator_window()
            case UserTypeKey.CAPTURIST.value:
                self.__configure_capturist_window()
            case UserTypeKey.NOT_LOGGED.value:
                self.__configure_not_logged_window()
        logging.info(
            "Se ha configurado la ventana de acuerdo al usuario loggeado: %s", self.__user_type_key)
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __configure_guest_window(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.label_welcome_user_name.setText("Invitado")
        self.label_my_account_your_user_name.setText("Invitado")
        self.stacked_widget.setEnabled(True)
        # User actions configuration
        self.push_button_create_user_create.setEnabled(False)
        self.scroll_area_modify_user.setEnabled(False)
        self.scroll_area_change_password.setEnabled(False)
        # Holder actions configuration
        self.push_button_create_holder_create.setEnabled(False)
        self.scroll_area_modify_holder.setEnabled(False)
        self.scroll_area_create_holder.setEnabled(False)
        # Deceased actions configuration
        self.push_button_create_deceased_create.setEnabled(False)
        self.scroll_area_create_deceased.setEnabled(False)
        self.scroll_area_modify_deceased.setEnabled(False)
        # Niches actions configuration
        self.push_button_create_niches_create.setEnabled(False)
        self.scroll_area_create_niche.setEnabled(False)
        self.scroll_area_modify_niche.setEnabled(False)
        # Payments actions configuration
        self.push_button_payment_create.setEnabled(False)
        self.scroll_area_payment_create.setEnabled(False)
        self.scroll_area_payment_modify.setEnabled(False)
        # Modules actions configuration
        self.push_button_module_create.setEnabled(False)
        self.scroll_area_create_module.setEnabled(False)
        self.scroll_area_modify_module.setEnabled(False)
        # Rows actions configuration
        self.push_button_row_create.setEnabled(False)
        self.scroll_area_create_row.setEnabled(False)
        self.scroll_area_modify_row.setEnabled(False)
        logging.info("Guest window configured")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __configure_administrator_window(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.stacked_widget.setEnabled(True)
        # User actions configuration
        self.push_button_create_user_create.setEnabled(True)
        self.scroll_area_modify_user.setEnabled(True)
        self.scroll_area_change_password.setEnabled(True)
        # Holder actions configuration
        self.push_button_create_holder_create.setEnabled(True)
        self.scroll_area_modify_holder.setEnabled(True)
        self.scroll_area_create_holder.setEnabled(True)
        self.push_button_modify_holder_activate.setEnabled(True)
        self.push_button_modify_holder_deactivate.setEnabled(True)
        # Deceased actions configuration
        self.push_button_create_deceased_create.setEnabled(True)
        self.scroll_area_create_deceased.setEnabled(True)
        self.scroll_area_modify_deceased.setEnabled(True)
        self.push_button_modify_deceased_active.setEnabled(True)
        self.push_button_modify_deceased_deactivate.setEnabled(True)
        # Niches actions configuration
        self.push_button_create_niches_create.setEnabled(True)
        self.scroll_area_create_niche.setEnabled(True)
        self.scroll_area_modify_niche.setEnabled(True)
        # Payments actions configuration
        self.push_button_payment_create.setEnabled(True)
        self.scroll_area_payment_create.setEnabled(True)
        self.scroll_area_payment_modify.setEnabled(True)
        # Modules actions configuration
        self.push_button_module_create.setEnabled(True)
        self.scroll_area_create_module.setEnabled(True)
        self.scroll_area_modify_module.setEnabled(True)
        # Rows actions configuration
        self.push_button_row_create.setEnabled(True)
        self.scroll_area_create_row.setEnabled(True)
        self.scroll_area_modify_row.setEnabled(True)
        logging.info("Administrator window configured")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __configure_capturist_window(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.stacked_widget.setEnabled(True)
        # User actions configuration
        self.push_button_create_user_create.setEnabled(False)
        self.scroll_area_modify_user.setEnabled(False)
        self.scroll_area_change_password.setEnabled(True)
        # Holder actions configuration
        self.push_button_create_holder_create.setEnabled(True)
        self.scroll_area_modify_holder.setEnabled(True)
        self.scroll_area_create_holder.setEnabled(True)
        self.push_button_modify_holder_activate.setEnabled(False)
        self.push_button_modify_holder_deactivate.setEnabled(False)
        # Deceased actions configuration
        self.push_button_create_deceased_create.setEnabled(True)
        self.scroll_area_create_deceased.setEnabled(True)
        self.scroll_area_modify_deceased.setEnabled(True)
        self.push_button_modify_deceased_active.setEnabled(False)
        self.push_button_modify_deceased_deactivate.setEnabled(False)
        # Niches actions configuration
        self.push_button_create_niches_create.setEnabled(False)
        self.scroll_area_create_niche.setEnabled(False)
        self.scroll_area_modify_niche.setEnabled(False)
        # Payments actions configuration
        self.push_button_payment_create.setEnabled(True)
        self.scroll_area_payment_create.setEnabled(True)
        self.scroll_area_payment_modify.setEnabled(False)
        # Modules actions configuration
        self.push_button_module_create.setEnabled(False)
        self.scroll_area_create_module.setEnabled(False)
        self.scroll_area_modify_module.setEnabled(False)
        # Rows actions configuration
        self.push_button_row_create.setEnabled(False)
        self.scroll_area_create_row.setEnabled(False)
        self.scroll_area_modify_row.setEnabled(False)
        logging.info("Capturist window configured")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __configure_not_logged_window(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.__user_type_key = UserTypeKey.NOT_LOGGED.value
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.setEnabled(False)
        logging.info("Not logged window configured")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_niches(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_create_niche.hide()
        self.scroll_area_modify_niche.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(4)
        self.line_edit_create_niche_name.clear()
        self.line_edit_create_niche_holder_search.clear()
        self.check_box_create_niche_is_busy.setChecked(False)
        self.check_box_create_niche_is_paid_off.setChecked(False)
        self.check_box_create_niche_is_donated.setChecked(False)
        logging.info("Niches stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_deceased(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_modify_deceased.hide()
        self.scroll_area_create_deceased.hide()
        self.push_button_deceased.setChecked(True)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.check_box_create_deceased_birth_date.setChecked(False)
        self.check_box_create_deceased_death_date.setChecked(False)
        self.combo_box_create_deceased_module.setCurrentIndex(0)
        self.plain_text_edit_create_deceased_book.clear()
        self.plain_text_edit_create_deceased_sheet.clear()
        self.line_edit_create_deceased_name.clear()
        self.line_edit_create_deceased_paternal_surname.clear()
        self.line_edit_create_deceased_maternal_surname.clear()
        self.combo_box_create_deceased_remain_type.setCurrentIndex(0)
        self.stacked_widget.setCurrentIndex(2)
        logging.info("Deceased stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_holders(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_create_holder.hide()
        self.scroll_area_modify_holder.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(True)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(3)
        self.line_edit_create_holder_name.clear()
        self.line_edit_create_holder_paternal_surname.clear()
        self.line_edit_create_holder_maternal_surname.clear()
        self.line_edit_create_holder_phone.clear()
        logging.info("Holders stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_payments(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_payment_create.hide()
        self.scroll_area_payment_modify.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(True)
        self.stacked_widget.setCurrentIndex(6)
        logging.info("Payments stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_modules(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_create_module.hide()
        self.scroll_area_modify_module.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(7)
        logging.info("Modules stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __set_stacked_widget_rows(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.scroll_area_create_row.hide()
        self.scroll_area_modify_row.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(8)
        logging.info("Rows stacked widget selected")
        logging.debug(ENDS_LOGGING_CONSTANT)

    def __logout(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.__configure_not_logged_window()
        self.__login_controller.line_edit_password.clear()
        self.__login_controller.line_edit_user.clear()
        self.__login_controller.show()
        logging.debug(ENDS_LOGGING_CONSTANT)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    filter = WheelEventFilter()
    app.installEventFilter(filter)
    window = EnduringChambers()
    sys.exit(app.exec())
