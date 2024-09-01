# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)
import niches.view.enduring_chambers_initials_rc

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(283, 175)
        Error.setMaximumSize(QSize(283, 175))
        icon = QIcon()
        icon.addFile(u":/icons/enduring_chambers_initials.ico", QSize(), QIcon.Normal, QIcon.Off)
        Error.setWindowIcon(icon)
        Error.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Error)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.push_button_accept = QPushButton(Error)
        self.push_button_accept.setObjectName(u"push_button_accept")

        self.gridLayout.addWidget(self.push_button_accept, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.label_error_description = QLabel(Error)
        self.label_error_description.setObjectName(u"label_error_description")
        self.label_error_description.setAlignment(Qt.AlignCenter)
        self.label_error_description.setWordWrap(True)

        self.gridLayout.addWidget(self.label_error_description, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)


        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.push_button_accept.setText(QCoreApplication.translate("Error", u"Aceptar", None))
        self.label_error_description.setText(QCoreApplication.translate("Error", u"TextLabel", None))
    # retranslateUi

