import repackage
from DbConnection import *
from User import User
from Encryptor import Encryptor
import datetime
from UserDaoMapper import UserDaoMapper

class UserDao:
    def __init__(self):
        self.__db_connection = DbConnection()
        self.__user_dao_mapper = UserDaoMapper()
        self.__encryptor = Encryptor()
        self.__db_connection.start_connection()
        self.__db_connection.end_connection()
        
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
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
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
                   user_name = %s,
                   updated_at = %s
                   WHERE id = %s
                   ''')
        values = (
            user.get_name(),
            user.get_paternal_surname(),
            user.get_maternal_surname(),
            user.get_user_type_id(),
            user.get_user_name(),
            datetime.datetime.now(),
            user.get_id()
            )
        
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
        except (Exception, psycopg2.DatabaseError) as error:
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        
        return self.find_by_id(user.get_id())

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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
    
    def search_user(self, search_string:str):
        search_string = "%" + search_string.replace(" ", "") + "%"
        user_list = []
        command = ('''
                   SELECT * FROM tb_user
                   WHERE
                   name LIKE %s OR
                   paternal_surname LIKE %s OR
                   maternal_surname LIKE %s OR
                   user_name LIKE %s OR
                   CONCAT (name, paternal_surname, maternal_surname) LIKE %s
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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        
        return user_list
    
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
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            user = User()

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
        
        return user