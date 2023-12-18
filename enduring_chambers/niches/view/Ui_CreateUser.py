# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUser.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_CreateUser(object):
    def setupUi(self, CreateUser):
        if not CreateUser.objectName():
            CreateUser.setObjectName(u"CreateUser")
        CreateUser.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(CreateUser)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 220, 160, 41))
        self.horizontal_layout_buttons = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontal_layout_buttons.setObjectName(u"horizontal_layout_buttons")
        self.horizontal_layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.push_button_clean = QPushButton(self.horizontalLayoutWidget)
        self.push_button_clean.setObjectName(u"push_button_clean")

        self.horizontal_layout_buttons.addWidget(self.push_button_clean)

        self.push_button_save = QPushButton(self.horizontalLayoutWidget)
        self.push_button_save.setObjectName(u"push_button_save")

        self.horizontal_layout_buttons.addWidget(self.push_button_save)

        self.gridLayoutWidget = QWidget(CreateUser)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 20, 261, 192))
        self.grid_layout_form = QGridLayout(self.gridLayoutWidget)
        self.grid_layout_form.setObjectName(u"grid_layout_form")
        self.grid_layout_form.setContentsMargins(0, 0, 0, 0)
        self.line_edit_paternal_surname = QLineEdit(self.gridLayoutWidget)
        self.line_edit_paternal_surname.setObjectName(u"line_edit_paternal_surname")

        self.grid_layout_form.addWidget(self.line_edit_paternal_surname, 1, 1, 1, 1)

        self.label_paternal_surname = QLabel(self.gridLayoutWidget)
        self.label_paternal_surname.setObjectName(u"label_paternal_surname")
        self.label_paternal_surname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_paternal_surname, 1, 0, 1, 1)

        self.label_password = QLabel(self.gridLayoutWidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_password, 5, 0, 1, 1)

        self.line_edit_name = QLineEdit(self.gridLayoutWidget)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.grid_layout_form.addWidget(self.line_edit_name, 0, 1, 1, 1)

        self.label_user_type = QLabel(self.gridLayoutWidget)
        self.label_user_type.setObjectName(u"label_user_type")
        self.label_user_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_user_type, 3, 0, 1, 1)

        self.label_name = QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_name, 0, 0, 1, 1)

        self.label_maternal_surname = QLabel(self.gridLayoutWidget)
        self.label_maternal_surname.setObjectName(u"label_maternal_surname")
        self.label_maternal_surname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_maternal_surname, 2, 0, 1, 1)

        self.label_repeat_password = QLabel(self.gridLayoutWidget)
        self.label_repeat_password.setObjectName(u"label_repeat_password")
        self.label_repeat_password.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_repeat_password, 6, 0, 1, 1)

        self.line_edit_password = QLineEdit(self.gridLayoutWidget)
        self.line_edit_password.setObjectName(u"line_edit_password")
        self.line_edit_password.setEchoMode(QLineEdit.Password)

        self.grid_layout_form.addWidget(self.line_edit_password, 5, 1, 1, 1)

        self.line_edit_maternal_surname = QLineEdit(self.gridLayoutWidget)
        self.line_edit_maternal_surname.setObjectName(u"line_edit_maternal_surname")

        self.grid_layout_form.addWidget(self.line_edit_maternal_surname, 2, 1, 1, 1)

        self.combo_box_user_type = QComboBox(self.gridLayoutWidget)
        self.combo_box_user_type.setObjectName(u"combo_box_user_type")

        self.grid_layout_form.addWidget(self.combo_box_user_type, 3, 1, 1, 1)

        self.line_edit_repeat_password = QLineEdit(self.gridLayoutWidget)
        self.line_edit_repeat_password.setObjectName(u"line_edit_repeat_password")
        self.line_edit_repeat_password.setEchoMode(QLineEdit.Password)

        self.grid_layout_form.addWidget(self.line_edit_repeat_password, 6, 1, 1, 1)

        self.label_user_name = QLabel(self.gridLayoutWidget)
        self.label_user_name.setObjectName(u"label_user_name")
        self.label_user_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.grid_layout_form.addWidget(self.label_user_name, 4, 0, 1, 1)

        self.line_edit_user_name = QLineEdit(self.gridLayoutWidget)
        self.line_edit_user_name.setObjectName(u"line_edit_user_name")

        self.grid_layout_form.addWidget(self.line_edit_user_name, 4, 1, 1, 1)

        QWidget.setTabOrder(self.line_edit_name, self.line_edit_paternal_surname)
        QWidget.setTabOrder(self.line_edit_paternal_surname, self.line_edit_maternal_surname)
        QWidget.setTabOrder(self.line_edit_maternal_surname, self.combo_box_user_type)
        QWidget.setTabOrder(self.combo_box_user_type, self.line_edit_user_name)
        QWidget.setTabOrder(self.line_edit_user_name, self.line_edit_password)
        QWidget.setTabOrder(self.line_edit_password, self.line_edit_repeat_password)
        QWidget.setTabOrder(self.line_edit_repeat_password, self.push_button_clean)
        QWidget.setTabOrder(self.push_button_clean, self.push_button_save)

        self.retranslateUi(CreateUser)

        QMetaObject.connectSlotsByName(CreateUser)
    # setupUi

    def retranslateUi(self, CreateUser):
        CreateUser.setWindowTitle(QCoreApplication.translate("CreateUser", u"Creaci\u00f3n de usuario", None))
        self.push_button_clean.setText(QCoreApplication.translate("CreateUser", u"Limpiar", None))
        self.push_button_save.setText(QCoreApplication.translate("CreateUser", u"Guardar", None))
        self.label_paternal_surname.setText(QCoreApplication.translate("CreateUser", u"Apellido Paterno:", None))
        self.label_password.setText(QCoreApplication.translate("CreateUser", u"Contrase\u00f1a: ", None))
        self.label_user_type.setText(QCoreApplication.translate("CreateUser", u"Tipo de usuario:", None))
        self.label_name.setText(QCoreApplication.translate("CreateUser", u"Nombre:", None))
        self.label_maternal_surname.setText(QCoreApplication.translate("CreateUser", u"Apellido Materno:", None))
        self.label_repeat_password.setText(QCoreApplication.translate("CreateUser", u"Repetir Contrase\u00f1a:", None))
        self.label_user_name.setText(QCoreApplication.translate("CreateUser", u"Nombre de usuario:", None))
    # retranslateUi

