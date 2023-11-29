"""
HolderDao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import datetime
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.mapper.holder_dao_mapper import HolderDaoMapper
from niches.model.entity.holder import Holder

class HolderDao:
    """
    Class with the functionality of Holder Dao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__holder_dao_mapper = HolderDaoMapper()

    def create_holder(self, holder:Holder):
        """
        Saves the holder on database

        Arguments:
            holder: Holder
                Holder entity to be created
        Returns:
            holder : Holder
                Created Holder entity 
        """
        command = '''
                INSERT INTO tb_holder(
                    name,
                    paternal_surname,
                    maternal_surname,
                    phone,
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
                    %s)
                '''
        values = (
            holder.get_name(),
            holder.get_paternal_surname(),
            holder.get_maternal_surname(),
            holder.get_phone(),
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
            logging.debug("Se creó el titular")
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_by_id(self, holder_id:int):
        """
        Find holder by its holder_id
        
        Arguments:
            holder_id: int
                holder_id of the user to find
        Returns:
            holder: Holder
                Holder found
        """
        command = '''
                SELECT * 
                FROM tb_holder
                WHERE
                id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % holder_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            user = self.__holder_dao_mapper.real_dict_row_to_holder(row)
            logging.debug("Se buscó el titular por su id")
            return user
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_holders(self, search_string:str):
        """
        Search all holders by search_string
        
        Arguments:
            search_string: str
                String to match with the users search
        Returns:
            holder_list = list<Holder>
        """
        search_string = "%" + search_string + "%"
        holder_list = []
        command = '''
                SELECT * FROM tb_holder
                WHERE
                name LIKE %s OR
                paternal_surname LIKE %s OR
                maternal_surname LIKE %s OR
                phone LIKE %s OR
                CONCAT (name , ' ', paternal_surname, ' ', maternal_surname) LIKE %s
                '''
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
                holder = self.__holder_dao_mapper.real_dict_row_to_holder(row)
                holder_list.append(holder)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los titulares")
            return holder_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_active_holders(self, search_string:str):
        """
        Search all active holders by search_string
        
        Arguments:
            search_string: str
                String to match with the users search
        Returns:
            holder_list = list<Holder>
        """
        search_string = "%" + search_string + "%"
        holder_list = []
        command = '''
                SELECT * FROM tb_holder
                WHERE
                (name LIKE %s OR
                paternal_surname LIKE %s OR
                maternal_surname LIKE %s OR
                phone LIKE %s OR
                CONCAT (name , ' ', paternal_surname, ' ', maternal_surname) LIKE %s)
                AND
                (is_active = True)
                '''

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
                holder = self.__holder_dao_mapper.real_dict_row_to_holder(row)
                holder_list.append(holder)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron los usuarios activos")
            return holder_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_holder(self, holder:Holder):
        """
        Modifies the holder on database
        
        Arguments:
            holder : Holder
                Holder entity to be modified
        """
        command = '''
                UPDATE tb_holder
                SET
                name = %s,
                paternal_surname = %s,
                maternal_surname = %s,
                phone = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            holder.get_name(),
            holder.get_paternal_surname(),
            holder.get_maternal_surname(),
            holder.get_phone(),
            datetime.datetime.now(),
            holder.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el titular")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()