import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
import repackage
repackage.up()
from exception.Error import Ui_Error

class ErrorController(QtWidgets.QWidget, Ui_Error):
    def __init__(self):
        super(ErrorController, self).__init__()
        self.setupUi(self)
        self.label_error_description.setText("")
        self.push_button_accept.clicked.connect(self.hide_window)
    
    def handle_value_error(self, ve:ValueError):
        self.label_error_description.setText(str(ve))

    def handle_exception_error(self, ex:Exception):
        self.label_error_description.setText(str(ex))
    
    def hide_window(self):
        self.close()

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = ErrorController()
    window.show()
    sys.exit(app.exec())