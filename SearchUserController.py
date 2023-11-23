import sys
import PySide6.QtCore as QtCore
import PySide6.QtWidgets as QtWidgets
from Ui_SearchUser import Ui_SearchUser
from UserDao import UserDao
from UserDto import UserDto
from UserMapper import UserMapper
from ModifyUserController import ModifyUserController


class SearchUserController(QtWidgets.QMainWindow, Ui_SearchUser):
    def __init__(self):
        super(SearchUserController, self).__init__()
        self.setupUi(self)
        self.__row = 0
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()
        self.__modify_user_controller = ModifyUserController()
        self.line_edit_search.textChanged.connect(self.__search_users)
        self.table_widget_users.cellDoubleClicked.connect(self.__select_user)
        self.__configure_table()

    def __select_user(self):
        row = self.table_widget_users.currentRow()
        user_id = int(self.table_widget_users.item(row, 0).text())
        print(user_id)
        self.__modify_user_controller.load_user(user_id)
        self.__modify_user_controller.show()


    def __configure_table(self):
        self.table_widget_users.clear()
        self.table_widget_users.setRowCount(self.__row)
        self.table_widget_users.setColumnCount(8)
        self.table_widget_users.setHorizontalHeaderLabels(("id", "Nombre", "Apellido Paterno", "Apellido Materno", "Tipo de usuario", "Activo", "Creado", "Actualizado"))
        self.table_widget_users.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def __search_users(self):
        self.list_widget_users.clear()
        list_user_dto = []
        list_user = []
        list_user = self.__user_dao.search_user(self.line_edit_search.text())
        self.__row = len(list_user)
        self.__configure_table()
        row = 0
        for user in list_user:
            user_dto = UserDto()
            user_dto = self.__user_mapper.user_to_user_dto(user)
            list_user_dto.append(user_dto)
            self.list_widget_users.addItem("[" + str(user_dto.get_id()) + "] " + 
                                           user_dto.get_name() + " " +
                                           user_dto.get_paternal_surname() + " " +
                                           user_dto.get_maternal_surname())
            self.table_widget_users.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user_dto.get_id())))
            self.table_widget_users.setItem(row, 1, QtWidgets.QTableWidgetItem(user_dto.get_name()))
            self.table_widget_users.setItem(row, 2, QtWidgets.QTableWidgetItem(user_dto.get_paternal_surname()))
            self.table_widget_users.setItem(row, 3, QtWidgets.QTableWidgetItem(user_dto.get_maternal_surname()))
            self.table_widget_users.setItem(row, 4, QtWidgets.QTableWidgetItem(str(user_dto.get_user_type_id())))
            self.table_widget_users.setItem(row, 5, QtWidgets.QTableWidgetItem(str(user_dto.is_active())))
            self.table_widget_users.setItem(row, 6, QtWidgets.QTableWidgetItem(str(user_dto.get_created_at())))
            self.table_widget_users.setItem(row, 7, QtWidgets.QTableWidgetItem(str(user_dto.get_updated_at())))
            row = row + 1

if __name__ == "__main__": 
    app = QtWidgets.QApplication(sys.argv)
    window = SearchUserController()
    window.show()
    sys.exit(app.exec())