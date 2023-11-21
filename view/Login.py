# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(283, 175)
        self.horizontalLayoutWidget = QWidget(Login)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(60, 110, 160, 41))
        self.horizontal_layout_buttons = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")
        self.horizontal_layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.push_button_login = QPushButton(self.horizontalLayoutWidget)
        self.push_button_login.setObjectName(u"push_button_login")

        self.horizontal_layout_buttons.addWidget(self.push_button_login)

        self.push_button_guest = QPushButton(self.horizontalLayoutWidget)
        self.push_button_guest.setObjectName(u"push_button_guest")

        self.horizontal_layout_buttons.addWidget(self.push_button_guest)

        self.gridLayoutWidget = QWidget(Login)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 19, 201, 81))
        self.grid_layout_form = QGridLayout(self.gridLayoutWidget)
        self.grid_layout_form.setObjectName(u"grid_layout_form")
        self.grid_layout_form.setContentsMargins(0, 0, 0, 0)
        self.label_user = QLabel(self.gridLayoutWidget)
        self.label_user.setObjectName(u"label_user")

        self.grid_layout_form.addWidget(self.label_user, 0, 0, 1, 1)

        self.label_password = QLabel(self.gridLayoutWidget)
        self.label_password.setObjectName(u"label_password")

        self.grid_layout_form.addWidget(self.label_password, 2, 0, 1, 1)

        self.line_edit_user = QLineEdit(self.gridLayoutWidget)
        self.line_edit_user.setObjectName(u"line_edit_user")

        self.grid_layout_form.addWidget(self.line_edit_user, 0, 1, 1, 1)

        self.line_edit_password = QLineEdit(self.gridLayoutWidget)
        self.line_edit_password.setObjectName(u"line_edit_password")
        self.line_edit_password.setCursor(QCursor(Qt.IBeamCursor))
        self.line_edit_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        self.grid_layout_form.addWidget(self.line_edit_password, 2, 1, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.push_button_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.push_button_guest.setText(QCoreApplication.translate("Login", u"Invitado", None))
        self.label_user.setText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.label_password.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
    # retranslateUi

