import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from niches.view.Ui_MainWindow import Ui_MainWindow
from niches.controller.ErrorController import ErrorController
from niches.controller.CreateUserController import CreateUserController
from niches.controller.SearchUserController import SearchUserController
from niches.controller.LoginController import LoginController
from niches.util.Constants import UserTypeKey
from niches.util.LoggingConfiguration import get_loging

logging = get_loging()

class MainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.setupUi(self)
        self.__user_type_key = UserTypeKey.NOT_LOGGED.value
        self.__login_controller = LoginController()
        self.__create_user_controller = CreateUserController()
        self.__search_user_controller = SearchUserController()
        self.push_button_create_user.clicked.connect(self.__create_user_controller.show)
        self.push_button_search_users.clicked.connect(self.__search_user_controller.show)
        self.__login_controller.push_button_login.clicked.connect(self.__configure_windows_by_user_type)
        self.__login_controller.line_edit_password.returnPressed.connect(self.__configure_windows_by_user_type)
        self.__login_controller.push_button_guest.clicked.connect(self.__configure_windows_by_user_type)
        self.show()
        self.__login_controller.show()
        logging.info("System started")
    
    def __configure_windows_by_user_type(self):
        self.__user_type_key = self.__login_controller.get_logged_user_type_key()
        match self.__user_type_key:
            case UserTypeKey.GUEST.value:
                self.__configure_guest_window()

            case UserTypeKey.ADMINISTRATOR.value:
                self.__configure_administrator_window()

            case UserTypeKey.CAPTURIST.value:
                self.__configure_capturist_window()

            case UserTypeKey.NOT_LOGGED.value:
                self.__configure_not_logged_window()

        
    def __configure_guest_window(self):
        self.push_button_create_user.setEnabled(False)
        self.push_button_search_users.setEnabled(True)
        self.push_button_create_holder.setEnabled(False)
        self.push_button_search_holders.setEnabled(True)
        self.push_button_create_deceased.setEnabled(False)
        self.push_button_search_deceased.setEnabled(True)
        self.push_button_create_niche.setEnabled(False)
        self.push_button_search_niches.setEnabled(True)

    def __configure_capturist_window(self):
        self.push_button_create_user.setEnabled(False)
        self.push_button_search_users.setEnabled(True)
        self.push_button_create_holder.setEnabled(True)
        self.push_button_search_holders.setEnabled(True)
        self.push_button_create_deceased.setEnabled(True)
        self.push_button_search_deceased.setEnabled(True)
        self.push_button_create_niche.setEnabled(True)
        self.push_button_search_niches.setEnabled(True)

    def __configure_administrator_window(self):
        self.push_button_create_user.setEnabled(True)
        self.push_button_search_users.setEnabled(True)
        self.push_button_create_holder.setEnabled(True)
        self.push_button_search_holders.setEnabled(True)
        self.push_button_create_deceased.setEnabled(True)
        self.push_button_search_deceased.setEnabled(True)
        self.push_button_create_niche.setEnabled(True)
        self.push_button_search_niches.setEnabled(True)
    
    def __configure_not_logged_window(self):
        self.push_button_create_user.setEnabled(False)
        self.push_button_search_users.setEnabled(False)
        self.push_button_create_holder.setEnabled(False)
        self.push_button_search_holders.setEnabled(False)
        self.push_button_create_deceased.setEnabled(False)
        self.push_button_search_deceased.setEnabled(False)
        self.push_button_create_niche.setEnabled(False)
        self.push_button_search_niches.setEnabled(False)

    def get_logged_user_type_key(self):
        return self.__user_type_key

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowController()
    sys.exit(app.exec())