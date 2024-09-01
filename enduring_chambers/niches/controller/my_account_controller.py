"""
MyAccount Controller Module
"""
from niches.util.logging_configuration import get_loging
from niches.model.dto.user_dto import UserDto
from niches.view.ui.main_window import Ui_MainWindow
from niches.util.validator import validate_is_not_empty, validate_password
from niches.constant.constants import FieldName
from niches.service.user_service import UserService
from niches.util.encryptor import Encryptor
from niches.controller.error_controller import ErrorController
logging = get_loging()

class MyAccountController:
    """
    My Account controller class
    
    Arguments:
        main_window : Ui_MainWindow
            Reuses the main_main window to add the configuration of this class
    """
    def __init__(self, main_window:Ui_MainWindow):
        self.main_window = main_window
        self.__user_service = UserService()
        self.__encryptor = Encryptor()
        self.__error_controller = ErrorController()
        self.__configure_actions()
        logging.debug("My account controller created")

    def __configure_actions(self):
        self.main_window.push_button_my_account.clicked.connect(
            self.__set_stacked_widget_my_account)
        self.main_window.push_button_change_password.clicked.connect(self.__change_password)
        logging.debug("My account controller actions configured")

    def __set_stacked_widget_my_account(self):
        self.main_window.push_button_deceased.setChecked(False)
        self.main_window.push_button_holders.setChecked(False)
        self.main_window.push_button_my_account.setChecked(True)
        self.main_window.push_button_niches.setChecked(False)
        self.main_window.push_button_users.setChecked(False)
        self.main_window.push_button_payments.setChecked(False)
        self.main_window.stacked_widget.setCurrentIndex(5)
        logging.debug("My account stacked widget selected")

    def __change_password(self):
        try:
            validate_is_not_empty(self.main_window.line_edit_my_account_current_password.text(),
                                                   FieldName.PASSWORD)
            validate_password(self.main_window.line_edit_my_account_new_password.text(),
                              self.main_window.line_edit_my_account_repeat_new_password.text())
            user_dto = UserDto()
            user_dto = self.__user_service.find_user_by_user_name(
                self.main_window.get_logged_user_dto().get_user_name())
            if (user_dto.get_user_name() == self.main_window.get_logged_user_dto().get_user_name()
                and
                self.__encryptor.check_password(
                    self.main_window.line_edit_my_account_current_password.text(),
                    self.main_window.get_logged_user_dto().get_password())
                and user_dto is not None):
                self.__user_service.change_password(
                    self.main_window.get_logged_user_dto().get_user_name(),
                    self.main_window.line_edit_my_account_new_password.text())
                user_dto = self.__user_service.find_user_by_user_name(
                    self.main_window.get_logged_user_dto().get_user_name())
                self.main_window.get_logged_user_dto().set_password(user_dto.get_password())
                self.__clean_change_password()
                logging.debug("Password changed")
                self.__error_controller.handle_exception_error("Contraseña actualizada")
                self.__error_controller.show()
            else:
                self.__error_controller.handle_exception_error("Contraseña actual inválida")
                self.__error_controller.show()
            logging.debug("Password changed")

        except ValueError as ve:
            logging.exception(ve)
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except TypeError as e:
            logging.exception(e)
            self.__error_controller.handle_exception_error("El usuario no existe")
            self.__error_controller.show()

        except Exception as e:
            logging.exception(e)
            self.__error_controller.handle_exception_error("El usuario no existe")
            self.__error_controller.show()

    def __clean_change_password(self):
        self.main_window.line_edit_my_account_current_password.clear()
        self.main_window.line_edit_my_account_new_password.clear()
        self.main_window.line_edit_my_account_repeat_new_password.clear()
        logging.debug("Password cleaned")
