# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(283, 175)
        self.push_button_accept = QPushButton(Error)
        self.push_button_accept.setObjectName(u"push_button_accept")
        self.push_button_accept.setGeometry(QRect(100, 130, 75, 24))
        self.label_error_description = QLabel(Error)
        self.label_error_description.setObjectName(u"label_error_description")
        self.label_error_description.setGeometry(QRect(60, 50, 161, 51))
        self.label_error_description.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.push_button_accept.setText(QCoreApplication.translate("Error", u"Aceptar", None))
        self.label_error_description.setText(QCoreApplication.translate("Error", u"TextLabel", None))
    # retranslateUi

