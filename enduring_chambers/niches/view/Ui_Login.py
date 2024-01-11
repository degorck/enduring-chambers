# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import niches.view.enduring_chambers_initials_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(384, 457)
        Login.setMaximumSize(QSize(384, 457))
        icon = QIcon()
        icon.addFile(u":/icons/enduring_chambers_initials.ico", QSize(), QIcon.Normal, QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setStyleSheet(u"")
        self.gridLayout = QGridLayout(Login)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_user = QLabel(self.frame_2)
        self.label_user.setObjectName(u"label_user")

        self.verticalLayout.addWidget(self.label_user)

        self.line_edit_user = QLineEdit(self.frame_2)
        self.line_edit_user.setObjectName(u"line_edit_user")

        self.verticalLayout.addWidget(self.line_edit_user)

        self.label_password = QLabel(self.frame_2)
        self.label_password.setObjectName(u"label_password")

        self.verticalLayout.addWidget(self.label_password)

        self.line_edit_password = QLineEdit(self.frame_2)
        self.line_edit_password.setObjectName(u"line_edit_password")
        self.line_edit_password.setCursor(QCursor(Qt.IBeamCursor))
        self.line_edit_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.line_edit_password)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_3 = QFrame(Login)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setTextFormat(Qt.RichText)
        self.label.setPixmap(QPixmap(u":/icons/user.svg"))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)

        self.horizontal_layout_buttons = QHBoxLayout()
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")

        self.gridLayout.addLayout(self.horizontal_layout_buttons, 5, 0, 1, 1)

        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.push_button_login = QPushButton(self.frame)
        self.push_button_login.setObjectName(u"push_button_login")

        self.horizontalLayout.addWidget(self.push_button_login)

        self.push_button_guest = QPushButton(self.frame)
        self.push_button_guest.setObjectName(u"push_button_guest")

        self.horizontalLayout.addWidget(self.push_button_guest)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout.addWidget(self.frame, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 0, 1, 1)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_user.setText(QCoreApplication.translate("Login", u"Usuario:", None))
        self.label_password.setText(QCoreApplication.translate("Login", u"Contrase\u00f1a:", None))
        self.label.setText("")
        self.push_button_login.setText(QCoreApplication.translate("Login", u"Login", None))
        self.push_button_guest.setText(QCoreApplication.translate("Login", u"Invitado", None))
    # retranslateUi

