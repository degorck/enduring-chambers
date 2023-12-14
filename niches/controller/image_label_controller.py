"""
Label Image Module controller for drag and drop image
"""
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt

class ImageLabelController(QLabel):
    """
    Class that configures drag and drop label image
    """
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setMaximumSize(400, 400)
        self.setText("\n\n Arrastra tu imagen aquí \n\n")
        self.setStyleSheet(
            """
            QLabel{
                border: 2px dashed
            }
            """
        )

    def set_pixmap(self, image):
        """
        Set image on label image

        Arguments:
            image: QPixmap
                Image to be set on label
        """
        super().setPixmap(image)
