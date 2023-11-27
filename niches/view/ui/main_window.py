# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QGraphicsView, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QStatusBar,
    QTableView, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 631)
        MainWindow.setMinimumSize(QSize(650, 500))
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_9 = QFrame(self.centralwidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(100, 0))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_welcome = QLabel(self.frame_9)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_welcome)

        self.label_welcome_user_name = QLabel(self.frame_9)
        self.label_welcome_user_name.setObjectName(u"label_welcome_user_name")
        self.label_welcome_user_name.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	padding: 8px 8px;\n"
"	border-radius: 10px;\n"
"}")
        self.label_welcome_user_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_welcome_user_name)

        self.push_button_users = QPushButton(self.frame_9)
        self.push_button_users.setObjectName(u"push_button_users")
        font = QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.push_button_users.setFont(font)
        self.push_button_users.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.push_button_users.setAcceptDrops(False)
        self.push_button_users.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u"C:/Users/small/Downloads/feather/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.push_button_users.setIcon(icon)
        self.push_button_users.setIconSize(QSize(20, 20))
        self.push_button_users.setCheckable(True)
        self.push_button_users.setAutoDefault(False)
        self.push_button_users.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_users)

        self.push_button_deceased = QPushButton(self.frame_9)
        self.push_button_deceased.setObjectName(u"push_button_deceased")
        self.push_button_deceased.setLayoutDirection(Qt.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u"C:/Users/small/Downloads/feather/user-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.push_button_deceased.setIcon(icon1)
        self.push_button_deceased.setIconSize(QSize(20, 20))
        self.push_button_deceased.setCheckable(True)
        self.push_button_deceased.setAutoDefault(False)
        self.push_button_deceased.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_deceased)

        self.push_button_holders = QPushButton(self.frame_9)
        self.push_button_holders.setObjectName(u"push_button_holders")
        self.push_button_holders.setLayoutDirection(Qt.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u"C:/Users/small/Downloads/feather/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.push_button_holders.setIcon(icon2)
        self.push_button_holders.setIconSize(QSize(20, 20))
        self.push_button_holders.setCheckable(True)
        self.push_button_holders.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_holders)

        self.push_button_niches = QPushButton(self.frame_9)
        self.push_button_niches.setObjectName(u"push_button_niches")
        self.push_button_niches.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u"C:/Users/small/Downloads/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.push_button_niches.setIcon(icon3)
        self.push_button_niches.setIconSize(QSize(20, 20))
        self.push_button_niches.setCheckable(True)
        self.push_button_niches.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_niches)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.push_button_my_account = QPushButton(self.frame_9)
        self.push_button_my_account.setObjectName(u"push_button_my_account")
        self.push_button_my_account.setLayoutDirection(Qt.RightToLeft)
        self.push_button_my_account.setAutoFillBackground(False)
        icon4 = QIcon()
        icon4.addFile(u"C:/Users/small/Downloads/feather/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.push_button_my_account.setIcon(icon4)
        self.push_button_my_account.setIconSize(QSize(20, 20))
        self.push_button_my_account.setCheckable(True)
        self.push_button_my_account.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_my_account)


        self.gridLayout.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setAutoFillBackground(False)
        self.stacked_widget.setFrameShape(QFrame.NoFrame)
        self.stacked_widget.setFrameShadow(QFrame.Plain)
        self.unselected = QWidget()
        self.unselected.setObjectName(u"unselected")
        self.gridLayout_14 = QGridLayout(self.unselected)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_25 = QFrame(self.unselected)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_26 = QLabel(self.frame_25)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_22.addWidget(self.label_26)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)


        self.gridLayout_14.addWidget(self.frame_25, 0, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.stacked_widget.addWidget(self.unselected)
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.gridLayout_3 = QGridLayout(self.users)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scroll_area_create_user = QScrollArea(self.users)
        self.scroll_area_create_user.setObjectName(u"scroll_area_create_user")
        self.scroll_area_create_user.setEnabled(True)
        self.scroll_area_create_user.setMinimumSize(QSize(200, 0))
        self.scroll_area_create_user.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_create_user.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 194, 466))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_create_user = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user.setObjectName(u"label_create_user")
        self.label_create_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_create_user)

        self.horizontal_spacer_create_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.horizontal_spacer_create_user)

        self.label_create_user_name = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_name.setObjectName(u"label_create_user_name")
        self.label_create_user_name.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_create_user_name)

        self.line_edit_create_user_name = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_name.setObjectName(u"line_edit_create_user_name")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_name)

        self.label_create_user_paternal_surname = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_paternal_surname.setObjectName(u"label_create_user_paternal_surname")

        self.verticalLayout_2.addWidget(self.label_create_user_paternal_surname)

        self.line_edit_create_user_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_paternal_surname.setObjectName(u"line_edit_create_user_paternal_surname")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_paternal_surname)

        self.label_create_user_maternal_surname = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_maternal_surname.setObjectName(u"label_create_user_maternal_surname")

        self.verticalLayout_2.addWidget(self.label_create_user_maternal_surname)

        self.line_edit_create_user_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_maternal_surname.setObjectName(u"line_edit_create_user_maternal_surname")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_maternal_surname)

        self.label_create_user_user_name = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_user_name.setObjectName(u"label_create_user_user_name")

        self.verticalLayout_2.addWidget(self.label_create_user_user_name)

        self.line_edit_create_user_user_name = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_user_name.setObjectName(u"line_edit_create_user_user_name")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_user_name)

        self.label_create_user_password = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_password.setObjectName(u"label_create_user_password")

        self.verticalLayout_2.addWidget(self.label_create_user_password)

        self.line_edit_create_user_password = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_password.setObjectName(u"line_edit_create_user_password")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_password)

        self.label_create_user_repeat_password = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_repeat_password.setObjectName(u"label_create_user_repeat_password")

        self.verticalLayout_2.addWidget(self.label_create_user_repeat_password)

        self.line_edit_create_user_repeat_password = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_repeat_password.setObjectName(u"line_edit_create_user_repeat_password")

        self.verticalLayout_2.addWidget(self.line_edit_create_user_repeat_password)

        self.label_create_user_user_type = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_user_type.setObjectName(u"label_create_user_user_type")

        self.verticalLayout_2.addWidget(self.label_create_user_user_type)

        self.combo_box_create_user_user_type = QComboBox(self.scrollAreaWidgetContents_3)
        self.combo_box_create_user_user_type.setObjectName(u"combo_box_create_user_user_type")

        self.verticalLayout_2.addWidget(self.combo_box_create_user_user_type)

        self.vertical_spacer_create_user = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.vertical_spacer_create_user)

        self.frame_create_user = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_create_user.setObjectName(u"frame_create_user")
        self.frame_create_user.setFrameShape(QFrame.StyledPanel)
        self.frame_create_user.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_create_user)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.push_button_create_user_save_user = QPushButton(self.frame_create_user)
        self.push_button_create_user_save_user.setObjectName(u"push_button_create_user_save_user")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.push_button_create_user_save_user)

        self.push_button_create_user_clean_user = QPushButton(self.frame_create_user)
        self.push_button_create_user_clean_user.setObjectName(u"push_button_create_user_clean_user")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.push_button_create_user_clean_user)


        self.verticalLayout_2.addWidget(self.frame_create_user)

        self.scroll_area_create_user.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scroll_area_create_user, 1, 1, 1, 1)

        self.scroll_area_modify_user = QScrollArea(self.users)
        self.scroll_area_modify_user.setObjectName(u"scroll_area_modify_user")
        self.scroll_area_modify_user.setMinimumSize(QSize(200, 0))
        self.scroll_area_modify_user.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_modify_user.setWidgetResizable(True)
        self.scroll_area_modify_user.setAlignment(Qt.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 194, 346))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_modify_user = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user.setObjectName(u"label_modify_user")
        self.label_modify_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_modify_user)

        self.horizontal_spacer_modify_user = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.horizontal_spacer_modify_user)

        self.label_modify_user_name = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user_name.setObjectName(u"label_modify_user_name")

        self.verticalLayout.addWidget(self.label_modify_user_name)

        self.line_edit_modify_user_name = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_modify_user_name.setObjectName(u"line_edit_modify_user_name")

        self.verticalLayout.addWidget(self.line_edit_modify_user_name)

        self.label_modify_user_paternal_surname = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user_paternal_surname.setObjectName(u"label_modify_user_paternal_surname")

        self.verticalLayout.addWidget(self.label_modify_user_paternal_surname)

        self.line_edit_modify_user_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_modify_user_paternal_surname.setObjectName(u"line_edit_modify_user_paternal_surname")

        self.verticalLayout.addWidget(self.line_edit_modify_user_paternal_surname)

        self.label_modify_user_maternal_surname = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user_maternal_surname.setObjectName(u"label_modify_user_maternal_surname")

        self.verticalLayout.addWidget(self.label_modify_user_maternal_surname)

        self.line_edit_modify_user_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_2)
        self.line_edit_modify_user_maternal_surname.setObjectName(u"line_edit_modify_user_maternal_surname")

        self.verticalLayout.addWidget(self.line_edit_modify_user_maternal_surname)

        self.label_modify_user_user_type = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user_user_type.setObjectName(u"label_modify_user_user_type")

        self.verticalLayout.addWidget(self.label_modify_user_user_type)

        self.combo_box_modify_user_user_type = QComboBox(self.scrollAreaWidgetContents_2)
        self.combo_box_modify_user_user_type.setObjectName(u"combo_box_modify_user_user_type")

        self.verticalLayout.addWidget(self.combo_box_modify_user_user_type)

        self.vertical_spacer_modify_user = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.vertical_spacer_modify_user)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.push_button_modify_user_activate = QPushButton(self.frame_2)
        self.push_button_modify_user_activate.setObjectName(u"push_button_modify_user_activate")

        self.horizontalLayout_6.addWidget(self.push_button_modify_user_activate)

        self.push_button_modify_user_deactivate = QPushButton(self.frame_2)
        self.push_button_modify_user_deactivate.setObjectName(u"push_button_modify_user_deactivate")

        self.horizontalLayout_6.addWidget(self.push_button_modify_user_deactivate)


        self.verticalLayout.addWidget(self.frame_2)

        self.push_button_modify_user_save = QPushButton(self.scrollAreaWidgetContents_2)
        self.push_button_modify_user_save.setObjectName(u"push_button_modify_user_save")

        self.verticalLayout.addWidget(self.push_button_modify_user_save)

        self.scroll_area_modify_user.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scroll_area_modify_user, 1, 2, 1, 1)

        self.scroll_area_users = QScrollArea(self.users)
        self.scroll_area_users.setObjectName(u"scroll_area_users")
        self.scroll_area_users.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 124, 117))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_widget_users = QTableWidget(self.scrollAreaWidgetContents_4)
        self.table_widget_users.setObjectName(u"table_widget_users")

        self.gridLayout_2.addWidget(self.table_widget_users, 1, 0, 1, 2)

        self.line_edit_search_users = QLineEdit(self.scrollAreaWidgetContents_4)
        self.line_edit_search_users.setObjectName(u"line_edit_search_users")

        self.gridLayout_2.addWidget(self.line_edit_search_users, 0, 1, 1, 1)

        self.label_search_users = QLabel(self.scrollAreaWidgetContents_4)
        self.label_search_users.setObjectName(u"label_search_users")

        self.gridLayout_2.addWidget(self.label_search_users, 0, 0, 1, 1)

        self.scroll_area_users.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_3.addWidget(self.scroll_area_users, 1, 0, 1, 1)

        self.frame = QFrame(self.users)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_users = QLabel(self.frame)
        self.label_users.setObjectName(u"label_users")

        self.horizontalLayout.addWidget(self.label_users)

        self.horizontal_spacer_users_title = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_users_title)

        self.push_button_create_user_create = QPushButton(self.frame)
        self.push_button_create_user_create.setObjectName(u"push_button_create_user_create")

        self.horizontalLayout.addWidget(self.push_button_create_user_create)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.users)
        self.deceased = QWidget()
        self.deceased.setObjectName(u"deceased")
        self.gridLayout_11 = QGridLayout(self.deceased)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_16 = QFrame(self.deceased)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.pushButton_22 = QPushButton(self.frame_16)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_13.addWidget(self.pushButton_22)


        self.gridLayout_11.addWidget(self.frame_16, 0, 0, 1, 3)

        self.scrollArea_10 = QScrollArea(self.deceased)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 124, 117))
        self.formLayout_11 = QFormLayout(self.scrollAreaWidgetContents_20)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents_20)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.lineEdit_13)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_20)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.tableView_4 = QTableView(self.scrollAreaWidgetContents_20)
        self.tableView_4.setObjectName(u"tableView_4")

        self.formLayout_11.setWidget(1, QFormLayout.SpanningRole, self.tableView_4)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_20)

        self.gridLayout_11.addWidget(self.scrollArea_10, 1, 0, 1, 1)

        self.scrollArea_12 = QScrollArea(self.deceased)
        self.scrollArea_12.setObjectName(u"scrollArea_12")
        self.scrollArea_12.setMinimumSize(QSize(200, 0))
        self.scrollArea_12.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_12.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 194, 466))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_22)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.horizontalSpacer_5)

        self.label_6 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_14.addWidget(self.label_6)

        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_22)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_14.addWidget(self.lineEdit_4)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_14.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_22)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_14.addWidget(self.lineEdit_5)

        self.label_14 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_14.addWidget(self.label_14)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_22)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_14.addWidget(self.lineEdit_6)

        self.label_16 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_14.addWidget(self.label_16)

        self.dateEdit = QDateEdit(self.scrollAreaWidgetContents_22)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout_14.addWidget(self.dateEdit)

        self.label_17 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_14.addWidget(self.label_17)

        self.dateEdit_2 = QDateEdit(self.scrollAreaWidgetContents_22)
        self.dateEdit_2.setObjectName(u"dateEdit_2")

        self.verticalLayout_14.addWidget(self.dateEdit_2)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_14.addWidget(self.label_15)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_22)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_14.addWidget(self.comboBox)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_22)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_14.addWidget(self.label_18)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_22)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout_14.addWidget(self.comboBox_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_25 = QPushButton(self.frame_18)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_15.addWidget(self.pushButton_25)

        self.pushButton_26 = QPushButton(self.frame_18)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.horizontalLayout_15.addWidget(self.pushButton_26)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.scrollArea_12.setWidget(self.scrollAreaWidgetContents_22)

        self.gridLayout_11.addWidget(self.scrollArea_12, 1, 1, 1, 1)

        self.scrollArea_11 = QScrollArea(self.deceased)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        self.scrollArea_11.setMinimumSize(QSize(200, 0))
        self.scrollArea_11.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 194, 466))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_19)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_6)

        self.label_20 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_13.addWidget(self.label_20)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_21)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_13.addWidget(self.lineEdit_7)

        self.label_25 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_13.addWidget(self.label_25)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents_21)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.verticalLayout_13.addWidget(self.lineEdit_9)

        self.label_27 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_13.addWidget(self.label_27)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_21)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.verticalLayout_13.addWidget(self.lineEdit_10)

        self.label_28 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_13.addWidget(self.label_28)

        self.dateEdit_3 = QDateEdit(self.scrollAreaWidgetContents_21)
        self.dateEdit_3.setObjectName(u"dateEdit_3")

        self.verticalLayout_13.addWidget(self.dateEdit_3)

        self.label_29 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_13.addWidget(self.label_29)

        self.dateEdit_4 = QDateEdit(self.scrollAreaWidgetContents_21)
        self.dateEdit_4.setObjectName(u"dateEdit_4")

        self.verticalLayout_13.addWidget(self.dateEdit_4)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_13.addWidget(self.label_30)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_21)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_13.addWidget(self.comboBox_4)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_13.addWidget(self.label_31)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents_21)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_13.addWidget(self.comboBox_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_21)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_23 = QPushButton(self.frame_17)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_14.addWidget(self.pushButton_23)

        self.pushButton_24 = QPushButton(self.frame_17)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_14.addWidget(self.pushButton_24)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_21)

        self.gridLayout_11.addWidget(self.scrollArea_11, 1, 2, 1, 1)

        self.stacked_widget.addWidget(self.deceased)
        self.holders = QWidget()
        self.holders.setObjectName(u"holders")
        self.gridLayout_12 = QGridLayout(self.holders)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_19 = QFrame(self.holders)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_16.addWidget(self.label_22)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)

        self.pushButton_27 = QPushButton(self.frame_19)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.horizontalLayout_16.addWidget(self.pushButton_27)


        self.gridLayout_12.addWidget(self.frame_19, 0, 0, 1, 3)

        self.scrollArea_13 = QScrollArea(self.holders)
        self.scrollArea_13.setObjectName(u"scrollArea_13")
        self.scrollArea_13.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 124, 117))
        self.formLayout_12 = QFormLayout(self.scrollAreaWidgetContents_23)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.lineEdit_14 = QLineEdit(self.scrollAreaWidgetContents_23)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.lineEdit_14)

        self.label_21 = QLabel(self.scrollAreaWidgetContents_23)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.tableView_5 = QTableView(self.scrollAreaWidgetContents_23)
        self.tableView_5.setObjectName(u"tableView_5")

        self.formLayout_12.setWidget(1, QFormLayout.SpanningRole, self.tableView_5)

        self.scrollArea_13.setWidget(self.scrollAreaWidgetContents_23)

        self.gridLayout_12.addWidget(self.scrollArea_13, 1, 0, 1, 1)

        self.scrollArea_15 = QScrollArea(self.holders)
        self.scrollArea_15.setObjectName(u"scrollArea_15")
        self.scrollArea_15.setMinimumSize(QSize(200, 0))
        self.scrollArea_15.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollAreaWidgetContents_25 = QWidget()
        self.scrollAreaWidgetContents_25.setObjectName(u"scrollAreaWidgetContents_25")
        self.scrollAreaWidgetContents_25.setGeometry(QRect(0, 0, 194, 316))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_25)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_32 = QLabel(self.scrollAreaWidgetContents_25)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_32)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_16.addItem(self.horizontalSpacer_7)

        self.label_34 = QLabel(self.scrollAreaWidgetContents_25)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_16.addWidget(self.label_34)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents_25)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_16.addWidget(self.lineEdit_11)

        self.label_35 = QLabel(self.scrollAreaWidgetContents_25)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_16.addWidget(self.label_35)

        self.lineEdit_12 = QLineEdit(self.scrollAreaWidgetContents_25)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.verticalLayout_16.addWidget(self.lineEdit_12)

        self.label_36 = QLabel(self.scrollAreaWidgetContents_25)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_16.addWidget(self.label_36)

        self.lineEdit_16 = QLineEdit(self.scrollAreaWidgetContents_25)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.verticalLayout_16.addWidget(self.lineEdit_16)

        self.label_37 = QLabel(self.scrollAreaWidgetContents_25)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_16.addWidget(self.label_37)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents_25)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.verticalLayout_16.addWidget(self.lineEdit_17)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_6)

        self.frame_21 = QFrame(self.scrollAreaWidgetContents_25)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_30 = QPushButton(self.frame_21)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.horizontalLayout_18.addWidget(self.pushButton_30)

        self.pushButton_31 = QPushButton(self.frame_21)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.horizontalLayout_18.addWidget(self.pushButton_31)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_25)

        self.gridLayout_12.addWidget(self.scrollArea_15, 1, 1, 1, 1)

        self.scrollArea_14 = QScrollArea(self.holders)
        self.scrollArea_14.setObjectName(u"scrollArea_14")
        self.scrollArea_14.setMinimumSize(QSize(200, 0))
        self.scrollArea_14.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollAreaWidgetContents_24 = QWidget()
        self.scrollAreaWidgetContents_24.setObjectName(u"scrollAreaWidgetContents_24")
        self.scrollAreaWidgetContents_24.setGeometry(QRect(0, 0, 194, 316))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_24)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_33 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_33)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.horizontalSpacer_12)

        self.label_38 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_15.addWidget(self.label_38)

        self.lineEdit_18 = QLineEdit(self.scrollAreaWidgetContents_24)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.verticalLayout_15.addWidget(self.lineEdit_18)

        self.label_39 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_15.addWidget(self.label_39)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents_24)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.verticalLayout_15.addWidget(self.lineEdit_19)

        self.label_40 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_15.addWidget(self.label_40)

        self.lineEdit_20 = QLineEdit(self.scrollAreaWidgetContents_24)
        self.lineEdit_20.setObjectName(u"lineEdit_20")

        self.verticalLayout_15.addWidget(self.lineEdit_20)

        self.label_41 = QLabel(self.scrollAreaWidgetContents_24)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_15.addWidget(self.label_41)

        self.lineEdit_21 = QLineEdit(self.scrollAreaWidgetContents_24)
        self.lineEdit_21.setObjectName(u"lineEdit_21")

        self.verticalLayout_15.addWidget(self.lineEdit_21)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)

        self.frame_20 = QFrame(self.scrollAreaWidgetContents_24)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_28 = QPushButton(self.frame_20)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.horizontalLayout_17.addWidget(self.pushButton_28)

        self.pushButton_29 = QPushButton(self.frame_20)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.horizontalLayout_17.addWidget(self.pushButton_29)


        self.verticalLayout_15.addWidget(self.frame_20)

        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_24)

        self.gridLayout_12.addWidget(self.scrollArea_14, 1, 2, 1, 1)

        self.stacked_widget.addWidget(self.holders)
        self.niches = QWidget()
        self.niches.setObjectName(u"niches")
        self.gridLayout_4 = QGridLayout(self.niches)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scrollArea_2 = QScrollArea(self.niches)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(200, 0))
        self.scrollArea_2.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 194, 463))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer)

        self.label_42 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_3.addWidget(self.label_42)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.verticalLayout_3.addWidget(self.comboBox_6)

        self.label_43 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_3.addWidget(self.label_43)

        self.comboBox_7 = QComboBox(self.scrollAreaWidgetContents_6)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.verticalLayout_3.addWidget(self.comboBox_7)

        self.label_44 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_3.addWidget(self.label_44)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_3.addWidget(self.spinBox)

        self.label_45 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_3.addWidget(self.label_45)

        self.lineEdit_22 = QLineEdit(self.scrollAreaWidgetContents_6)
        self.lineEdit_22.setObjectName(u"lineEdit_22")

        self.verticalLayout_3.addWidget(self.lineEdit_22)

        self.label_23 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_3.addWidget(self.label_23)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.graphicsView = QGraphicsView(self.frame_6)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_5.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.toolButton = QToolButton(self.frame_6)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_5.addWidget(self.toolButton, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_6)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_3.addWidget(self.pushButton_5)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_4.addWidget(self.scrollArea_2, 1, 1, 1, 1)

        self.scrollArea = QScrollArea(self.niches)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 124, 117))
        self.formLayout_4 = QFormLayout(self.scrollAreaWidgetContents_5)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_5)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.tableView = QTableView(self.scrollAreaWidgetContents_5)
        self.tableView.setObjectName(u"tableView")

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.tableView)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_4.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.scrollArea_3 = QScrollArea(self.niches)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setMinimumSize(QSize(200, 0))
        self.scrollArea_3.setMaximumSize(QSize(200, 16777215))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 194, 313))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_46 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_4.addWidget(self.label_46)

        self.lineEdit_23 = QLineEdit(self.scrollAreaWidgetContents_7)
        self.lineEdit_23.setObjectName(u"lineEdit_23")

        self.verticalLayout_4.addWidget(self.lineEdit_23)

        self.label_47 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_4.addWidget(self.label_47)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.toolButton_2 = QToolButton(self.frame_7)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout_6.addWidget(self.toolButton_2, 1, 1, 1, 1)

        self.graphicsView_2 = QGraphicsView(self.frame_7)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.gridLayout_6.addWidget(self.graphicsView_2, 0, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_6 = QPushButton(self.frame_5)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_5)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout_4.addWidget(self.frame_5)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_4.addWidget(self.scrollArea_3, 1, 2, 1, 1)

        self.frame_3 = QFrame(self.niches)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_2.addWidget(self.pushButton_4)


        self.gridLayout_4.addWidget(self.frame_3, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.niches)
        self.my_account = QWidget()
        self.my_account.setObjectName(u"my_account")
        self.gridLayout_13 = QGridLayout(self.my_account)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scroll_area_change_password = QScrollArea(self.my_account)
        self.scroll_area_change_password.setObjectName(u"scroll_area_change_password")
        self.scroll_area_change_password.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_change_password.setWidgetResizable(True)
        self.scrollAreaWidgetContents_28 = QWidget()
        self.scrollAreaWidgetContents_28.setObjectName(u"scrollAreaWidgetContents_28")
        self.scrollAreaWidgetContents_28.setGeometry(QRect(0, 0, 152, 266))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_28)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_my_account_change_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_change_password.setObjectName(u"label_my_account_change_password")
        self.label_my_account_change_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_my_account_change_password)

        self.horizontal_spacer_my_account_change_password = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_18.addItem(self.horizontal_spacer_my_account_change_password)

        self.label_my_account_current_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_current_password.setObjectName(u"label_my_account_current_password")

        self.verticalLayout_18.addWidget(self.label_my_account_current_password)

        self.line_edit_my_account_current_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_current_password.setObjectName(u"line_edit_my_account_current_password")

        self.verticalLayout_18.addWidget(self.line_edit_my_account_current_password)

        self.label_my_account_new_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_new_password.setObjectName(u"label_my_account_new_password")

        self.verticalLayout_18.addWidget(self.label_my_account_new_password)

        self.line_edit_my_account_new_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_new_password.setObjectName(u"line_edit_my_account_new_password")

        self.verticalLayout_18.addWidget(self.line_edit_my_account_new_password)

        self.label_my_account_repeat_new_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_repeat_new_password.setObjectName(u"label_my_account_repeat_new_password")

        self.verticalLayout_18.addWidget(self.label_my_account_repeat_new_password)

        self.line_edit_my_account_repeat_new_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_repeat_new_password.setObjectName(u"line_edit_my_account_repeat_new_password")

        self.verticalLayout_18.addWidget(self.line_edit_my_account_repeat_new_password)

        self.vertical_spacer_my_account = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.vertical_spacer_my_account)

        self.frame_change_password = QFrame(self.scrollAreaWidgetContents_28)
        self.frame_change_password.setObjectName(u"frame_change_password")
        self.frame_change_password.setFrameShape(QFrame.StyledPanel)
        self.frame_change_password.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_change_password)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.push_button_change_password = QPushButton(self.frame_change_password)
        self.push_button_change_password.setObjectName(u"push_button_change_password")

        self.horizontalLayout_21.addWidget(self.push_button_change_password)


        self.verticalLayout_18.addWidget(self.frame_change_password)

        self.scroll_area_change_password.setWidget(self.scrollAreaWidgetContents_28)

        self.gridLayout_13.addWidget(self.scroll_area_change_password, 2, 1, 1, 1)

        self.frame_22 = QFrame(self.my_account)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_my_account_my_account = QLabel(self.frame_22)
        self.label_my_account_my_account.setObjectName(u"label_my_account_my_account")

        self.horizontalLayout_19.addWidget(self.label_my_account_my_account)

        self.horizontal_spacer_my_account_header = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontal_spacer_my_account_header)


        self.gridLayout_13.addWidget(self.frame_22, 0, 0, 1, 3)

        self.frame_8 = QFrame(self.my_account)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_my_account_user_name = QLabel(self.frame_8)
        self.label_my_account_user_name.setObjectName(u"label_my_account_user_name")

        self.horizontalLayout_5.addWidget(self.label_my_account_user_name)

        self.label_my_account_your_user_name = QLabel(self.frame_8)
        self.label_my_account_your_user_name.setObjectName(u"label_my_account_your_user_name")

        self.horizontalLayout_5.addWidget(self.label_my_account_your_user_name)

        self.horizontal_spacer_my_account_user_name = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontal_spacer_my_account_user_name)


        self.gridLayout_13.addWidget(self.frame_8, 1, 0, 1, 3)

        self.stacked_widget.addWidget(self.my_account)

        self.gridLayout.addWidget(self.stacked_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.push_button_deceased.setDefault(False)
        self.stacked_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Enduring Chambers", None))
        self.label_welcome.setText(QCoreApplication.translate("MainWindow", u"Hola:", None))
        self.label_welcome_user_name.setText(QCoreApplication.translate("MainWindow", u"user_name", None))
        self.push_button_users.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.push_button_deceased.setText(QCoreApplication.translate("MainWindow", u"Fallecidos", None))
        self.push_button_holders.setText(QCoreApplication.translate("MainWindow", u"Titulares", None))
        self.push_button_niches.setText(QCoreApplication.translate("MainWindow", u"Nichos", None))
        self.push_button_my_account.setText(QCoreApplication.translate("MainWindow", u"Mi cuenta", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Selecciona un bot\u00f3n", None))
        self.label_create_user.setText(QCoreApplication.translate("MainWindow", u"Crear usuario", None))
        self.label_create_user_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_create_user_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_create_user_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_create_user_user_name.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario:", None))
        self.label_create_user_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.label_create_user_repeat_password.setText(QCoreApplication.translate("MainWindow", u"Repetir contrase\u00f1a:", None))
        self.label_create_user_user_type.setText(QCoreApplication.translate("MainWindow", u"Tipo de usuario:", None))
        self.push_button_create_user_save_user.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_create_user_clean_user.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_modify_user.setText(QCoreApplication.translate("MainWindow", u"Modificar usuario", None))
        self.label_modify_user_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_modify_user_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_modify_user_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_modify_user_user_type.setText(QCoreApplication.translate("MainWindow", u"Tipo de usuario", None))
        self.push_button_modify_user_activate.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.push_button_modify_user_deactivate.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.push_button_modify_user_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_search_users.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.label_users.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.push_button_create_user_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fallecidos", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Crear fallecido", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Fecha de defunci\u00f3n:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tipo de restos:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nicho:", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Modificar fallecido", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Fecha de defunci\u00f3n", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tipo de restos:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Nicho:", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Titulares", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Crear titular", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Modificar titular", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Crear nicho", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Letra:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Titular:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Imagen:", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Modificar nicho", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Titular:", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Imagen:", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nichos", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_my_account_change_password.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a:", None))
        self.label_my_account_current_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a actual:", None))
        self.label_my_account_new_password.setText(QCoreApplication.translate("MainWindow", u"Nueva contrase\u00f1a:", None))
        self.label_my_account_repeat_new_password.setText(QCoreApplication.translate("MainWindow", u"Repetir contrase\u00f1a:", None))
        self.push_button_change_password.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a", None))
        self.label_my_account_my_account.setText(QCoreApplication.translate("MainWindow", u"Mi cuenta", None))
        self.label_my_account_user_name.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario:", None))
        self.label_my_account_your_user_name.setText(QCoreApplication.translate("MainWindow", u"your_user_name", None))
    # retranslateUi

