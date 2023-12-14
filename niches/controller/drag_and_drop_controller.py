"""
Controller for DragAndDrop image items
"""
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from niches.controller.image_label_controller import ImageLabelController
from niches.view.ui.main_window import Ui_MainWindow
from niches.constant.constants import ValidImageExtension, NOT_VALID_IMAGE
from niches.controller.error_controller import ErrorController

class DragAndDropController(QWidget):
    def __init__(self, main_window:Ui_MainWindow):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Arrastra la imagen...")
        self.resize(400, 400)
        self.setAcceptDrops(True)
        main_layout = QVBoxLayout()
        self.photo_viewer = ImageLabelController()
        main_layout.addWidget(self.photo_viewer)
        self.setLayout(main_layout)
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
        self.photo_viewer.set_pixmap(QPixmap(file_path).scaled(
            400, self.height(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))
        self.main_window.label_create_deceased_image.setPixmap(QPixmap(file_path).scaled(
            200, self.height(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))

    def get_file_path(self):
        return self.__file_path

    def open_window_configuration(self):
        self.__file_path = None
        self.photo_viewer.clear()
        self.photo_viewer.setText("\n\n Arrastra tu imagen aquí \n\n")
        self.main_window.label_create_deceased_image.clear()
        self.main_window.label_create_deceased_image.setText("Sin imagen")
