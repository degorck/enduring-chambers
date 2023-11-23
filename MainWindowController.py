import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from Ui_MainWindow import Ui_MainWindow
from ErrorController import ErrorController
from CreateUserController import CreateUserController
from SearchUserController import SearchUserController

class MainWindowController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowController, self).__init__()
        self.setupUi(self)
        self.__create_user_controller = CreateUserController()
        self.__search_user_controller = SearchUserController()
        self.push_button_create_user.clicked.connect(self.__create_user_controller.show)
        self.push_button_search_users.clicked.connect(self.__search_user_controller.show)

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowController()
    window.show()
    sys.exit(app.exec())