import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from niches.view.Ui_MainWindow import Ui_MainWindow
from niches.controller.ErrorController import ErrorController
from niches.controller.CreateUserController import CreateUserController
from niches.controller.SearchUserController import SearchUserController
from niches.controller.LoginController import LoginController
from niches.util.Constants import UserTypeKey

class MainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.setupUi(self)
        self.__user_type_key = UserTypeKey.GUEST
        self.__login_controller = LoginController()
        self.__create_user_controller = CreateUserController()
        self.__search_user_controller = SearchUserController()
        self.push_button_create_user.clicked.connect(self.__create_user_controller.show)
        self.push_button_search_users.clicked.connect(self.__search_user_controller.show)
        self.__login_controller.push_button_login.clicked.connect(self.configure_windows_by_user_type)
        self.__login_controller.push_button_guest.clicked.connect(self.configure_windows_by_user_type)
        self.show()
        self.__login_controller.show()
    
    def configure_windows_by_user_type(self):
        self.__user_type_key = self.__login_controller.get_logged_user_type_key()
        match self.__user_type_key:
            case UserTypeKey.GUEST:
                self.__configure_guest_window()
                print(self.__user_type_key)
            case UserTypeKey.ADMINISTRATOR():
                self.__configure_administrator_window()
                print(self.__user_type_key)
            case UserTypeKey.CAPTURIST():
                self.__configure_capturist_window()
                print(self.__user_type_key)

        for user_type_key in UserTypeKey:
            print(user_type_key)  
        
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
        self.push_button_search_users.setEnabled(False)
        self.push_button_create_holder.setEnabled(False)
        self.push_button_search_holders.setEnabled(False)
        self.push_button_create_deceased.setEnabled(False)
        self.push_button_search_deceased.setEnabled(False)
        self.push_button_create_niche.setEnabled(False)
        self.push_button_search_niches.setEnabled(False)

    def __configure_administrator_window(self):
        self.push_button_create_user.setEnabled(False)
        self.push_button_search_users.setEnabled(False)
        self.push_button_create_holder.setEnabled(False)
        self.push_button_search_holders.setEnabled(False)
        self.push_button_create_deceased.setEnabled(False)
        self.push_button_search_deceased.setEnabled(False)
        self.push_button_create_niche.setEnabled(False)
        self.push_button_search_niches.setEnabled(False)

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowController()
    sys.exit(app.exec())