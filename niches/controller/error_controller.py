'''Module that controls error window'''
from PySide6 import QtWidgets
from niches.view.Ui_Error import Ui_Error

class ErrorController(QtWidgets.QWidget, Ui_Error):
    '''Class with error window functionality'''
    def __init__(self):
        super(ErrorController, self).__init__()
        self.setupUi(self)
        self.label_error_description.setText("")
        self.push_button_accept.clicked.connect(self.__hide_window)
    def handle_value_error(self, ve:ValueError):
        '''Loads value error on label_error_description'''
        self.label_error_description.setText(str(ve))
    def handle_exception_error(self, ex:Exception):
        '''Loads exception error on label_error_description'''
        self.label_error_description.setText(str(ex))
    def __hide_window(self):
        self.close()
        