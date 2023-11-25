from niches.util.DatabaseConnection import DatabaseConnection
import psycopg2
from niches.model.entity.User import User
from niches.util.Encryptor import Encryptor
import datetime
from niches.model.mapper.UserDaoMapper import UserDaoMapper
import logging

class UserDao:
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__user_dao_mapper = UserDaoMapper()
        self.__encryptor = Encryptor()
        
    def create_user(self, user:User):
        command = '''
                INSERT INTO tb_user(
                    name,
                    paternal_surname,
                    maternal_surname,
                    user_type_id,
                    user_name,
                    password,
                    is_active,
                    created_at,
                    updated_at)
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)
                '''
        values = (
            user.get_name(),
            user.get_paternal_surname(),
            user.get_maternal_surname(),
            user.get_user_type_id(),
            user.get_user_name(),
            self.__encryptor.hash_password(user.get_password()),
            True,
            datetime.datetime.now(),
            datetime.datetime.now()
            )
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.get_cursor().execute('SELECT LASTVAL()')
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            logging.debug("Se creó el usuario")
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        
    def modify_user(self, user:User):
        command = ('''
                   UPDATE tb_user
                   SET
                   name = %s,
                   paternal_surname = %s,
                   maternal_surname = %s,
                   user_type_id = %s,
                   updated_at = %s
                   WHERE id = %s
                   ''')
        values = (
            user.get_name(),
            user.get_paternal_surname(),
            user.get_maternal_surname(),
            user.get_user_type_id(),
            datetime.datetime.now(),
            user.get_id()
            )
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el usuario")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        


    def deactivate_user(self, id:int):
        command = ('''
                   UPDATE tb_user
                   SET
                   is_active = %s,
                   updated_at = %s
                   WHERE id = %s
                   ''')
        values = (
            False,
            datetime.datetime.now(),
            id
            )
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se desactivó el usuario")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def reactivate_user(self, id:int):
        command = ('''
                   UPDATE tb_user
                   SET
                   is_active = %s,
                   updated_at = %s
                   WHERE id = %s
                   ''')
        values = (
            True,
            datetime.datetime.now(),
            id
            )
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se reactivó el usuario")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.error(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def change_user_password(self, id:int, password:str):
        command = ('''
                   UPDATE tb_user
                   SET
                   password = %s,
                   updated_at = %s
                   WHERE id = %s
                   ''')
        values = (
            self.__encryptor.hash_password(password),
            datetime.datetime.now(),
            id
            )
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se cambió la contraseña")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error
        
        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
    
    def search_users(self, search_string:str):
        search_string = "%" + search_string + "%"
        user_list = []
        command = ('''
                   SELECT * FROM tb_user
                   WHERE
                   name LIKE %s OR
                   paternal_surname LIKE %s OR
                   maternal_surname LIKE %s OR
                   user_name LIKE %s OR
                   CONCAT (name , ' ', paternal_surname, ' ', maternal_surname) LIKE %s
                   ''')
        
        values = (
            search_string,
            search_string,
            search_string,
            search_string,
            search_string)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                user = self.__user_dao_mapper.real_dict_row_to_user(row)
                user_list.append(user)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los usuarios")
            return user_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()        

    def search_active_users(self, search_string:str):
        search_string = "%" + search_string + "%"
        user_list = []
        command = ('''
                   SELECT * FROM tb_user
                   WHERE
                   name LIKE %s OR
                   paternal_surname LIKE %s OR
                   maternal_surname LIKE %s OR
                   user_name LIKE %s OR
                   CONCAT (name , ' ', paternal_surname, ' ', maternal_surname) LIKE %s
                   AND
                   is_active = True
                   ''')
        
        values = (
            search_string,
            search_string,
            search_string,
            search_string,
            search_string)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                user = self.__user_dao_mapper.real_dict_row_to_user(row)
                user_list.append(user)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron los usuarios activos")
            return user_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()        
    
    def find_by_id(self, id:int):
        command = ('''
                   SELECT * 
                   FROM tb_user
                   WHERE
                   id = %s
                   ''')
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            user = self.__user_dao_mapper.real_dict_row_to_user(row)
            logging.debug("Se buscó el usuario por su id")
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        
    def find_active_user_by_user_name(self, user_name:str):
        user_name = "'" + user_name + "'"
        command = ('''
                   SELECT * 
                   FROM tb_user
                   WHERE
                   user_name = %s
                   AND
                   is_active = True
                   ''')
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % user_name)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            if row != None:
                user = self.__user_dao_mapper.real_dict_row_to_user(row)
                logging.debug("Se buscó el usuario activo por su nombre de usuario")
                return user
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()