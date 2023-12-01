"""
User Type Dao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.user_type import UserType
from niches.model.mapper.dao.user_type_dao_mapper import UserTypeDaoMapper

class UserTypeDao:
    """
    Class with the functionality of UserTypeDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__user_type_dao_mapper = UserTypeDaoMapper()

    def find_by_id(self, user_type_id:int):
        """
        Find the user type by its id

        Args:
            user_type_id: int
                user_type_id of the user type to find
        Returns:
            user_type : UserType
                 User type entity found 
        """
        command = '''
                SELECT * 
                FROM tb_user_type
                WHERE
                id_user_type = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % user_type_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            user_type = UserType()
            user_type =  self.__user_type_dao_mapper.real_dict_row_to_user(row)
            logging.debug("Se encontró un usuario por su id")
            return user_type
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all(self):
        """
        Find the all the user_types

        Returns:
            user_type_list : list<UserType>
                All the user types list
        """
        command = '''
                SELECT * 
                FROM tb_user_type
                ORDER BY id_user_type
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_user_type = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                user_type = UserType()
                user_type =  self.__user_type_dao_mapper.real_dict_row_to_user(row)
                list_user_type.append(user_type)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los usuarios")
            return list_user_type

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
