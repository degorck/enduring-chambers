from niches.util.DbConnection import *
from niches.model.entity.UserType import UserType
from niches.model.mapper.UserTypeDaoMapper import UserTypeDaoMapper
import logging

class UserTypeDao:
    def __init__(self):
        self.__db_connection = DbConnection()
        self.__user_type_dao_mapper = UserTypeDaoMapper()

    def find_by_id(self, id:int):
        command = ('''
                   SELECT * 
                   FROM tb_user_type
                   WHERE
                   id = %s
                   ''')
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % id)
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
        command = ('''
                   SELECT * 
                   FROM tb_user_type
                   ''')
        
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