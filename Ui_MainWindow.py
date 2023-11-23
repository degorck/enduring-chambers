# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 350)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.group_box_users = QGroupBox(self.centralwidget)
        self.group_box_users.setObjectName(u"group_box_users")
        self.group_box_users.setGeometry(QRect(40, 30, 151, 121))
        self.verticalLayoutWidget = QWidget(self.group_box_users)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 131, 86))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.push_button_create_user = QPushButton(self.verticalLayoutWidget)
        self.push_button_create_user.setObjectName(u"push_button_create_user")
        self.push_button_create_user.setEnabled(False)

        self.verticalLayout.addWidget(self.push_button_create_user)

        self.push_button_search_users = QPushButton(self.verticalLayoutWidget)
        self.push_button_search_users.setObjectName(u"push_button_search_users")
        self.push_button_search_users.setEnabled(False)

        self.verticalLayout.addWidget(self.push_button_search_users)

        self.group_box_holders = QGroupBox(self.centralwidget)
        self.group_box_holders.setObjectName(u"group_box_holders")
        self.group_box_holders.setGeometry(QRect(200, 30, 151, 121))
        self.verticalLayoutWidget_2 = QWidget(self.group_box_holders)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 131, 86))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.push_button_create_holder = QPushButton(self.verticalLayoutWidget_2)
        self.push_button_create_holder.setObjectName(u"push_button_create_holder")
        self.push_button_create_holder.setEnabled(False)

        self.verticalLayout_2.addWidget(self.push_button_create_holder)

        self.push_button_search_holders = QPushButton(self.verticalLayoutWidget_2)
        self.push_button_search_holders.setObjectName(u"push_button_search_holders")
        self.push_button_search_holders.setEnabled(False)

        self.verticalLayout_2.addWidget(self.push_button_search_holders)

        self.group_box_deceased = QGroupBox(self.centralwidget)
        self.group_box_deceased.setObjectName(u"group_box_deceased")
        self.group_box_deceased.setGeometry(QRect(40, 160, 151, 121))
        self.verticalLayoutWidget_3 = QWidget(self.group_box_deceased)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 131, 86))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.push_button_create_deceased = QPushButton(self.verticalLayoutWidget_3)
        self.push_button_create_deceased.setObjectName(u"push_button_create_deceased")
        self.push_button_create_deceased.setEnabled(False)

        self.verticalLayout_3.addWidget(self.push_button_create_deceased)

        self.push_button_search_deceased = QPushButton(self.verticalLayoutWidget_3)
        self.push_button_search_deceased.setObjectName(u"push_button_search_deceased")
        self.push_button_search_deceased.setEnabled(False)

        self.verticalLayout_3.addWidget(self.push_button_search_deceased)

        self.group_box_niches = QGroupBox(self.centralwidget)
        self.group_box_niches.setObjectName(u"group_box_niches")
        self.group_box_niches.setGeometry(QRect(200, 160, 151, 121))
        self.verticalLayoutWidget_4 = QWidget(self.group_box_niches)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 20, 131, 86))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.push_button_create_niche = QPushButton(self.verticalLayoutWidget_4)
        self.push_button_create_niche.setObjectName(u"push_button_create_niche")
        self.push_button_create_niche.setEnabled(False)

        self.verticalLayout_4.addWidget(self.push_button_create_niche)

        self.push_button_search_niches = QPushButton(self.verticalLayoutWidget_4)
        self.push_button_search_niches.setObjectName(u"push_button_search_niches")
        self.push_button_search_niches.setEnabled(False)

        self.verticalLayout_4.addWidget(self.push_button_search_niches)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 407, 22))
        self.menuConfiguraci_n = QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuConfiguraci_n.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pantalla Principal", None))
        self.group_box_users.setTitle(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.push_button_create_user.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.push_button_search_users.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda", None))
        self.group_box_holders.setTitle(QCoreApplication.translate("MainWindow", u"Titulares", None))
        self.push_button_create_holder.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.push_button_search_holders.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda", None))
        self.group_box_deceased.setTitle(QCoreApplication.translate("MainWindow", u"Fallecidos", None))
        self.push_button_create_deceased.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.push_button_search_deceased.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda", None))
        self.group_box_niches.setTitle(QCoreApplication.translate("MainWindow", u"Nichos", None))
        self.push_button_create_niche.setText(QCoreApplication.translate("MainWindow", u"Alta", None))
        self.push_button_search_niches.setText(QCoreApplication.translate("MainWindow", u"B\u00fasqueda", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("MainWindow", u"Configuraci\u00f3n", None))
    # retranslateUi

