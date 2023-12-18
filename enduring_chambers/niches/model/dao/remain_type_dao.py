"""
Remain Type Dao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.remain_type import RemainType
from niches.model.mapper.dao.remain_type_dao_mapper import real_dict_row_to_remain_type

class RemainTypeDao:
    """
    Class with the functionality of RemainTypeDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def find_by_id(self, remain_type_id:int):
        """
        Find the remain type by its id

        Arguments:
            remain_type_id: int
                remain_type_id of the remain type to find
        Returns:
            remain_type : RemainType
                 Remain type entity found 
        """
        command = '''
                SELECT * 
                FROM tb_remain_type
                WHERE
                id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % remain_type_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            remain_type = RemainType()
            remain_type =  real_dict_row_to_remain_type(row)
            logging.debug("Se encontró un tipo de resto por su id")
            return remain_type
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all(self):
        """
        Find the all the remain_types

        Returns:
            remain_type_list : list<RemainType>
                All the remain types list
        """
        command = '''
                SELECT * 
                FROM tb_remain_type
                ORDER BY id
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_remain_type = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                remain_type = RemainType()
                remain_type =  real_dict_row_to_remain_type(row)
                list_remain_type.append(remain_type)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los tipos de resto")
            return list_remain_type

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
