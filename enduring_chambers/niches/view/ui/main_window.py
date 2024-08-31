# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import niches.view.enduring_chambers_initials_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 631)
        MainWindow.setMinimumSize(QSize(650, 500))
        icon = QIcon()
        icon.addFile(u":/icons/enduring_chambers_initials.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_lateral_window = QFrame(self.centralwidget)
        self.frame_lateral_window.setObjectName(u"frame_lateral_window")
        self.frame_lateral_window.setMinimumSize(QSize(110, 0))
        self.frame_lateral_window.setMaximumSize(QSize(200, 16777215))
        self.frame_lateral_window.setStyleSheet(u"")
        self.frame_lateral_window.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lateral_window.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_lateral_window)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_welcome = QLabel(self.frame_lateral_window)
        self.label_welcome.setObjectName(u"label_welcome")
        self.label_welcome.setStyleSheet(u"")
        self.label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_welcome)

        self.label_welcome_user_name = QLabel(self.frame_lateral_window)
        self.label_welcome_user_name.setObjectName(u"label_welcome_user_name")
        self.label_welcome_user_name.setStyleSheet(u"")
        self.label_welcome_user_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_welcome_user_name)

        self.push_button_users = QPushButton(self.frame_lateral_window)
        self.push_button_users.setObjectName(u"push_button_users")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.push_button_users.sizePolicy().hasHeightForWidth())
        self.push_button_users.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        font.setKerning(True)
        self.push_button_users.setFont(font)
        self.push_button_users.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.push_button_users.setAcceptDrops(False)
        self.push_button_users.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u":/icons/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_users.setIcon(icon1)
        self.push_button_users.setIconSize(QSize(20, 20))
        self.push_button_users.setCheckable(True)
        self.push_button_users.setAutoDefault(False)
        self.push_button_users.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_users)

        self.push_button_deceased = QPushButton(self.frame_lateral_window)
        self.push_button_deceased.setObjectName(u"push_button_deceased")
        sizePolicy.setHeightForWidth(self.push_button_deceased.sizePolicy().hasHeightForWidth())
        self.push_button_deceased.setSizePolicy(sizePolicy)
        self.push_button_deceased.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon2 = QIcon()
        icon2.addFile(u":/icons/user-minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_deceased.setIcon(icon2)
        self.push_button_deceased.setIconSize(QSize(20, 20))
        self.push_button_deceased.setCheckable(True)
        self.push_button_deceased.setAutoDefault(False)
        self.push_button_deceased.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_deceased)

        self.push_button_holders = QPushButton(self.frame_lateral_window)
        self.push_button_holders.setObjectName(u"push_button_holders")
        sizePolicy.setHeightForWidth(self.push_button_holders.sizePolicy().hasHeightForWidth())
        self.push_button_holders.setSizePolicy(sizePolicy)
        self.push_button_holders.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/user-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_holders.setIcon(icon3)
        self.push_button_holders.setIconSize(QSize(20, 20))
        self.push_button_holders.setCheckable(True)
        self.push_button_holders.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_holders)

        self.push_button_niches = QPushButton(self.frame_lateral_window)
        self.push_button_niches.setObjectName(u"push_button_niches")
        sizePolicy.setHeightForWidth(self.push_button_niches.sizePolicy().hasHeightForWidth())
        self.push_button_niches.setSizePolicy(sizePolicy)
        self.push_button_niches.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon4 = QIcon()
        icon4.addFile(u":/icons/archive.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_niches.setIcon(icon4)
        self.push_button_niches.setIconSize(QSize(20, 20))
        self.push_button_niches.setCheckable(True)
        self.push_button_niches.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_niches)

        self.push_button_payments = QPushButton(self.frame_lateral_window)
        self.push_button_payments.setObjectName(u"push_button_payments")
        sizePolicy.setHeightForWidth(self.push_button_payments.sizePolicy().hasHeightForWidth())
        self.push_button_payments.setSizePolicy(sizePolicy)
        self.push_button_payments.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon5 = QIcon()
        icon5.addFile(u":/icons/credit-card.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_payments.setIcon(icon5)
        self.push_button_payments.setIconSize(QSize(20, 20))
        self.push_button_payments.setCheckable(True)
        self.push_button_payments.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_payments)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.push_button_my_account = QPushButton(self.frame_lateral_window)
        self.push_button_my_account.setObjectName(u"push_button_my_account")
        self.push_button_my_account.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.push_button_my_account.setAutoFillBackground(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/user-check.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_my_account.setIcon(icon6)
        self.push_button_my_account.setIconSize(QSize(20, 20))
        self.push_button_my_account.setCheckable(True)
        self.push_button_my_account.setFlat(True)

        self.verticalLayout_5.addWidget(self.push_button_my_account)


        self.horizontalLayout_7.addWidget(self.frame_lateral_window)

        self.stacked_widget = QStackedWidget(self.centralwidget)
        self.stacked_widget.setObjectName(u"stacked_widget")
        self.stacked_widget.setAutoFillBackground(False)
        self.stacked_widget.setFrameShape(QFrame.Shape.NoFrame)
        self.stacked_widget.setFrameShadow(QFrame.Shadow.Plain)
        self.unselected = QWidget()
        self.unselected.setObjectName(u"unselected")
        self.gridLayout_14 = QGridLayout(self.unselected)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.frame_25 = QFrame(self.unselected)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_26 = QLabel(self.frame_25)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_22.addWidget(self.label_26)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_11)


        self.gridLayout_14.addWidget(self.frame_25, 0, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.stacked_widget.addWidget(self.unselected)
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.gridLayout_3 = QGridLayout(self.users)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scroll_area_create_user = QScrollArea(self.users)
        self.scroll_area_create_user.setObjectName(u"scroll_area_create_user")
        self.scroll_area_create_user.setEnabled(True)
        self.scroll_area_create_user.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_user.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_create_user.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 194, 466))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_create_user = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user.setObjectName(u"label_create_user")
        self.label_create_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_create_user)

        self.horizontal_spacer_create_user = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontal_spacer_create_user)

        self.label_create_user_name = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_name.setObjectName(u"label_create_user_name")
        self.label_create_user_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

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
        self.line_edit_create_user_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.line_edit_create_user_password)

        self.label_create_user_repeat_password = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_repeat_password.setObjectName(u"label_create_user_repeat_password")

        self.verticalLayout_2.addWidget(self.label_create_user_repeat_password)

        self.line_edit_create_user_repeat_password = QLineEdit(self.scrollAreaWidgetContents_3)
        self.line_edit_create_user_repeat_password.setObjectName(u"line_edit_create_user_repeat_password")
        self.line_edit_create_user_repeat_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.line_edit_create_user_repeat_password)

        self.label_create_user_user_type = QLabel(self.scrollAreaWidgetContents_3)
        self.label_create_user_user_type.setObjectName(u"label_create_user_user_type")

        self.verticalLayout_2.addWidget(self.label_create_user_user_type)

        self.combo_box_create_user_user_type = QComboBox(self.scrollAreaWidgetContents_3)
        self.combo_box_create_user_user_type.setObjectName(u"combo_box_create_user_user_type")

        self.verticalLayout_2.addWidget(self.combo_box_create_user_user_type)

        self.vertical_spacer_create_user = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.vertical_spacer_create_user)

        self.frame_create_user_buttons = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_create_user_buttons.setObjectName(u"frame_create_user_buttons")
        self.frame_create_user_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_create_user_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_create_user_buttons)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.push_button_create_user_save_user = QPushButton(self.frame_create_user_buttons)
        self.push_button_create_user_save_user.setObjectName(u"push_button_create_user_save_user")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.push_button_create_user_save_user)

        self.push_button_create_user_clean_user = QPushButton(self.frame_create_user_buttons)
        self.push_button_create_user_clean_user.setObjectName(u"push_button_create_user_clean_user")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.push_button_create_user_clean_user)


        self.verticalLayout_2.addWidget(self.frame_create_user_buttons)

        self.scroll_area_create_user.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_3.addWidget(self.scroll_area_create_user, 1, 1, 1, 1)

        self.scroll_area_modify_user = QScrollArea(self.users)
        self.scroll_area_modify_user.setObjectName(u"scroll_area_modify_user")
        self.scroll_area_modify_user.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_user.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_modify_user.setWidgetResizable(True)
        self.scroll_area_modify_user.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 194, 346))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_modify_user = QLabel(self.scrollAreaWidgetContents_2)
        self.label_modify_user.setObjectName(u"label_modify_user")
        self.label_modify_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_modify_user)

        self.horizontal_spacer_modify_user = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

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

        self.vertical_spacer_modify_user = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.vertical_spacer_modify_user)

        self.frame_modify_user_buttons = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_modify_user_buttons.setObjectName(u"frame_modify_user_buttons")
        self.frame_modify_user_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_modify_user_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frame_modify_user_buttons)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.push_button_modify_user_activate = QPushButton(self.frame_modify_user_buttons)
        self.push_button_modify_user_activate.setObjectName(u"push_button_modify_user_activate")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.push_button_modify_user_activate)

        self.push_button_modify_user_deactivate = QPushButton(self.frame_modify_user_buttons)
        self.push_button_modify_user_deactivate.setObjectName(u"push_button_modify_user_deactivate")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.push_button_modify_user_deactivate)

        self.push_button_modify_user_save = QPushButton(self.frame_modify_user_buttons)
        self.push_button_modify_user_save.setObjectName(u"push_button_modify_user_save")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.push_button_modify_user_save)


        self.verticalLayout.addWidget(self.frame_modify_user_buttons)

        self.scroll_area_modify_user.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_3.addWidget(self.scroll_area_modify_user, 1, 2, 1, 1)

        self.scroll_area_users = QScrollArea(self.users)
        self.scroll_area_users.setObjectName(u"scroll_area_users")
        self.scroll_area_users.setStyleSheet(u"")
        self.scroll_area_users.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 98, 117))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.line_edit_search_users = QLineEdit(self.scrollAreaWidgetContents_4)
        self.line_edit_search_users.setObjectName(u"line_edit_search_users")

        self.gridLayout_2.addWidget(self.line_edit_search_users, 0, 1, 1, 1)

        self.table_widget_users = QTableWidget(self.scrollAreaWidgetContents_4)
        self.table_widget_users.setObjectName(u"table_widget_users")

        self.gridLayout_2.addWidget(self.table_widget_users, 1, 0, 1, 2)

        self.scroll_area_users.setWidget(self.scrollAreaWidgetContents_4)

        self.gridLayout_3.addWidget(self.scroll_area_users, 1, 0, 1, 1)

        self.frame_users_header = QFrame(self.users)
        self.frame_users_header.setObjectName(u"frame_users_header")
        self.frame_users_header.setStyleSheet(u"")
        self.frame_users_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_users_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_users_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_users = QLabel(self.frame_users_header)
        self.label_users.setObjectName(u"label_users")

        self.horizontalLayout.addWidget(self.label_users)

        self.horizontal_spacer_users_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontal_spacer_users_header)

        self.push_button_create_user_create = QPushButton(self.frame_users_header)
        self.push_button_create_user_create.setObjectName(u"push_button_create_user_create")

        self.horizontalLayout.addWidget(self.push_button_create_user_create)


        self.gridLayout_3.addWidget(self.frame_users_header, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.users)
        self.deceased = QWidget()
        self.deceased.setObjectName(u"deceased")
        self.gridLayout_11 = QGridLayout(self.deceased)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.scroll_area_modify_deceased = QScrollArea(self.deceased)
        self.scroll_area_modify_deceased.setObjectName(u"scroll_area_modify_deceased")
        self.scroll_area_modify_deceased.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_deceased.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_modify_deceased.setWidgetResizable(True)
        self.scrollAreaWidgetContents_21 = QWidget()
        self.scrollAreaWidgetContents_21.setObjectName(u"scrollAreaWidgetContents_21")
        self.scrollAreaWidgetContents_21.setGeometry(QRect(0, 0, 194, 872))
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContents_21)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_modify_deceased = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased.setObjectName(u"label_modify_deceased")
        self.label_modify_deceased.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_modify_deceased)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_13.addItem(self.horizontalSpacer_6)

        self.label_modify_deceased_image = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_image.setObjectName(u"label_modify_deceased_image")
        self.label_modify_deceased_image.setStyleSheet(u"QLabel{\n"
"	border: 2px dashed\n"
"}")
        self.label_modify_deceased_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_modify_deceased_image)

        self.push_button_modify_deceased_image = QPushButton(self.scrollAreaWidgetContents_21)
        self.push_button_modify_deceased_image.setObjectName(u"push_button_modify_deceased_image")

        self.verticalLayout_13.addWidget(self.push_button_modify_deceased_image)

        self.label_modify_deceased_name = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_name.setObjectName(u"label_modify_deceased_name")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_name)

        self.line_edit_modify_deceased_name = QLineEdit(self.scrollAreaWidgetContents_21)
        self.line_edit_modify_deceased_name.setObjectName(u"line_edit_modify_deceased_name")

        self.verticalLayout_13.addWidget(self.line_edit_modify_deceased_name)

        self.label_modify_deceased_paternal_surname = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_paternal_surname.setObjectName(u"label_modify_deceased_paternal_surname")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_paternal_surname)

        self.line_edit_modify_deceased_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_21)
        self.line_edit_modify_deceased_paternal_surname.setObjectName(u"line_edit_modify_deceased_paternal_surname")

        self.verticalLayout_13.addWidget(self.line_edit_modify_deceased_paternal_surname)

        self.label_modify_deceased_maternal_surname = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_maternal_surname.setObjectName(u"label_modify_deceased_maternal_surname")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_maternal_surname)

        self.line_edit_modify_deceased_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_21)
        self.line_edit_modify_deceased_maternal_surname.setObjectName(u"line_edit_modify_deceased_maternal_surname")

        self.verticalLayout_13.addWidget(self.line_edit_modify_deceased_maternal_surname)

        self.label_modify_deceased_birth_date = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_birth_date.setObjectName(u"label_modify_deceased_birth_date")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_birth_date)

        self.checkBox_modify_deceased_birth_date = QCheckBox(self.scrollAreaWidgetContents_21)
        self.checkBox_modify_deceased_birth_date.setObjectName(u"checkBox_modify_deceased_birth_date")

        self.verticalLayout_13.addWidget(self.checkBox_modify_deceased_birth_date)

        self.date_edit_modify_deceased_birth_date = QDateEdit(self.scrollAreaWidgetContents_21)
        self.date_edit_modify_deceased_birth_date.setObjectName(u"date_edit_modify_deceased_birth_date")
        self.date_edit_modify_deceased_birth_date.setCalendarPopup(True)

        self.verticalLayout_13.addWidget(self.date_edit_modify_deceased_birth_date)

        self.label_modify_deceased_death_date = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_death_date.setObjectName(u"label_modify_deceased_death_date")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_death_date)

        self.checkBox_modify_deceased_death_date = QCheckBox(self.scrollAreaWidgetContents_21)
        self.checkBox_modify_deceased_death_date.setObjectName(u"checkBox_modify_deceased_death_date")

        self.verticalLayout_13.addWidget(self.checkBox_modify_deceased_death_date)

        self.date_edit_modify_deceased_death_date = QDateEdit(self.scrollAreaWidgetContents_21)
        self.date_edit_modify_deceased_death_date.setObjectName(u"date_edit_modify_deceased_death_date")
        self.date_edit_modify_deceased_death_date.setCalendarPopup(True)

        self.verticalLayout_13.addWidget(self.date_edit_modify_deceased_death_date)

        self.label__modify_deceased_remaint_type = QLabel(self.scrollAreaWidgetContents_21)
        self.label__modify_deceased_remaint_type.setObjectName(u"label__modify_deceased_remaint_type")

        self.verticalLayout_13.addWidget(self.label__modify_deceased_remaint_type)

        self.combo_box_modify_deceased_remain_type = QComboBox(self.scrollAreaWidgetContents_21)
        self.combo_box_modify_deceased_remain_type.setObjectName(u"combo_box_modify_deceased_remain_type")

        self.verticalLayout_13.addWidget(self.combo_box_modify_deceased_remain_type)

        self.label_31 = QLabel(self.scrollAreaWidgetContents_21)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_13.addWidget(self.label_31)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_21)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.combo_box_modify_deceased_row = QComboBox(self.frame_3)
        self.combo_box_modify_deceased_row.setObjectName(u"combo_box_modify_deceased_row")

        self.gridLayout_10.addWidget(self.combo_box_modify_deceased_row, 1, 1, 1, 1)

        self.combo_box_modify_deceased_module = QComboBox(self.frame_3)
        self.combo_box_modify_deceased_module.setObjectName(u"combo_box_modify_deceased_module")

        self.gridLayout_10.addWidget(self.combo_box_modify_deceased_module, 1, 0, 1, 1)

        self.label_modify_deceased_module = QLabel(self.frame_3)
        self.label_modify_deceased_module.setObjectName(u"label_modify_deceased_module")

        self.gridLayout_10.addWidget(self.label_modify_deceased_module, 0, 0, 1, 1)

        self.label_modify_deceased_row = QLabel(self.frame_3)
        self.label_modify_deceased_row.setObjectName(u"label_modify_deceased_row")

        self.gridLayout_10.addWidget(self.label_modify_deceased_row, 0, 1, 1, 1)


        self.verticalLayout_13.addWidget(self.frame_3)

        self.combo_box_modify_deceased_niche = QComboBox(self.scrollAreaWidgetContents_21)
        self.combo_box_modify_deceased_niche.setObjectName(u"combo_box_modify_deceased_niche")

        self.verticalLayout_13.addWidget(self.combo_box_modify_deceased_niche)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.label_modify_deceased_book = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_book.setObjectName(u"label_modify_deceased_book")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_book)

        self.plain_text_edit_modify_deceased_book = QPlainTextEdit(self.scrollAreaWidgetContents_21)
        self.plain_text_edit_modify_deceased_book.setObjectName(u"plain_text_edit_modify_deceased_book")

        self.verticalLayout_13.addWidget(self.plain_text_edit_modify_deceased_book)

        self.label_modify_deceased_sheet = QLabel(self.scrollAreaWidgetContents_21)
        self.label_modify_deceased_sheet.setObjectName(u"label_modify_deceased_sheet")

        self.verticalLayout_13.addWidget(self.label_modify_deceased_sheet)

        self.plain_text_edit_modify_deceased_sheet = QPlainTextEdit(self.scrollAreaWidgetContents_21)
        self.plain_text_edit_modify_deceased_sheet.setObjectName(u"plain_text_edit_modify_deceased_sheet")

        self.verticalLayout_13.addWidget(self.plain_text_edit_modify_deceased_sheet)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_21)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_5 = QFormLayout(self.frame_17)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.push_button_modify_deceased_active = QPushButton(self.frame_17)
        self.push_button_modify_deceased_active.setObjectName(u"push_button_modify_deceased_active")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.push_button_modify_deceased_active)

        self.push_button_modify_deceased_save = QPushButton(self.frame_17)
        self.push_button_modify_deceased_save.setObjectName(u"push_button_modify_deceased_save")

        self.formLayout_5.setWidget(1, QFormLayout.SpanningRole, self.push_button_modify_deceased_save)

        self.push_button_modify_deceased_deactivate = QPushButton(self.frame_17)
        self.push_button_modify_deceased_deactivate.setObjectName(u"push_button_modify_deceased_deactivate")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.push_button_modify_deceased_deactivate)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.scroll_area_modify_deceased.setWidget(self.scrollAreaWidgetContents_21)

        self.gridLayout_11.addWidget(self.scroll_area_modify_deceased, 1, 2, 1, 1)

        self.frame_deceased_header = QFrame(self.deceased)
        self.frame_deceased_header.setObjectName(u"frame_deceased_header")
        self.frame_deceased_header.setStyleSheet(u"")
        self.frame_deceased_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_deceased_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_deceased_header)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_deceased = QLabel(self.frame_deceased_header)
        self.label_deceased.setObjectName(u"label_deceased")

        self.horizontalLayout_13.addWidget(self.label_deceased)

        self.horizontal_spacer_deceased_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontal_spacer_deceased_header)

        self.push_button_create_deceased_create = QPushButton(self.frame_deceased_header)
        self.push_button_create_deceased_create.setObjectName(u"push_button_create_deceased_create")

        self.horizontalLayout_13.addWidget(self.push_button_create_deceased_create)


        self.gridLayout_11.addWidget(self.frame_deceased_header, 0, 0, 1, 3)

        self.scroll_area_search_deceased = QScrollArea(self.deceased)
        self.scroll_area_search_deceased.setObjectName(u"scroll_area_search_deceased")
        self.scroll_area_search_deceased.setWidgetResizable(True)
        self.scrollAreaWidgetContents_20 = QWidget()
        self.scrollAreaWidgetContents_20.setObjectName(u"scrollAreaWidgetContents_20")
        self.scrollAreaWidgetContents_20.setGeometry(QRect(0, 0, 98, 117))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_20)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.line_edit_search_deceased = QLineEdit(self.scrollAreaWidgetContents_20)
        self.line_edit_search_deceased.setObjectName(u"line_edit_search_deceased")

        self.gridLayout_7.addWidget(self.line_edit_search_deceased, 0, 0, 1, 1)

        self.table_widget_deceased = QTableWidget(self.scrollAreaWidgetContents_20)
        self.table_widget_deceased.setObjectName(u"table_widget_deceased")

        self.gridLayout_7.addWidget(self.table_widget_deceased, 1, 0, 1, 1)

        self.scroll_area_search_deceased.setWidget(self.scrollAreaWidgetContents_20)

        self.gridLayout_11.addWidget(self.scroll_area_search_deceased, 1, 0, 1, 1)

        self.scroll_area_create_deceased = QScrollArea(self.deceased)
        self.scroll_area_create_deceased.setObjectName(u"scroll_area_create_deceased")
        self.scroll_area_create_deceased.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_deceased.setMaximumSize(QSize(200, 16777215))
        self.scroll_area_create_deceased.setWidgetResizable(True)
        self.scrollAreaWidgetContents_22 = QWidget()
        self.scrollAreaWidgetContents_22.setObjectName(u"scrollAreaWidgetContents_22")
        self.scrollAreaWidgetContents_22.setGeometry(QRect(0, 0, 194, 842))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_22)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_create_deceased = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased.setObjectName(u"label_create_deceased")
        self.label_create_deceased.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_create_deceased)

        self.horizontal_spacer_create_deceased = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_14.addItem(self.horizontal_spacer_create_deceased)

        self.label_create_deceased_image = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_image.setObjectName(u"label_create_deceased_image")
        self.label_create_deceased_image.setStyleSheet(u"QLabel{\n"
"	border: 2px dashed\n"
"}")
        self.label_create_deceased_image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_create_deceased_image)

        self.push_button_create_deceased_image = QPushButton(self.scrollAreaWidgetContents_22)
        self.push_button_create_deceased_image.setObjectName(u"push_button_create_deceased_image")

        self.verticalLayout_14.addWidget(self.push_button_create_deceased_image)

        self.label_create_deceased_name = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_name.setObjectName(u"label_create_deceased_name")

        self.verticalLayout_14.addWidget(self.label_create_deceased_name)

        self.line_edit_create_deceased_name = QLineEdit(self.scrollAreaWidgetContents_22)
        self.line_edit_create_deceased_name.setObjectName(u"line_edit_create_deceased_name")

        self.verticalLayout_14.addWidget(self.line_edit_create_deceased_name)

        self.label_create_deceased_paternal_surname = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_paternal_surname.setObjectName(u"label_create_deceased_paternal_surname")

        self.verticalLayout_14.addWidget(self.label_create_deceased_paternal_surname)

        self.line_edit_create_deceased_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_22)
        self.line_edit_create_deceased_paternal_surname.setObjectName(u"line_edit_create_deceased_paternal_surname")

        self.verticalLayout_14.addWidget(self.line_edit_create_deceased_paternal_surname)

        self.label_create_deceased_maternal_surname = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_maternal_surname.setObjectName(u"label_create_deceased_maternal_surname")

        self.verticalLayout_14.addWidget(self.label_create_deceased_maternal_surname)

        self.line_edit_create_deceased_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_22)
        self.line_edit_create_deceased_maternal_surname.setObjectName(u"line_edit_create_deceased_maternal_surname")

        self.verticalLayout_14.addWidget(self.line_edit_create_deceased_maternal_surname)

        self.label_create_deceased_birth_date = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_birth_date.setObjectName(u"label_create_deceased_birth_date")

        self.verticalLayout_14.addWidget(self.label_create_deceased_birth_date)

        self.checkbox_create_deceased_birth_date = QCheckBox(self.scrollAreaWidgetContents_22)
        self.checkbox_create_deceased_birth_date.setObjectName(u"checkbox_create_deceased_birth_date")

        self.verticalLayout_14.addWidget(self.checkbox_create_deceased_birth_date)

        self.date_edit_create_deceased_birth_date = QDateEdit(self.scrollAreaWidgetContents_22)
        self.date_edit_create_deceased_birth_date.setObjectName(u"date_edit_create_deceased_birth_date")
        self.date_edit_create_deceased_birth_date.setCalendarPopup(True)

        self.verticalLayout_14.addWidget(self.date_edit_create_deceased_birth_date)

        self.label_create_deceased_death_date = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_death_date.setObjectName(u"label_create_deceased_death_date")

        self.verticalLayout_14.addWidget(self.label_create_deceased_death_date)

        self.checkBox_create_deceased_death_date = QCheckBox(self.scrollAreaWidgetContents_22)
        self.checkBox_create_deceased_death_date.setObjectName(u"checkBox_create_deceased_death_date")

        self.verticalLayout_14.addWidget(self.checkBox_create_deceased_death_date)

        self.date_edit_create_deceased_death_date = QDateEdit(self.scrollAreaWidgetContents_22)
        self.date_edit_create_deceased_death_date.setObjectName(u"date_edit_create_deceased_death_date")
        self.date_edit_create_deceased_death_date.setCalendarPopup(True)

        self.verticalLayout_14.addWidget(self.date_edit_create_deceased_death_date)

        self.label_create_deceased_remain_type = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_remain_type.setObjectName(u"label_create_deceased_remain_type")

        self.verticalLayout_14.addWidget(self.label_create_deceased_remain_type)

        self.combo_box_create_deceased_remain_type = QComboBox(self.scrollAreaWidgetContents_22)
        self.combo_box_create_deceased_remain_type.setObjectName(u"combo_box_create_deceased_remain_type")

        self.verticalLayout_14.addWidget(self.combo_box_create_deceased_remain_type)

        self.label_create_deceased_niche = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_niche.setObjectName(u"label_create_deceased_niche")

        self.verticalLayout_14.addWidget(self.label_create_deceased_niche)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_22)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_create_deceased_module = QLabel(self.frame_2)
        self.label_create_deceased_module.setObjectName(u"label_create_deceased_module")

        self.gridLayout_9.addWidget(self.label_create_deceased_module, 0, 0, 1, 1)

        self.label_create_deceased_row = QLabel(self.frame_2)
        self.label_create_deceased_row.setObjectName(u"label_create_deceased_row")

        self.gridLayout_9.addWidget(self.label_create_deceased_row, 0, 1, 1, 1)

        self.combo_box_create_deceased_module = QComboBox(self.frame_2)
        self.combo_box_create_deceased_module.setObjectName(u"combo_box_create_deceased_module")

        self.gridLayout_9.addWidget(self.combo_box_create_deceased_module, 1, 0, 1, 1)

        self.combo_box_create_deceased_row = QComboBox(self.frame_2)
        self.combo_box_create_deceased_row.setObjectName(u"combo_box_create_deceased_row")

        self.gridLayout_9.addWidget(self.combo_box_create_deceased_row, 1, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_2)

        self.combo_box_create_deceased_niche = QComboBox(self.scrollAreaWidgetContents_22)
        self.combo_box_create_deceased_niche.setObjectName(u"combo_box_create_deceased_niche")

        self.verticalLayout_14.addWidget(self.combo_box_create_deceased_niche)

        self.label_create_deceased_book = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_book.setObjectName(u"label_create_deceased_book")

        self.verticalLayout_14.addWidget(self.label_create_deceased_book)

        self.plain_text_edit_create_deceased_book = QPlainTextEdit(self.scrollAreaWidgetContents_22)
        self.plain_text_edit_create_deceased_book.setObjectName(u"plain_text_edit_create_deceased_book")

        self.verticalLayout_14.addWidget(self.plain_text_edit_create_deceased_book)

        self.label_create_deceased_sheet = QLabel(self.scrollAreaWidgetContents_22)
        self.label_create_deceased_sheet.setObjectName(u"label_create_deceased_sheet")

        self.verticalLayout_14.addWidget(self.label_create_deceased_sheet)

        self.plain_text_edit_create_deceased_sheet = QPlainTextEdit(self.scrollAreaWidgetContents_22)
        self.plain_text_edit_create_deceased_sheet.setObjectName(u"plain_text_edit_create_deceased_sheet")

        self.verticalLayout_14.addWidget(self.plain_text_edit_create_deceased_sheet)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_22)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.push_button_create_deceased_save_deceased = QPushButton(self.frame_18)
        self.push_button_create_deceased_save_deceased.setObjectName(u"push_button_create_deceased_save_deceased")

        self.horizontalLayout_15.addWidget(self.push_button_create_deceased_save_deceased)

        self.push_button_create_deceased_clean = QPushButton(self.frame_18)
        self.push_button_create_deceased_clean.setObjectName(u"push_button_create_deceased_clean")

        self.horizontalLayout_15.addWidget(self.push_button_create_deceased_clean)


        self.verticalLayout_14.addWidget(self.frame_18)

        self.scroll_area_create_deceased.setWidget(self.scrollAreaWidgetContents_22)

        self.gridLayout_11.addWidget(self.scroll_area_create_deceased, 1, 1, 1, 1)

        self.stacked_widget.addWidget(self.deceased)
        self.holders = QWidget()
        self.holders.setObjectName(u"holders")
        self.gridLayout_12 = QGridLayout(self.holders)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_holders_header = QFrame(self.holders)
        self.frame_holders_header.setObjectName(u"frame_holders_header")
        self.frame_holders_header.setStyleSheet(u"")
        self.frame_holders_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_holders_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_holders_header)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_holders = QLabel(self.frame_holders_header)
        self.label_holders.setObjectName(u"label_holders")

        self.horizontalLayout_16.addWidget(self.label_holders)

        self.horizontal_spacer_holders_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontal_spacer_holders_header)

        self.push_button_create_holder_create = QPushButton(self.frame_holders_header)
        self.push_button_create_holder_create.setObjectName(u"push_button_create_holder_create")

        self.horizontalLayout_16.addWidget(self.push_button_create_holder_create)


        self.gridLayout_12.addWidget(self.frame_holders_header, 0, 0, 1, 3)

        self.scroll_area_holders = QScrollArea(self.holders)
        self.scroll_area_holders.setObjectName(u"scroll_area_holders")
        self.scroll_area_holders.setWidgetResizable(True)
        self.scrollAreaWidgetContents_23 = QWidget()
        self.scrollAreaWidgetContents_23.setObjectName(u"scrollAreaWidgetContents_23")
        self.scrollAreaWidgetContents_23.setGeometry(QRect(0, 0, 98, 117))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_23)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line_edit_search_holders = QLineEdit(self.scrollAreaWidgetContents_23)
        self.line_edit_search_holders.setObjectName(u"line_edit_search_holders")

        self.gridLayout.addWidget(self.line_edit_search_holders, 0, 1, 1, 1)

        self.table_widget_holders = QTableWidget(self.scrollAreaWidgetContents_23)
        self.table_widget_holders.setObjectName(u"table_widget_holders")

        self.gridLayout.addWidget(self.table_widget_holders, 1, 0, 1, 2)

        self.scroll_area_holders.setWidget(self.scrollAreaWidgetContents_23)

        self.gridLayout_12.addWidget(self.scroll_area_holders, 1, 0, 1, 1)

        self.scroll_area_create_holder = QScrollArea(self.holders)
        self.scroll_area_create_holder.setObjectName(u"scroll_area_create_holder")
        self.scroll_area_create_holder.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_holder.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_create_holder.setWidgetResizable(True)
        self.scrollAreaWidgetContents_25 = QWidget()
        self.scrollAreaWidgetContents_25.setObjectName(u"scrollAreaWidgetContents_25")
        self.scrollAreaWidgetContents_25.setGeometry(QRect(0, 0, 194, 316))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents_25)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_create_holder = QLabel(self.scrollAreaWidgetContents_25)
        self.label_create_holder.setObjectName(u"label_create_holder")
        self.label_create_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_create_holder)

        self.horizontal_spacer_create_holder = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_16.addItem(self.horizontal_spacer_create_holder)

        self.label_create_holder_name = QLabel(self.scrollAreaWidgetContents_25)
        self.label_create_holder_name.setObjectName(u"label_create_holder_name")

        self.verticalLayout_16.addWidget(self.label_create_holder_name)

        self.line_edit_create_holder_name = QLineEdit(self.scrollAreaWidgetContents_25)
        self.line_edit_create_holder_name.setObjectName(u"line_edit_create_holder_name")

        self.verticalLayout_16.addWidget(self.line_edit_create_holder_name)

        self.label_create_holder_paternal_surname = QLabel(self.scrollAreaWidgetContents_25)
        self.label_create_holder_paternal_surname.setObjectName(u"label_create_holder_paternal_surname")

        self.verticalLayout_16.addWidget(self.label_create_holder_paternal_surname)

        self.line_edit_create_holder_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_25)
        self.line_edit_create_holder_paternal_surname.setObjectName(u"line_edit_create_holder_paternal_surname")

        self.verticalLayout_16.addWidget(self.line_edit_create_holder_paternal_surname)

        self.label_create_holder_maternal_surname = QLabel(self.scrollAreaWidgetContents_25)
        self.label_create_holder_maternal_surname.setObjectName(u"label_create_holder_maternal_surname")

        self.verticalLayout_16.addWidget(self.label_create_holder_maternal_surname)

        self.line_edit_create_holder_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_25)
        self.line_edit_create_holder_maternal_surname.setObjectName(u"line_edit_create_holder_maternal_surname")

        self.verticalLayout_16.addWidget(self.line_edit_create_holder_maternal_surname)

        self.label_create_holder_phone = QLabel(self.scrollAreaWidgetContents_25)
        self.label_create_holder_phone.setObjectName(u"label_create_holder_phone")

        self.verticalLayout_16.addWidget(self.label_create_holder_phone)

        self.line_edit_create_holder_phone = QLineEdit(self.scrollAreaWidgetContents_25)
        self.line_edit_create_holder_phone.setObjectName(u"line_edit_create_holder_phone")

        self.verticalLayout_16.addWidget(self.line_edit_create_holder_phone)

        self.vertical_spacer_create_holder = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.vertical_spacer_create_holder)

        self.frame_create_holder_buttons = QFrame(self.scrollAreaWidgetContents_25)
        self.frame_create_holder_buttons.setObjectName(u"frame_create_holder_buttons")
        self.frame_create_holder_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_create_holder_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_create_holder_buttons)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.push_button_create_holder_save_holder = QPushButton(self.frame_create_holder_buttons)
        self.push_button_create_holder_save_holder.setObjectName(u"push_button_create_holder_save_holder")

        self.horizontalLayout_18.addWidget(self.push_button_create_holder_save_holder)

        self.push_button_create_holder_clean_holder = QPushButton(self.frame_create_holder_buttons)
        self.push_button_create_holder_clean_holder.setObjectName(u"push_button_create_holder_clean_holder")

        self.horizontalLayout_18.addWidget(self.push_button_create_holder_clean_holder)


        self.verticalLayout_16.addWidget(self.frame_create_holder_buttons)

        self.scroll_area_create_holder.setWidget(self.scrollAreaWidgetContents_25)

        self.gridLayout_12.addWidget(self.scroll_area_create_holder, 1, 1, 1, 1)

        self.scroll_area_modify_holder = QScrollArea(self.holders)
        self.scroll_area_modify_holder.setObjectName(u"scroll_area_modify_holder")
        self.scroll_area_modify_holder.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_holder.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_modify_holder.setWidgetResizable(True)
        self.scrollAreaWidgetContents_24 = QWidget()
        self.scrollAreaWidgetContents_24.setObjectName(u"scrollAreaWidgetContents_24")
        self.scrollAreaWidgetContents_24.setGeometry(QRect(0, 0, 194, 346))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents_24)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_modify_holder = QLabel(self.scrollAreaWidgetContents_24)
        self.label_modify_holder.setObjectName(u"label_modify_holder")
        self.label_modify_holder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_modify_holder)

        self.horizontal_spacer_modify_holder = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_15.addItem(self.horizontal_spacer_modify_holder)

        self.label_modify_holder_name = QLabel(self.scrollAreaWidgetContents_24)
        self.label_modify_holder_name.setObjectName(u"label_modify_holder_name")

        self.verticalLayout_15.addWidget(self.label_modify_holder_name)

        self.line_edit_modify_holder_name = QLineEdit(self.scrollAreaWidgetContents_24)
        self.line_edit_modify_holder_name.setObjectName(u"line_edit_modify_holder_name")

        self.verticalLayout_15.addWidget(self.line_edit_modify_holder_name)

        self.label_modify_holder_paternal_surname = QLabel(self.scrollAreaWidgetContents_24)
        self.label_modify_holder_paternal_surname.setObjectName(u"label_modify_holder_paternal_surname")

        self.verticalLayout_15.addWidget(self.label_modify_holder_paternal_surname)

        self.line_edit_modify_holder_paternal_surname = QLineEdit(self.scrollAreaWidgetContents_24)
        self.line_edit_modify_holder_paternal_surname.setObjectName(u"line_edit_modify_holder_paternal_surname")

        self.verticalLayout_15.addWidget(self.line_edit_modify_holder_paternal_surname)

        self.label_modify_holder_maternal_surname = QLabel(self.scrollAreaWidgetContents_24)
        self.label_modify_holder_maternal_surname.setObjectName(u"label_modify_holder_maternal_surname")

        self.verticalLayout_15.addWidget(self.label_modify_holder_maternal_surname)

        self.line_edit_modify_holder_maternal_surname = QLineEdit(self.scrollAreaWidgetContents_24)
        self.line_edit_modify_holder_maternal_surname.setObjectName(u"line_edit_modify_holder_maternal_surname")

        self.verticalLayout_15.addWidget(self.line_edit_modify_holder_maternal_surname)

        self.label_modify_holder_name_phone = QLabel(self.scrollAreaWidgetContents_24)
        self.label_modify_holder_name_phone.setObjectName(u"label_modify_holder_name_phone")

        self.verticalLayout_15.addWidget(self.label_modify_holder_name_phone)

        self.line_edit_modify_holder_phone = QLineEdit(self.scrollAreaWidgetContents_24)
        self.line_edit_modify_holder_phone.setObjectName(u"line_edit_modify_holder_phone")

        self.verticalLayout_15.addWidget(self.line_edit_modify_holder_phone)

        self.vertical_spacer_modify_holder = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.vertical_spacer_modify_holder)

        self.frame_modify_holder_buttons = QFrame(self.scrollAreaWidgetContents_24)
        self.frame_modify_holder_buttons.setObjectName(u"frame_modify_holder_buttons")
        self.frame_modify_holder_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_modify_holder_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_modify_holder_buttons)
        self.formLayout.setObjectName(u"formLayout")
        self.push_button_modify_holder_activate = QPushButton(self.frame_modify_holder_buttons)
        self.push_button_modify_holder_activate.setObjectName(u"push_button_modify_holder_activate")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.push_button_modify_holder_activate)

        self.push_button_modify_holder_deactivate = QPushButton(self.frame_modify_holder_buttons)
        self.push_button_modify_holder_deactivate.setObjectName(u"push_button_modify_holder_deactivate")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.push_button_modify_holder_deactivate)

        self.push_button_modify_holder_save = QPushButton(self.frame_modify_holder_buttons)
        self.push_button_modify_holder_save.setObjectName(u"push_button_modify_holder_save")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.push_button_modify_holder_save)


        self.verticalLayout_15.addWidget(self.frame_modify_holder_buttons)

        self.scroll_area_modify_holder.setWidget(self.scrollAreaWidgetContents_24)

        self.gridLayout_12.addWidget(self.scroll_area_modify_holder, 1, 2, 1, 1)

        self.stacked_widget.addWidget(self.holders)
        self.niches = QWidget()
        self.niches.setObjectName(u"niches")
        self.gridLayout_4 = QGridLayout(self.niches)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.scroll_area_search_niches = QScrollArea(self.niches)
        self.scroll_area_search_niches.setObjectName(u"scroll_area_search_niches")
        self.scroll_area_search_niches.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 223, 432))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.table_widget_niches = QTableWidget(self.scrollAreaWidgetContents_5)
        self.table_widget_niches.setObjectName(u"table_widget_niches")

        self.gridLayout_8.addWidget(self.table_widget_niches, 1, 0, 1, 3)

        self.line_edit_search_niches = QLineEdit(self.scrollAreaWidgetContents_5)
        self.line_edit_search_niches.setObjectName(u"line_edit_search_niches")

        self.gridLayout_8.addWidget(self.line_edit_search_niches, 0, 2, 1, 1)

        self.horizontal_layout_niches_new_page = QHBoxLayout()
        self.horizontal_layout_niches_new_page.setObjectName(u"horizontal_layout_niches_new_page")
        self.horizontal_spacer_niches_new_page = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontal_layout_niches_new_page.addItem(self.horizontal_spacer_niches_new_page)

        self.push_button_niches_new_page = QPushButton(self.scrollAreaWidgetContents_5)
        self.push_button_niches_new_page.setObjectName(u"push_button_niches_new_page")

        self.horizontal_layout_niches_new_page.addWidget(self.push_button_niches_new_page)


        self.gridLayout_8.addLayout(self.horizontal_layout_niches_new_page, 3, 2, 1, 1)

        self.scroll_area_search_niches.setWidget(self.scrollAreaWidgetContents_5)

        self.gridLayout_4.addWidget(self.scroll_area_search_niches, 1, 0, 1, 1)

        self.scroll_area_modify_niche = QScrollArea(self.niches)
        self.scroll_area_modify_niche.setObjectName(u"scroll_area_modify_niche")
        self.scroll_area_modify_niche.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_niche.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_modify_niche.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 213, 432))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_modify_niche = QLabel(self.scrollAreaWidgetContents_7)
        self.label_modify_niche.setObjectName(u"label_modify_niche")
        self.label_modify_niche.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_modify_niche)

        self.horizontal_spacer_modify_niche = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_4.addItem(self.horizontal_spacer_modify_niche)

        self.label_modify_niche_name = QLabel(self.scrollAreaWidgetContents_7)
        self.label_modify_niche_name.setObjectName(u"label_modify_niche_name")
        self.label_modify_niche_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_modify_niche_name)

        self.label_holder_modify_niche = QLabel(self.scrollAreaWidgetContents_7)
        self.label_holder_modify_niche.setObjectName(u"label_holder_modify_niche")

        self.verticalLayout_4.addWidget(self.label_holder_modify_niche)

        self.line_edit_modify_niche_search_holder = QLineEdit(self.scrollAreaWidgetContents_7)
        self.line_edit_modify_niche_search_holder.setObjectName(u"line_edit_modify_niche_search_holder")

        self.verticalLayout_4.addWidget(self.line_edit_modify_niche_search_holder)

        self.combo_box_modify_niche_holder = QComboBox(self.scrollAreaWidgetContents_7)
        self.combo_box_modify_niche_holder.setObjectName(u"combo_box_modify_niche_holder")

        self.verticalLayout_4.addWidget(self.combo_box_modify_niche_holder)

        self.check_box_modify_niche_is_busy = QCheckBox(self.scrollAreaWidgetContents_7)
        self.check_box_modify_niche_is_busy.setObjectName(u"check_box_modify_niche_is_busy")

        self.verticalLayout_4.addWidget(self.check_box_modify_niche_is_busy)

        self.check_box_modify_niche_paid_off = QCheckBox(self.scrollAreaWidgetContents_7)
        self.check_box_modify_niche_paid_off.setObjectName(u"check_box_modify_niche_paid_off")

        self.verticalLayout_4.addWidget(self.check_box_modify_niche_paid_off)

        self.check_box_modify_niche_is_donated = QCheckBox(self.scrollAreaWidgetContents_7)
        self.check_box_modify_niche_is_donated.setObjectName(u"check_box_modify_niche_is_donated")

        self.verticalLayout_4.addWidget(self.check_box_modify_niche_is_donated)

        self.vertical_spacer_modify_niche = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.vertical_spacer_modify_niche)

        self.frame = QFrame(self.scrollAreaWidgetContents_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.push_button_modify_niche_activate = QPushButton(self.frame)
        self.push_button_modify_niche_activate.setObjectName(u"push_button_modify_niche_activate")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.push_button_modify_niche_activate)

        self.push_button_modify_niche_deactivate = QPushButton(self.frame)
        self.push_button_modify_niche_deactivate.setObjectName(u"push_button_modify_niche_deactivate")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.push_button_modify_niche_deactivate)

        self.push_button_modify_niche_save = QPushButton(self.frame)
        self.push_button_modify_niche_save.setObjectName(u"push_button_modify_niche_save")

        self.formLayout_4.setWidget(1, QFormLayout.SpanningRole, self.push_button_modify_niche_save)


        self.verticalLayout_4.addWidget(self.frame)

        self.scroll_area_modify_niche.setWidget(self.scrollAreaWidgetContents_7)

        self.gridLayout_4.addWidget(self.scroll_area_modify_niche, 1, 2, 1, 1)

        self.scroll_area_create_niche = QScrollArea(self.niches)
        self.scroll_area_create_niche.setObjectName(u"scroll_area_create_niche")
        self.scroll_area_create_niche.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_niche.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_create_niche.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 213, 432))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_create_niche = QLabel(self.scrollAreaWidgetContents_6)
        self.label_create_niche.setObjectName(u"label_create_niche")
        self.label_create_niche.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_create_niche)

        self.horizontal_spacer_create_niche = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontal_spacer_create_niche)

        self.label_number_create_niche = QLabel(self.scrollAreaWidgetContents_6)
        self.label_number_create_niche.setObjectName(u"label_number_create_niche")

        self.verticalLayout_3.addWidget(self.label_number_create_niche)

        self.spin_box_create_niche_number = QSpinBox(self.scrollAreaWidgetContents_6)
        self.spin_box_create_niche_number.setObjectName(u"spin_box_create_niche_number")
        self.spin_box_create_niche_number.setEnabled(False)

        self.verticalLayout_3.addWidget(self.spin_box_create_niche_number)

        self.label_holder_create_niche = QLabel(self.scrollAreaWidgetContents_6)
        self.label_holder_create_niche.setObjectName(u"label_holder_create_niche")

        self.verticalLayout_3.addWidget(self.label_holder_create_niche)

        self.line_edit_create_niche_holder_search = QLineEdit(self.scrollAreaWidgetContents_6)
        self.line_edit_create_niche_holder_search.setObjectName(u"line_edit_create_niche_holder_search")
        self.line_edit_create_niche_holder_search.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.line_edit_create_niche_holder_search.setDragEnabled(False)

        self.verticalLayout_3.addWidget(self.line_edit_create_niche_holder_search)

        self.combo_box_create_niche_holder = QComboBox(self.scrollAreaWidgetContents_6)
        self.combo_box_create_niche_holder.setObjectName(u"combo_box_create_niche_holder")

        self.verticalLayout_3.addWidget(self.combo_box_create_niche_holder)

        self.check_box_create_niche_is_busy = QCheckBox(self.scrollAreaWidgetContents_6)
        self.check_box_create_niche_is_busy.setObjectName(u"check_box_create_niche_is_busy")

        self.verticalLayout_3.addWidget(self.check_box_create_niche_is_busy)

        self.check_box_create_niche_is_paid_off = QCheckBox(self.scrollAreaWidgetContents_6)
        self.check_box_create_niche_is_paid_off.setObjectName(u"check_box_create_niche_is_paid_off")

        self.verticalLayout_3.addWidget(self.check_box_create_niche_is_paid_off)

        self.check_box_create_niche_is_donated = QCheckBox(self.scrollAreaWidgetContents_6)
        self.check_box_create_niche_is_donated.setObjectName(u"check_box_create_niche_is_donated")

        self.verticalLayout_3.addWidget(self.check_box_create_niche_is_donated)

        self.vertical_spacer_create_niche = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vertical_spacer_create_niche)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.push_button_create_niche_save_niche = QPushButton(self.frame_4)
        self.push_button_create_niche_save_niche.setObjectName(u"push_button_create_niche_save_niche")

        self.horizontalLayout_3.addWidget(self.push_button_create_niche_save_niche)

        self.push_button_create_niche_clean = QPushButton(self.frame_4)
        self.push_button_create_niche_clean.setObjectName(u"push_button_create_niche_clean")

        self.horizontalLayout_3.addWidget(self.push_button_create_niche_clean)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.scroll_area_create_niche.setWidget(self.scrollAreaWidgetContents_6)

        self.gridLayout_4.addWidget(self.scroll_area_create_niche, 1, 1, 1, 1)

        self.frame_niches_header = QFrame(self.niches)
        self.frame_niches_header.setObjectName(u"frame_niches_header")
        self.frame_niches_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_niches_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_niches_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_niches_header_detail = QFrame(self.frame_niches_header)
        self.frame_niches_header_detail.setObjectName(u"frame_niches_header_detail")
        self.frame_niches_header_detail.setMinimumSize(QSize(200, 0))
        self.frame_niches_header_detail.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_niches_header_detail.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_niches_header_detail)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_niches_row = QLabel(self.frame_niches_header_detail)
        self.label_niches_row.setObjectName(u"label_niches_row")

        self.gridLayout_6.addWidget(self.label_niches_row, 2, 0, 1, 1)

        self.horizontal_spacer_niches_detail_module = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontal_spacer_niches_detail_module, 1, 2, 1, 1)

        self.combo_box_niches_module = QComboBox(self.frame_niches_header_detail)
        self.combo_box_niches_module.setObjectName(u"combo_box_niches_module")

        self.gridLayout_6.addWidget(self.combo_box_niches_module, 1, 1, 1, 1)

        self.label_niches_module = QLabel(self.frame_niches_header_detail)
        self.label_niches_module.setObjectName(u"label_niches_module")

        self.gridLayout_6.addWidget(self.label_niches_module, 1, 0, 1, 1)

        self.horizontal_spacer_niches_detail_row = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontal_spacer_niches_detail_row, 2, 2, 1, 1)

        self.combo_box_niches_row = QComboBox(self.frame_niches_header_detail)
        self.combo_box_niches_row.setObjectName(u"combo_box_niches_row")

        self.gridLayout_6.addWidget(self.combo_box_niches_row, 2, 1, 1, 1)

        self.label_niches = QLabel(self.frame_niches_header_detail)
        self.label_niches.setObjectName(u"label_niches")

        self.gridLayout_6.addWidget(self.label_niches, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_niches_header_detail)

        self.frame_niches_header_buttons = QFrame(self.frame_niches_header)
        self.frame_niches_header_buttons.setObjectName(u"frame_niches_header_buttons")
        self.frame_niches_header_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_niches_header_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_niches_header_buttons)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.push_button_modules = QPushButton(self.frame_niches_header_buttons)
        self.push_button_modules.setObjectName(u"push_button_modules")
        sizePolicy.setHeightForWidth(self.push_button_modules.sizePolicy().hasHeightForWidth())
        self.push_button_modules.setSizePolicy(sizePolicy)
        self.push_button_modules.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon7 = QIcon()
        icon7.addFile(u":/icons/table.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_modules.setIcon(icon7)
        self.push_button_modules.setIconSize(QSize(20, 20))
        self.push_button_modules.setCheckable(False)
        self.push_button_modules.setFlat(True)

        self.gridLayout_5.addWidget(self.push_button_modules, 0, 1, 1, 1)

        self.push_button_rows = QPushButton(self.frame_niches_header_buttons)
        self.push_button_rows.setObjectName(u"push_button_rows")
        sizePolicy.setHeightForWidth(self.push_button_rows.sizePolicy().hasHeightForWidth())
        self.push_button_rows.setSizePolicy(sizePolicy)
        self.push_button_rows.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon8 = QIcon()
        icon8.addFile(u":/icons/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.push_button_rows.setIcon(icon8)
        self.push_button_rows.setIconSize(QSize(20, 20))
        self.push_button_rows.setCheckable(False)
        self.push_button_rows.setFlat(True)

        self.gridLayout_5.addWidget(self.push_button_rows, 1, 1, 1, 1)

        self.horizontal_spacer_niches_buttons_row = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontal_spacer_niches_buttons_row, 1, 0, 1, 1)

        self.horizontal_spacer_niches_buttons_modules = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontal_spacer_niches_buttons_modules, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_niches_header_buttons)

        self.horizontal_spacer_niches_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontal_spacer_niches_header)

        self.push_button_create_niches_create = QPushButton(self.frame_niches_header)
        self.push_button_create_niches_create.setObjectName(u"push_button_create_niches_create")

        self.horizontalLayout_2.addWidget(self.push_button_create_niches_create)


        self.gridLayout_4.addWidget(self.frame_niches_header, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.niches)
        self.my_account = QWidget()
        self.my_account.setObjectName(u"my_account")
        self.gridLayout_13 = QGridLayout(self.my_account)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.scroll_area_change_password = QScrollArea(self.my_account)
        self.scroll_area_change_password.setObjectName(u"scroll_area_change_password")
        self.scroll_area_change_password.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_change_password.setWidgetResizable(True)
        self.scrollAreaWidgetContents_28 = QWidget()
        self.scrollAreaWidgetContents_28.setObjectName(u"scrollAreaWidgetContents_28")
        self.scrollAreaWidgetContents_28.setGeometry(QRect(0, 0, 152, 266))
        self.verticalLayout_18 = QVBoxLayout(self.scrollAreaWidgetContents_28)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_my_account_change_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_change_password.setObjectName(u"label_my_account_change_password")
        self.label_my_account_change_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_my_account_change_password)

        self.horizontal_spacer_my_account_change_password = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_18.addItem(self.horizontal_spacer_my_account_change_password)

        self.label_my_account_current_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_current_password.setObjectName(u"label_my_account_current_password")

        self.verticalLayout_18.addWidget(self.label_my_account_current_password)

        self.line_edit_my_account_current_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_current_password.setObjectName(u"line_edit_my_account_current_password")
        self.line_edit_my_account_current_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_18.addWidget(self.line_edit_my_account_current_password)

        self.label_my_account_new_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_new_password.setObjectName(u"label_my_account_new_password")

        self.verticalLayout_18.addWidget(self.label_my_account_new_password)

        self.line_edit_my_account_new_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_new_password.setObjectName(u"line_edit_my_account_new_password")
        self.line_edit_my_account_new_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_18.addWidget(self.line_edit_my_account_new_password)

        self.label_my_account_repeat_new_password = QLabel(self.scrollAreaWidgetContents_28)
        self.label_my_account_repeat_new_password.setObjectName(u"label_my_account_repeat_new_password")

        self.verticalLayout_18.addWidget(self.label_my_account_repeat_new_password)

        self.line_edit_my_account_repeat_new_password = QLineEdit(self.scrollAreaWidgetContents_28)
        self.line_edit_my_account_repeat_new_password.setObjectName(u"line_edit_my_account_repeat_new_password")
        self.line_edit_my_account_repeat_new_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_18.addWidget(self.line_edit_my_account_repeat_new_password)

        self.vertical_spacer_my_account = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.vertical_spacer_my_account)

        self.frame_change_password = QFrame(self.scrollAreaWidgetContents_28)
        self.frame_change_password.setObjectName(u"frame_change_password")
        self.frame_change_password.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_change_password.setFrameShadow(QFrame.Shadow.Raised)
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
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_my_account_my_account = QLabel(self.frame_22)
        self.label_my_account_my_account.setObjectName(u"label_my_account_my_account")

        self.horizontalLayout_19.addWidget(self.label_my_account_my_account)

        self.horizontal_spacer_my_account_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontal_spacer_my_account_header)

        self.push_button_my_account_logout = QPushButton(self.frame_22)
        self.push_button_my_account_logout.setObjectName(u"push_button_my_account_logout")

        self.horizontalLayout_19.addWidget(self.push_button_my_account_logout)


        self.gridLayout_13.addWidget(self.frame_22, 0, 0, 1, 3)

        self.frame_8 = QFrame(self.my_account)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_my_account_user_name = QLabel(self.frame_8)
        self.label_my_account_user_name.setObjectName(u"label_my_account_user_name")

        self.horizontalLayout_5.addWidget(self.label_my_account_user_name)

        self.label_my_account_your_user_name = QLabel(self.frame_8)
        self.label_my_account_your_user_name.setObjectName(u"label_my_account_your_user_name")

        self.horizontalLayout_5.addWidget(self.label_my_account_your_user_name)

        self.horizontal_spacer_my_account_user_name = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontal_spacer_my_account_user_name)


        self.gridLayout_13.addWidget(self.frame_8, 1, 0, 1, 3)

        self.stacked_widget.addWidget(self.my_account)
        self.payments = QWidget()
        self.payments.setObjectName(u"payments")
        self.gridLayout_15 = QGridLayout(self.payments)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.scroll_area_payment_search = QScrollArea(self.payments)
        self.scroll_area_payment_search.setObjectName(u"scroll_area_payment_search")
        self.scroll_area_payment_search.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 109, 115))
        self.gridLayout_17 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_payment_search_total_value = QLabel(self.scrollAreaWidgetContents)
        self.label_payment_search_total_value.setObjectName(u"label_payment_search_total_value")

        self.gridLayout_17.addWidget(self.label_payment_search_total_value, 1, 1, 1, 1)

        self.label_payment_search_total = QLabel(self.scrollAreaWidgetContents)
        self.label_payment_search_total.setObjectName(u"label_payment_search_total")

        self.gridLayout_17.addWidget(self.label_payment_search_total, 1, 0, 1, 1)

        self.horizontal_spacer_search_payments = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontal_spacer_search_payments, 1, 2, 1, 1)

        self.table_widget_payments = QTableWidget(self.scrollAreaWidgetContents)
        self.table_widget_payments.setObjectName(u"table_widget_payments")

        self.gridLayout_17.addWidget(self.table_widget_payments, 0, 0, 1, 3)

        self.scroll_area_payment_search.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_15.addWidget(self.scroll_area_payment_search, 1, 0, 1, 1)

        self.scroll_area_payment_create = QScrollArea(self.payments)
        self.scroll_area_payment_create.setObjectName(u"scroll_area_payment_create")
        self.scroll_area_payment_create.setMinimumSize(QSize(215, 0))
        self.scroll_area_payment_create.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_payment_create.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 194, 315))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_payment_register = QLabel(self.scrollAreaWidgetContents_8)
        self.label_payment_register.setObjectName(u"label_payment_register")
        self.label_payment_register.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_payment_register)

        self.label_payment_create_quantity = QLabel(self.scrollAreaWidgetContents_8)
        self.label_payment_create_quantity.setObjectName(u"label_payment_create_quantity")

        self.verticalLayout_6.addWidget(self.label_payment_create_quantity)

        self.double_spin_box_payment_create_quantity = QDoubleSpinBox(self.scrollAreaWidgetContents_8)
        self.double_spin_box_payment_create_quantity.setObjectName(u"double_spin_box_payment_create_quantity")
        self.double_spin_box_payment_create_quantity.setMaximum(500000.989999999990687)

        self.verticalLayout_6.addWidget(self.double_spin_box_payment_create_quantity)

        self.label_payment_create_payment_date = QLabel(self.scrollAreaWidgetContents_8)
        self.label_payment_create_payment_date.setObjectName(u"label_payment_create_payment_date")

        self.verticalLayout_6.addWidget(self.label_payment_create_payment_date)

        self.date_edit_payment_create_payment_date = QDateEdit(self.scrollAreaWidgetContents_8)
        self.date_edit_payment_create_payment_date.setObjectName(u"date_edit_payment_create_payment_date")

        self.verticalLayout_6.addWidget(self.date_edit_payment_create_payment_date)

        self.label_payment_create_comments = QLabel(self.scrollAreaWidgetContents_8)
        self.label_payment_create_comments.setObjectName(u"label_payment_create_comments")

        self.verticalLayout_6.addWidget(self.label_payment_create_comments)

        self.plain_text_edit_payment_create_comments = QPlainTextEdit(self.scrollAreaWidgetContents_8)
        self.plain_text_edit_payment_create_comments.setObjectName(u"plain_text_edit_payment_create_comments")

        self.verticalLayout_6.addWidget(self.plain_text_edit_payment_create_comments)

        self.check_box_payment_create_is_paid_off = QCheckBox(self.scrollAreaWidgetContents_8)
        self.check_box_payment_create_is_paid_off.setObjectName(u"check_box_payment_create_is_paid_off")

        self.verticalLayout_6.addWidget(self.check_box_payment_create_is_paid_off)

        self.vertical_spacer_payment_create = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.vertical_spacer_payment_create)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.push_button_payment_create_save = QPushButton(self.frame_6)
        self.push_button_payment_create_save.setObjectName(u"push_button_payment_create_save")

        self.horizontalLayout_8.addWidget(self.push_button_payment_create_save)

        self.push_button_payment_create_clean = QPushButton(self.frame_6)
        self.push_button_payment_create_clean.setObjectName(u"push_button_payment_create_clean")

        self.horizontalLayout_8.addWidget(self.push_button_payment_create_clean)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.scroll_area_payment_create.setWidget(self.scrollAreaWidgetContents_8)

        self.gridLayout_15.addWidget(self.scroll_area_payment_create, 1, 1, 1, 1)

        self.scroll_area_payment_modify = QScrollArea(self.payments)
        self.scroll_area_payment_modify.setObjectName(u"scroll_area_payment_modify")
        self.scroll_area_payment_modify.setMinimumSize(QSize(215, 0))
        self.scroll_area_payment_modify.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_payment_modify.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 99, 269))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.scrollAreaWidgetContents_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.label_payment_modify_quantity = QLabel(self.scrollAreaWidgetContents_9)
        self.label_payment_modify_quantity.setObjectName(u"label_payment_modify_quantity")

        self.verticalLayout_7.addWidget(self.label_payment_modify_quantity)

        self.double_spin_box_payment_modify_quantity = QDoubleSpinBox(self.scrollAreaWidgetContents_9)
        self.double_spin_box_payment_modify_quantity.setObjectName(u"double_spin_box_payment_modify_quantity")
        self.double_spin_box_payment_modify_quantity.setMaximum(500000.989999999990687)

        self.verticalLayout_7.addWidget(self.double_spin_box_payment_modify_quantity)

        self.label_payment_modify_payment_date = QLabel(self.scrollAreaWidgetContents_9)
        self.label_payment_modify_payment_date.setObjectName(u"label_payment_modify_payment_date")

        self.verticalLayout_7.addWidget(self.label_payment_modify_payment_date)

        self.date_edit_payment_modify_payment_date = QDateEdit(self.scrollAreaWidgetContents_9)
        self.date_edit_payment_modify_payment_date.setObjectName(u"date_edit_payment_modify_payment_date")

        self.verticalLayout_7.addWidget(self.date_edit_payment_modify_payment_date)

        self.label_payment_modify_comments = QLabel(self.scrollAreaWidgetContents_9)
        self.label_payment_modify_comments.setObjectName(u"label_payment_modify_comments")

        self.verticalLayout_7.addWidget(self.label_payment_modify_comments)

        self.plain_text_edit_payment_modify_comments = QPlainTextEdit(self.scrollAreaWidgetContents_9)
        self.plain_text_edit_payment_modify_comments.setObjectName(u"plain_text_edit_payment_modify_comments")

        self.verticalLayout_7.addWidget(self.plain_text_edit_payment_modify_comments)

        self.vertical_spacer_payment_modify = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.vertical_spacer_payment_modify)

        self.push_button_payment_modify_save = QPushButton(self.scrollAreaWidgetContents_9)
        self.push_button_payment_modify_save.setObjectName(u"push_button_payment_modify_save")

        self.verticalLayout_7.addWidget(self.push_button_payment_modify_save)

        self.scroll_area_payment_modify.setWidget(self.scrollAreaWidgetContents_9)

        self.gridLayout_15.addWidget(self.scroll_area_payment_modify, 1, 2, 1, 1)

        self.frame_5 = QFrame(self.payments)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_payment_niche = QLabel(self.frame_7)
        self.label_payment_niche.setObjectName(u"label_payment_niche")

        self.gridLayout_16.addWidget(self.label_payment_niche, 4, 1, 1, 1)

        self.combo_box_payments_module = QComboBox(self.frame_7)
        self.combo_box_payments_module.setObjectName(u"combo_box_payments_module")

        self.gridLayout_16.addWidget(self.combo_box_payments_module, 1, 2, 1, 1)

        self.label_payment_module = QLabel(self.frame_7)
        self.label_payment_module.setObjectName(u"label_payment_module")

        self.gridLayout_16.addWidget(self.label_payment_module, 1, 1, 1, 1)

        self.combo_box_payment_niche = QComboBox(self.frame_7)
        self.combo_box_payment_niche.setObjectName(u"combo_box_payment_niche")

        self.gridLayout_16.addWidget(self.combo_box_payment_niche, 4, 2, 1, 1)

        self.combo_box_payments_row = QComboBox(self.frame_7)
        self.combo_box_payments_row.setObjectName(u"combo_box_payments_row")

        self.gridLayout_16.addWidget(self.combo_box_payments_row, 3, 2, 1, 1)

        self.label_payment_row = QLabel(self.frame_7)
        self.label_payment_row.setObjectName(u"label_payment_row")

        self.gridLayout_16.addWidget(self.label_payment_row, 3, 1, 1, 1)

        self.label_payments = QLabel(self.frame_7)
        self.label_payments.setObjectName(u"label_payments")

        self.gridLayout_16.addWidget(self.label_payments, 0, 1, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontal_spacer_payment_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontal_spacer_payment_header)

        self.push_button_payment_create = QPushButton(self.frame_9)
        self.push_button_payment_create.setObjectName(u"push_button_payment_create")

        self.horizontalLayout_6.addWidget(self.push_button_payment_create)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.gridLayout_15.addWidget(self.frame_5, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.payments)
        self.modules = QWidget()
        self.modules.setObjectName(u"modules")
        self.gridLayout_19 = QGridLayout(self.modules)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.scroll_area_module_search = QScrollArea(self.modules)
        self.scroll_area_module_search.setObjectName(u"scroll_area_module_search")
        self.scroll_area_module_search.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 98, 89))
        self.gridLayout_18 = QGridLayout(self.scrollAreaWidgetContents_10)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.table_widget_modules = QTableWidget(self.scrollAreaWidgetContents_10)
        self.table_widget_modules.setObjectName(u"table_widget_modules")

        self.gridLayout_18.addWidget(self.table_widget_modules, 0, 0, 1, 1)

        self.scroll_area_module_search.setWidget(self.scrollAreaWidgetContents_10)

        self.gridLayout_19.addWidget(self.scroll_area_module_search, 1, 0, 1, 1)

        self.scroll_area_create_module = QScrollArea(self.modules)
        self.scroll_area_create_module.setObjectName(u"scroll_area_create_module")
        self.scroll_area_create_module.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_module.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_create_module.setWidgetResizable(True)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 98, 120))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_create_module = QLabel(self.scrollAreaWidgetContents_11)
        self.label_create_module.setObjectName(u"label_create_module")
        self.label_create_module.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_create_module)

        self.label_create_module_name = QLabel(self.scrollAreaWidgetContents_11)
        self.label_create_module_name.setObjectName(u"label_create_module_name")

        self.verticalLayout_8.addWidget(self.label_create_module_name)

        self.line_edit_create_module_name = QLineEdit(self.scrollAreaWidgetContents_11)
        self.line_edit_create_module_name.setObjectName(u"line_edit_create_module_name")

        self.verticalLayout_8.addWidget(self.line_edit_create_module_name)

        self.vertical_spacer_create_module = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.vertical_spacer_create_module)

        self.push_button_create_module_save = QPushButton(self.scrollAreaWidgetContents_11)
        self.push_button_create_module_save.setObjectName(u"push_button_create_module_save")

        self.verticalLayout_8.addWidget(self.push_button_create_module_save)

        self.scroll_area_create_module.setWidget(self.scrollAreaWidgetContents_11)

        self.gridLayout_19.addWidget(self.scroll_area_create_module, 1, 1, 1, 1)

        self.scroll_area_modify_module = QScrollArea(self.modules)
        self.scroll_area_modify_module.setObjectName(u"scroll_area_modify_module")
        self.scroll_area_modify_module.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_module.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_modify_module.setWidgetResizable(True)
        self.scrollAreaWidgetContents_12 = QWidget()
        self.scrollAreaWidgetContents_12.setObjectName(u"scrollAreaWidgetContents_12")
        self.scrollAreaWidgetContents_12.setGeometry(QRect(0, 0, 194, 170))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_12)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_modify_module = QLabel(self.scrollAreaWidgetContents_12)
        self.label_modify_module.setObjectName(u"label_modify_module")
        self.label_modify_module.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_modify_module)

        self.label_modify_module_name = QLabel(self.scrollAreaWidgetContents_12)
        self.label_modify_module_name.setObjectName(u"label_modify_module_name")

        self.verticalLayout_9.addWidget(self.label_modify_module_name)

        self.line_edit_modify_module_name = QLineEdit(self.scrollAreaWidgetContents_12)
        self.line_edit_modify_module_name.setObjectName(u"line_edit_modify_module_name")

        self.verticalLayout_9.addWidget(self.line_edit_modify_module_name)

        self.vertical_spacer_modify_module = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.vertical_spacer_modify_module)

        self.frame_modify_module_buttons = QFrame(self.scrollAreaWidgetContents_12)
        self.frame_modify_module_buttons.setObjectName(u"frame_modify_module_buttons")
        self.frame_modify_module_buttons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_modify_module_buttons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_modify_module_buttons)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.push_button_modify_module_activate = QPushButton(self.frame_modify_module_buttons)
        self.push_button_modify_module_activate.setObjectName(u"push_button_modify_module_activate")

        self.horizontalLayout_10.addWidget(self.push_button_modify_module_activate)

        self.push_button_modify_module_deactivate = QPushButton(self.frame_modify_module_buttons)
        self.push_button_modify_module_deactivate.setObjectName(u"push_button_modify_module_deactivate")

        self.horizontalLayout_10.addWidget(self.push_button_modify_module_deactivate)


        self.verticalLayout_9.addWidget(self.frame_modify_module_buttons)

        self.push_button_modify_module_save = QPushButton(self.scrollAreaWidgetContents_12)
        self.push_button_modify_module_save.setObjectName(u"push_button_modify_module_save")

        self.verticalLayout_9.addWidget(self.push_button_modify_module_save)

        self.scroll_area_modify_module.setWidget(self.scrollAreaWidgetContents_12)

        self.gridLayout_19.addWidget(self.scroll_area_modify_module, 1, 2, 1, 1)

        self.frame_modules_header = QFrame(self.modules)
        self.frame_modules_header.setObjectName(u"frame_modules_header")
        self.frame_modules_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_modules_header.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_modules_header)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_module = QLabel(self.frame_modules_header)
        self.label_module.setObjectName(u"label_module")

        self.horizontalLayout_9.addWidget(self.label_module)

        self.horizontal_spacer_module_header = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontal_spacer_module_header)

        self.push_button_module_create = QPushButton(self.frame_modules_header)
        self.push_button_module_create.setObjectName(u"push_button_module_create")

        self.horizontalLayout_9.addWidget(self.push_button_module_create)

        self.push_button_modules_return = QPushButton(self.frame_modules_header)
        self.push_button_modules_return.setObjectName(u"push_button_modules_return")

        self.horizontalLayout_9.addWidget(self.push_button_modules_return)


        self.gridLayout_19.addWidget(self.frame_modules_header, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.modules)
        self.rows = QWidget()
        self.rows.setObjectName(u"rows")
        self.gridLayout_20 = QGridLayout(self.rows)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.scroll_area_create_row = QScrollArea(self.rows)
        self.scroll_area_create_row.setObjectName(u"scroll_area_create_row")
        self.scroll_area_create_row.setMinimumSize(QSize(215, 0))
        self.scroll_area_create_row.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_create_row.setWidgetResizable(True)
        self.scrollAreaWidgetContents_14 = QWidget()
        self.scrollAreaWidgetContents_14.setObjectName(u"scrollAreaWidgetContents_14")
        self.scrollAreaWidgetContents_14.setGeometry(QRect(0, 0, 98, 120))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_create_row = QLabel(self.scrollAreaWidgetContents_14)
        self.label_create_row.setObjectName(u"label_create_row")
        self.label_create_row.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_create_row)

        self.label_create_row_name = QLabel(self.scrollAreaWidgetContents_14)
        self.label_create_row_name.setObjectName(u"label_create_row_name")

        self.verticalLayout_10.addWidget(self.label_create_row_name)

        self.line_edit_create_row_name = QLineEdit(self.scrollAreaWidgetContents_14)
        self.line_edit_create_row_name.setObjectName(u"line_edit_create_row_name")

        self.verticalLayout_10.addWidget(self.line_edit_create_row_name)

        self.vertical_spacer_create_row = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.vertical_spacer_create_row)

        self.push_button_create_row_save = QPushButton(self.scrollAreaWidgetContents_14)
        self.push_button_create_row_save.setObjectName(u"push_button_create_row_save")

        self.verticalLayout_10.addWidget(self.push_button_create_row_save)

        self.scroll_area_create_row.setWidget(self.scrollAreaWidgetContents_14)

        self.gridLayout_20.addWidget(self.scroll_area_create_row, 1, 1, 1, 1)

        self.scroll_area_modify_row = QScrollArea(self.rows)
        self.scroll_area_modify_row.setObjectName(u"scroll_area_modify_row")
        self.scroll_area_modify_row.setMinimumSize(QSize(215, 0))
        self.scroll_area_modify_row.setMaximumSize(QSize(215, 16777215))
        self.scroll_area_modify_row.setWidgetResizable(True)
        self.scrollAreaWidgetContents_15 = QWidget()
        self.scrollAreaWidgetContents_15.setObjectName(u"scrollAreaWidgetContents_15")
        self.scrollAreaWidgetContents_15.setGeometry(QRect(0, 0, 98, 120))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_15)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_modify_row = QLabel(self.scrollAreaWidgetContents_15)
        self.label_modify_row.setObjectName(u"label_modify_row")
        self.label_modify_row.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_modify_row)

        self.label_modify_row_name = QLabel(self.scrollAreaWidgetContents_15)
        self.label_modify_row_name.setObjectName(u"label_modify_row_name")

        self.verticalLayout_11.addWidget(self.label_modify_row_name)

        self.line_edit_modify_row_name = QLineEdit(self.scrollAreaWidgetContents_15)
        self.line_edit_modify_row_name.setObjectName(u"line_edit_modify_row_name")

        self.verticalLayout_11.addWidget(self.line_edit_modify_row_name)

        self.vertical_spacer_modify_row = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.vertical_spacer_modify_row)

        self.push_button_modify_row_save = QPushButton(self.scrollAreaWidgetContents_15)
        self.push_button_modify_row_save.setObjectName(u"push_button_modify_row_save")

        self.verticalLayout_11.addWidget(self.push_button_modify_row_save)

        self.scroll_area_modify_row.setWidget(self.scrollAreaWidgetContents_15)

        self.gridLayout_20.addWidget(self.scroll_area_modify_row, 1, 2, 1, 1)

        self.scroll_area_rows_search = QScrollArea(self.rows)
        self.scroll_area_rows_search.setObjectName(u"scroll_area_rows_search")
        self.scroll_area_rows_search.setWidgetResizable(True)
        self.scrollAreaWidgetContents_13 = QWidget()
        self.scrollAreaWidgetContents_13.setObjectName(u"scrollAreaWidgetContents_13")
        self.scrollAreaWidgetContents_13.setGeometry(QRect(0, 0, 98, 89))
        self.gridLayout_23 = QGridLayout(self.scrollAreaWidgetContents_13)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.table_widget_rows_search = QTableWidget(self.scrollAreaWidgetContents_13)
        self.table_widget_rows_search.setObjectName(u"table_widget_rows_search")

        self.gridLayout_23.addWidget(self.table_widget_rows_search, 0, 0, 1, 1)

        self.scroll_area_rows_search.setWidget(self.scrollAreaWidgetContents_13)

        self.gridLayout_20.addWidget(self.scroll_area_rows_search, 1, 0, 1, 1)

        self.frame_10 = QFrame(self.rows)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_10)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.push_button_row_create = QPushButton(self.frame_10)
        self.push_button_row_create.setObjectName(u"push_button_row_create")

        self.gridLayout_21.addWidget(self.push_button_row_create, 0, 3, 1, 1)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_11)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_row_module = QLabel(self.frame_11)
        self.label_row_module.setObjectName(u"label_row_module")

        self.gridLayout_22.addWidget(self.label_row_module, 1, 0, 1, 1)

        self.combo_box_row_module = QComboBox(self.frame_11)
        self.combo_box_row_module.setObjectName(u"combo_box_row_module")
        self.combo_box_row_module.setMinimumSize(QSize(65, 0))

        self.gridLayout_22.addWidget(self.combo_box_row_module, 1, 1, 1, 1)

        self.label_rows = QLabel(self.frame_11)
        self.label_rows.setObjectName(u"label_rows")

        self.gridLayout_22.addWidget(self.label_rows, 0, 0, 1, 2)


        self.gridLayout_21.addWidget(self.frame_11, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.push_button_rows_return = QPushButton(self.frame_10)
        self.push_button_rows_return.setObjectName(u"push_button_rows_return")

        self.gridLayout_21.addWidget(self.push_button_rows_return, 0, 4, 1, 1)


        self.gridLayout_20.addWidget(self.frame_10, 0, 0, 1, 3)

        self.stacked_widget.addWidget(self.rows)

        self.horizontalLayout_7.addWidget(self.stacked_widget)

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
        self.stacked_widget.setCurrentIndex(4)


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
        self.push_button_payments.setText(QCoreApplication.translate("MainWindow", u"Pagos", None))
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
        self.line_edit_search_users.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar usuario...", None))
        self.label_users.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.push_button_create_user_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_modify_deceased.setText(QCoreApplication.translate("MainWindow", u"Modificar fallecido", None))
        self.label_modify_deceased_image.setText(QCoreApplication.translate("MainWindow", u"Sin imagen", None))
        self.push_button_modify_deceased_image.setText(QCoreApplication.translate("MainWindow", u"Cargar imagen...", None))
        self.label_modify_deceased_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_modify_deceased_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_modify_deceased_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_modify_deceased_birth_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento", None))
        self.checkBox_modify_deceased_birth_date.setText(QCoreApplication.translate("MainWindow", u"Desconocido", None))
        self.label_modify_deceased_death_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de defunci\u00f3n", None))
        self.checkBox_modify_deceased_death_date.setText(QCoreApplication.translate("MainWindow", u"Desconocido", None))
        self.label__modify_deceased_remaint_type.setText(QCoreApplication.translate("MainWindow", u"Tipo de restos:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Nicho:", None))
        self.label_modify_deceased_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_modify_deceased_row.setText(QCoreApplication.translate("MainWindow", u"Fila:", None))
        self.label_modify_deceased_book.setText(QCoreApplication.translate("MainWindow", u"Libro:", None))
        self.label_modify_deceased_sheet.setText(QCoreApplication.translate("MainWindow", u"Foja", None))
        self.push_button_modify_deceased_active.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.push_button_modify_deceased_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_modify_deceased_deactivate.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.label_deceased.setText(QCoreApplication.translate("MainWindow", u"Fallecidos", None))
        self.push_button_create_deceased_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.line_edit_search_deceased.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar fallecido...", None))
        self.label_create_deceased.setText(QCoreApplication.translate("MainWindow", u"Crear fallecido", None))
        self.label_create_deceased_image.setText(QCoreApplication.translate("MainWindow", u"Sin imagen", None))
        self.push_button_create_deceased_image.setText(QCoreApplication.translate("MainWindow", u"Cargar imagen...", None))
        self.label_create_deceased_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_create_deceased_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_create_deceased_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_create_deceased_birth_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de nacimiento:", None))
        self.checkbox_create_deceased_birth_date.setText(QCoreApplication.translate("MainWindow", u"Desconocido", None))
        self.label_create_deceased_death_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de defunci\u00f3n:", None))
        self.checkBox_create_deceased_death_date.setText(QCoreApplication.translate("MainWindow", u"Desconocido", None))
        self.label_create_deceased_remain_type.setText(QCoreApplication.translate("MainWindow", u"Tipo de restos:", None))
        self.label_create_deceased_niche.setText(QCoreApplication.translate("MainWindow", u"Nicho:", None))
        self.label_create_deceased_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_create_deceased_row.setText(QCoreApplication.translate("MainWindow", u"Fila:", None))
        self.label_create_deceased_book.setText(QCoreApplication.translate("MainWindow", u"Libro:", None))
        self.label_create_deceased_sheet.setText(QCoreApplication.translate("MainWindow", u"Foja:", None))
        self.push_button_create_deceased_save_deceased.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_create_deceased_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_holders.setText(QCoreApplication.translate("MainWindow", u"Titulares", None))
        self.push_button_create_holder_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.line_edit_search_holders.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar titular...", None))
        self.label_create_holder.setText(QCoreApplication.translate("MainWindow", u"Crear titular", None))
        self.label_create_holder_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_create_holder_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_create_holder_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno:", None))
        self.label_create_holder_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.push_button_create_holder_save_holder.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_create_holder_clean_holder.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_modify_holder.setText(QCoreApplication.translate("MainWindow", u"Modificar titular", None))
        self.label_modify_holder_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_modify_holder_paternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Paterno:", None))
        self.label_modify_holder_maternal_surname.setText(QCoreApplication.translate("MainWindow", u"Apellido Materno", None))
        self.label_modify_holder_name_phone.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono:", None))
        self.push_button_modify_holder_activate.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.push_button_modify_holder_deactivate.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.push_button_modify_holder_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.line_edit_search_niches.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar nicho...", None))
        self.push_button_niches_new_page.setText(QCoreApplication.translate("MainWindow", u" >", None))
        self.label_modify_niche.setText(QCoreApplication.translate("MainWindow", u"Modificar nicho", None))
        self.label_modify_niche_name.setText(QCoreApplication.translate("MainWindow", u"nombre", None))
        self.label_holder_modify_niche.setText(QCoreApplication.translate("MainWindow", u"Titular:", None))
        self.line_edit_modify_niche_search_holder.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar titular...", None))
        self.check_box_modify_niche_is_busy.setText(QCoreApplication.translate("MainWindow", u"Ocupado", None))
        self.check_box_modify_niche_paid_off.setText(QCoreApplication.translate("MainWindow", u"Pagado", None))
        self.check_box_modify_niche_is_donated.setText(QCoreApplication.translate("MainWindow", u"Donado", None))
        self.push_button_modify_niche_activate.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.push_button_modify_niche_deactivate.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.push_button_modify_niche_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_create_niche.setText(QCoreApplication.translate("MainWindow", u"Crear nicho", None))
        self.label_number_create_niche.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.label_holder_create_niche.setText(QCoreApplication.translate("MainWindow", u"Titular:", None))
        self.line_edit_create_niche_holder_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Buscar titular...", None))
        self.check_box_create_niche_is_busy.setText(QCoreApplication.translate("MainWindow", u"Ocupado", None))
        self.check_box_create_niche_is_paid_off.setText(QCoreApplication.translate("MainWindow", u"Pagado", None))
        self.check_box_create_niche_is_donated.setText(QCoreApplication.translate("MainWindow", u"Donado", None))
        self.push_button_create_niche_save_niche.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_create_niche_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_niches_row.setText(QCoreApplication.translate("MainWindow", u"Fila:", None))
        self.label_niches_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_niches.setText(QCoreApplication.translate("MainWindow", u"Nichos", None))
        self.push_button_modules.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulos", None))
        self.push_button_rows.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
        self.push_button_create_niches_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_my_account_change_password.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a:", None))
        self.label_my_account_current_password.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a actual:", None))
        self.label_my_account_new_password.setText(QCoreApplication.translate("MainWindow", u"Nueva contrase\u00f1a:", None))
        self.label_my_account_repeat_new_password.setText(QCoreApplication.translate("MainWindow", u"Repetir contrase\u00f1a:", None))
        self.push_button_change_password.setText(QCoreApplication.translate("MainWindow", u"Cambiar contrase\u00f1a", None))
        self.label_my_account_my_account.setText(QCoreApplication.translate("MainWindow", u"Mi cuenta", None))
        self.push_button_my_account_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label_my_account_user_name.setText(QCoreApplication.translate("MainWindow", u"Nombre de usuario:", None))
        self.label_my_account_your_user_name.setText(QCoreApplication.translate("MainWindow", u"your_user_name", None))
        self.label_payment_search_total_value.setText(QCoreApplication.translate("MainWindow", u"0.00 MXN", None))
        self.label_payment_search_total.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_payment_register.setText(QCoreApplication.translate("MainWindow", u"Registrar pago", None))
        self.label_payment_create_quantity.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_payment_create_payment_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de pago:", None))
        self.label_payment_create_comments.setText(QCoreApplication.translate("MainWindow", u"Comentarios:", None))
        self.check_box_payment_create_is_paid_off.setText(QCoreApplication.translate("MainWindow", u"Pagado", None))
        self.push_button_payment_create_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_payment_create_clean.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Modificar pago", None))
        self.label_payment_modify_quantity.setText(QCoreApplication.translate("MainWindow", u"Cantidad:", None))
        self.label_payment_modify_payment_date.setText(QCoreApplication.translate("MainWindow", u"Fecha de pago:", None))
        self.label_payment_modify_comments.setText(QCoreApplication.translate("MainWindow", u"Comentarios:", None))
        self.push_button_payment_modify_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_payment_niche.setText(QCoreApplication.translate("MainWindow", u"Nicho:", None))
        self.label_payment_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_payment_row.setText(QCoreApplication.translate("MainWindow", u"Fila:", None))
        self.label_payments.setText(QCoreApplication.translate("MainWindow", u"Pagos", None))
        self.push_button_payment_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_create_module.setText(QCoreApplication.translate("MainWindow", u"Crear m\u00f3dulo", None))
        self.label_create_module_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.push_button_create_module_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_modify_module.setText(QCoreApplication.translate("MainWindow", u"Modificar m\u00f3dulo", None))
        self.label_modify_module_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.push_button_modify_module_activate.setText(QCoreApplication.translate("MainWindow", u"Activar", None))
        self.push_button_modify_module_deactivate.setText(QCoreApplication.translate("MainWindow", u"Desactivar", None))
        self.push_button_modify_module_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulos", None))
        self.push_button_module_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.push_button_modules_return.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
        self.label_create_row.setText(QCoreApplication.translate("MainWindow", u"Crear fila", None))
        self.label_create_row_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.push_button_create_row_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.label_modify_row.setText(QCoreApplication.translate("MainWindow", u"Modificar fila", None))
        self.label_modify_row_name.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.push_button_modify_row_save.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.push_button_row_create.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.label_row_module.setText(QCoreApplication.translate("MainWindow", u"M\u00f3dulo:", None))
        self.label_rows.setText(QCoreApplication.translate("MainWindow", u"Filas", None))
        self.push_button_rows_return.setText(QCoreApplication.translate("MainWindow", u"Regresar", None))
    # retranslateUi

