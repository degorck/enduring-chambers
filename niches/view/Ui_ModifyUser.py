# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ModifyUser.ui'
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

class Ui_ModifyUser(object):
    def setupUi(self, ModifyUser):
        if not ModifyUser.objectName():
            ModifyUser.setObjectName(u"ModifyUser")
        ModifyUser.resize(509, 298)
        self.horizontalLayoutWidget = QWidget(ModifyUser)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(140, 220, 239, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.push_button_save = QPushButton(self.horizontalLayoutWidget)
        self.push_button_save.setObjectName(u"push_button_save")

        self.horizontalLayout.addWidget(self.push_button_save)

        self.push_button_activate = QPushButton(self.horizontalLayoutWidget)
        self.push_button_activate.setObjectName(u"push_button_activate")

        self.horizontalLayout.addWidget(self.push_button_activate)

        self.push_button_deactivate = QPushButton(self.horizontalLayoutWidget)
        self.push_button_deactivate.setObjectName(u"push_button_deactivate")

        self.horizontalLayout.addWidget(self.push_button_deactivate)

        self.gridLayoutWidget = QWidget(ModifyUser)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(60, 40, 401, 164))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name = QLabel(self.gridLayoutWidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_name, 0, 0, 1, 1)

        self.label_maternal_surname = QLabel(self.gridLayoutWidget)
        self.label_maternal_surname.setObjectName(u"label_maternal_surname")
        self.label_maternal_surname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_maternal_surname, 2, 0, 1, 1)

        self.line_edit_paternal_surname = QLineEdit(self.gridLayoutWidget)
        self.line_edit_paternal_surname.setObjectName(u"line_edit_paternal_surname")

        self.gridLayout.addWidget(self.line_edit_paternal_surname, 1, 1, 1, 1)

        self.line_edit_maternal_surname = QLineEdit(self.gridLayoutWidget)
        self.line_edit_maternal_surname.setObjectName(u"line_edit_maternal_surname")

        self.gridLayout.addWidget(self.line_edit_maternal_surname, 2, 1, 1, 1)

        self.line_edit_name = QLineEdit(self.gridLayoutWidget)
        self.line_edit_name.setObjectName(u"line_edit_name")

        self.gridLayout.addWidget(self.line_edit_name, 0, 1, 1, 1)

        self.combo_box_user_type = QComboBox(self.gridLayoutWidget)
        self.combo_box_user_type.setObjectName(u"combo_box_user_type")

        self.gridLayout.addWidget(self.combo_box_user_type, 3, 1, 1, 1)

        self.label_user_type = QLabel(self.gridLayoutWidget)
        self.label_user_type.setObjectName(u"label_user_type")
        self.label_user_type.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_user_type, 3, 0, 1, 1)

        self.label_paternal_surname = QLabel(self.gridLayoutWidget)
        self.label_paternal_surname.setObjectName(u"label_paternal_surname")
        self.label_paternal_surname.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_paternal_surname, 1, 0, 1, 1)

        QWidget.setTabOrder(self.line_edit_name, self.line_edit_paternal_surname)
        QWidget.setTabOrder(self.line_edit_paternal_surname, self.line_edit_maternal_surname)
        QWidget.setTabOrder(self.line_edit_maternal_surname, self.combo_box_user_type)
        QWidget.setTabOrder(self.combo_box_user_type, self.push_button_save)
        QWidget.setTabOrder(self.push_button_save, self.push_button_activate)
        QWidget.setTabOrder(self.push_button_activate, self.push_button_deactivate)

        self.retranslateUi(ModifyUser)

        QMetaObject.connectSlotsByName(ModifyUser)
    # setupUi

    def retranslateUi(self, ModifyUser):
        ModifyUser.setWindowTitle(QCoreApplication.translate("ModifyUser", u"Modificaci\u00f3n de usuario", None))
        self.push_button_save.setText(QCoreApplication.translate("ModifyUser", u"Guardar", None))
        self.push_button_activate.setText(QCoreApplication.translate("ModifyUser", u"Alta", None))
        self.push_button_deactivate.setText(QCoreApplication.translate("ModifyUser", u"Baja", None))
        self.label_name.setText(QCoreApplication.translate("ModifyUser", u"Nombre:", None))
        self.label_maternal_surname.setText(QCoreApplication.translate("ModifyUser", u"Apellido Materno:", None))
        self.label_user_type.setText(QCoreApplication.translate("ModifyUser", u"Tipo de usuario:", None))
        self.label_paternal_surname.setText(QCoreApplication.translate("ModifyUser", u"Apellido Paterno:", None))
    # retranslateUi

