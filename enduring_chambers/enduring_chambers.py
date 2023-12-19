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
from niches.util.wheel_event_filter import WheelEventFilter
logging = get_loging()

class EnduringChambers(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Class with the functionality of MainWindow

    Args:
        QtWidgets (QtWidgets.QMainWindow): Core QMainWindow
        Ui_MainWindow (Ui_MainWindow): Qt layer transformed to python code 
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.spin_box_create_niche_number.setEnabled(False)
        self.__user_controller = UserController(self)
        self.__my_account_controller = MyAccountController(self)
        self.__holder_controller = HolderController(self)
        self.__niche_controller = NicheController(self)
        self.__deceased_controller = DeceasedController(self)
        self.__payment_controller = PaymentController(self)
        self.__configure_actions()
        self.__configure_windows_by_user_type()
        self.show()
        self.__login_controller.show()
        logging.info("System started")

    def get_logged_user_type_key(self):
        """
        Returns
            user_type_key : str
                The logged user type key
        """
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

    def get_loaded_user_dto(self):
        """
        Returns
            loaded_user_dto : UserDto
                The loaded UserDto
        """
        return self.__loaded_user_dto

    def get_logged_user_dto(self):
        """
        Returns
            logged_user_dto : UserDto
                The loaded UserDto
        """
        return self.__logged_user_dto

    def __configure_actions(self):
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

    def __configure_windows_by_user_type(self):
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
        logging.debug(
            "Se ha configurado la ventana de acuerdo al usuario loggeado: %s", self.__user_type_key)

    def __configure_guest_window(self):
        self.label_welcome_user_name.setText("Invitado")
        self.label_my_account_your_user_name.setText("Invitado")
        self.stacked_widget.setEnabled(True)
        self.push_button_create_user_create.setEnabled(False)
        self.scroll_area_modify_user.setEnabled(False)
        self.scroll_area_change_password.setEnabled(False)
        self.push_button_create_holder_create.setEnabled(False)
        self.scroll_area_modify_holder.setEnabled(False)
        self.scroll_area_create_holder.setEnabled(False)
        self.scroll_area_create_deceased.setEnabled(False)
        self.scroll_area_modify_deceased.setEnabled(False)

    def __configure_administrator_window(self):
        self.stacked_widget.setEnabled(True)
        self.push_button_create_user_create.setEnabled(True)
        self.scroll_area_modify_user.setEnabled(True)
        self.scroll_area_change_password.setEnabled(True)
        self.push_button_create_holder_create.setEnabled(True)
        self.scroll_area_modify_holder.setEnabled(True)
        self.scroll_area_create_holder.setEnabled(True)

    def __configure_capturist_window(self):
        self.stacked_widget.setEnabled(True)
        self.push_button_create_user_create.setEnabled(False)
        self.scroll_area_modify_user.setEnabled(False)
        self.scroll_area_change_password.setEnabled(True)
        self.push_button_create_holder_create.setEnabled(True)
        self.scroll_area_modify_holder.setEnabled(True)
        self.scroll_area_create_holder.setEnabled(True)
        self.push_button_modify_holder_activate.setEnabled(False)
        self.push_button_modify_holder_deactivate.setEnabled(False)

    def __configure_not_logged_window(self):
        self.__user_type_key = UserTypeKey.NOT_LOGGED.value
        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.setEnabled(False)

    def __set_stacked_widget_niches(self):
        self.scroll_area_create_niche.hide()
        self.scroll_area_modify_niche.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(4)
        logging.debug("Niches stacked widget selected")

    def __set_stacked_widget_deceased(self):
        self.scroll_area_modify_deceased.hide()
        self.scroll_area_create_deceased.hide()
        self.push_button_create_deceased_create.setEnabled(False)
        self.push_button_deceased.setChecked(True)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(2)
        logging.debug("Deceased stacked widget selected")

    def __set_stacked_widget_holders(self):
        self.scroll_area_create_holder.hide()
        self.scroll_area_modify_holder.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(True)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(3)
        logging.debug("Holders stacked widget selected")

    def __set_stacked_widget_payments(self):
        self.scroll_area_payment_create.hide()
        self.scroll_area_payment_modify.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(False)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(True)
        self.stacked_widget.setCurrentIndex(6)
        logging.debug("Payments stacked widget selected")

    def __set_stacked_widget_modules(self):
        #self.scroll_area_create_payments.hide()
        #self.scroll_area_modify_payments.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(7)
        logging.debug("Modules stacked widget selected")

    def __set_stacked_widget_rows(self):
        #self.scroll_area_create_payments.hide()
        #self.scroll_area_modify_payments.hide()
        self.push_button_deceased.setChecked(False)
        self.push_button_holders.setChecked(False)
        self.push_button_my_account.setChecked(False)
        self.push_button_niches.setChecked(True)
        self.push_button_users.setChecked(False)
        self.push_button_payments.setChecked(False)
        self.stacked_widget.setCurrentIndex(8)
        logging.debug("Rows stacked widget selected")

    def __logout(self):
        self.__configure_not_logged_window()
        self.__login_controller.line_edit_password.clear()
        self.__login_controller.line_edit_user.clear()
        self.__login_controller.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    filter = WheelEventFilter()
    app.installEventFilter(filter)
    window = EnduringChambers()
    sys.exit(app.exec())
