"""
Controller for DragAndDrop image items
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from niches.util.image_label_util import ImageLabelUtil
from niches.view.ui.main_window import Ui_MainWindow
from niches.constant.constants import ValidImageExtension, NOT_VALID_IMAGE
from niches.controller.error_controller import ErrorController

class DragAndDropCreateUtil(QWidget):
    def __init__(self, main_window:Ui_MainWindow):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Arrastra la imagen...")
        self.resize(400, 400)
        self.setAcceptDrops(True)
        self.__main_layout = QVBoxLayout()
        self.__image_label_util = ImageLabelUtil()
        self.__main_layout.addWidget(self.__image_label_util)
        self.setLayout(self.__main_layout)
        self.__file_path = None
        self.__error_controller = ErrorController()

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
            raise ValueError(NOT_VALID_IMAGE)

    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
            raise ValueError(NOT_VALID_IMAGE)

    def dropEvent(self, event):
        try:
            if event.mimeData().hasImage:
                event.setDropAction(Qt.CopyAction)
                file_path = event.mimeData().urls()[0].toLocalFile()
                split_file_path = file_path.rsplit("/")
                file =  split_file_path[-1]
                split_file = file.split(".")
                extension = split_file[-1].lower()
                if extension in ValidImageExtension:
                    pass
                else:
                    raise ValueError(NOT_VALID_IMAGE)
                self.set_image(file_path)
                event.accept()
            else:
                event.ignore()
                raise ValueError(NOT_VALID_IMAGE)

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

    def set_image(self, file_path):
        self.resize(400, 400)
        self.__file_path = file_path
        self.__image_label_util.set_pixmap(QPixmap(file_path).scaled(
            400, self.height(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))
        self.main_window.label_create_deceased_image.setPixmap(QPixmap(file_path).scaled(
            200, self.height(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))

    def get_file_path(self):
        return self.__file_path

    def open_window_configuration(self):
        self.__file_path = None
        self.__image_label_util.clear()
        self.__image_label_util.setText("\n\n Arrastra tu imagen aquí \n\n")
        self.main_window.label_create_deceased_image.clear()
        self.main_window.label_create_deceased_image.setText("Sin imagen")
