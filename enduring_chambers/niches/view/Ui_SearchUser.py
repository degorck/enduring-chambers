# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SearchUser.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_SearchUser(object):
    def setupUi(self, SearchUser):
        if not SearchUser.objectName():
            SearchUser.setObjectName(u"SearchUser")
        SearchUser.resize(540, 369)
        self.centralwidget = QWidget(SearchUser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.line_edit_search = QLineEdit(self.centralwidget)
        self.line_edit_search.setObjectName(u"line_edit_search")
        self.line_edit_search.setGeometry(QRect(90, 10, 391, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 40, 49, 16))
        self.list_widget_users = QListWidget(self.centralwidget)
        self.list_widget_users.setObjectName(u"list_widget_users")
        self.list_widget_users.setGeometry(QRect(90, 60, 391, 261))
        self.table_widget_users = QTableWidget(self.centralwidget)
        self.table_widget_users.setObjectName(u"table_widget_users")
        self.table_widget_users.setGeometry(QRect(90, 60, 391, 261))
        SearchUser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SearchUser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        SearchUser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SearchUser)
        self.statusbar.setObjectName(u"statusbar")
        SearchUser.setStatusBar(self.statusbar)

        self.retranslateUi(SearchUser)

        QMetaObject.connectSlotsByName(SearchUser)
    # setupUi

    def retranslateUi(self, SearchUser):
        SearchUser.setWindowTitle(QCoreApplication.translate("SearchUser", u"B\u00fasqueda de usuario", None))
        self.label.setText(QCoreApplication.translate("SearchUser", u"Buscar: ", None))
        self.label_2.setText(QCoreApplication.translate("SearchUser", u"Usuarios:", None))
    # retranslateUi

