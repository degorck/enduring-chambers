"""
Module that controls the MainWindow
"""
import sys
from PySide6 import QtWidgets
from niches.view.ui.main_window import Ui_MainWindow
from niches.service.user_service import UserService
from niches.util.LoggingConfiguration import get_loging
logging = get_loging()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Class with the functionality of MainWindow

    Args:
        QtWidgets (QtWidgets.QMainWindow): Core QMainWindow
        Ui_MainWindow (Ui_MainWindow): Qt layer transformed to python code 
    """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.__user_service = UserService()
        logging.debug("System started")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
