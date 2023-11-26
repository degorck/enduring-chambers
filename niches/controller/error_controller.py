"""
    Module that controls Error widget.
"""
from PySide6 import QtWidgets
from niches.view.Ui_Error import Ui_Error

class ErrorController(QtWidgets.QWidget, Ui_Error):
    """
    Class with the functionality of Error widget

    Args:
        QtWidgets (QtWidgets.QWidget): Core QWidget
        Ui_Error (Ui_Error): Qt layer transformed to python code 
    """
    def __init__(self):
        super(ErrorController, self).__init__()
        self.setupUi(self)
        self.label_error_description.setText("")
        self.push_button_accept.clicked.connect(self.__hide_window)

    def handle_value_error(self, ve:ValueError):
        """
        Set label_error_description text with ValueError details
        """
        self.label_error_description.setText(str(ve))

    def handle_exception_error(self, ex:Exception):
        """
        Set label_error_description text with Exception details
        """
        self.label_error_description.setText(str(ex))

    def __hide_window(self):
        self.close()
        