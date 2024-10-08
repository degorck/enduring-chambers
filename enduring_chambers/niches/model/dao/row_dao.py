"""
RowDao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import datetime
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.row import Row
from niches.model.mapper.dao.row_dao_mapper import real_dict_row_to_row

class RowDao:
    """
    Class with the functionality of RowDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def find_by_id(self, row_id:int):
        """
        Find the row by its id

        Arguments:
            row_id: int
                row_id of the row to find
        Returns:
            row : Row
                 Row entity found 
        """
        command = '''
                SELECT tb_row.id,
                tb_row.name,
                tb_row.created_at,
                tb_row.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at
                FROM tb_row
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE tb_row.id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % row_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            row_entity = Row()
            row_entity =  real_dict_row_to_row(row)
            logging.debug("Se encontró una fila por su id")
            return row_entity
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all(self):
        """
        Find the all the rows

        Returns:
            row_list : list<row>
                All the row list
        """
        command = '''
                SELECT tb_row.id,
                tb_row.name,
                tb_row.created_at,
                tb_row.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at
                FROM tb_row
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                ORDER BY id
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_row = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                row_entity = Row()
                row_entity =  real_dict_row_to_row(row)
                list_row.append(row_entity)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todas las filas")
            return list_row

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all_by_module_id(self, module_id:int):
        """
        Find the all the rows by module_id
        
        Arguments:
            module_id: int
                Module to filter rows

        Returns:
            row_list : list<Row>
                All the row list
        """
        command = '''
                SELECT tb_row.id,
                tb_row.name,
                tb_row.created_at,
                tb_row.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at
                FROM tb_row
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE module_id = %s
                ORDER BY id
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command  % module_id)
            list_row = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                row_entity = Row()
                row_entity =  real_dict_row_to_row(row)
                list_row.append(row_entity)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos las filas")
            return list_row

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def create_row(self, row_entity:Row):
        """
        Create new row on database

        Arguments:
            row: Row
                row to save
        Returns:
            row: Row
                Row created
        """
        command = '''
                INSERT INTO tb_row(
                name,
                module_id,
                created_at,
                updated_at) 
                VALUES(
                    %s,
                    %s,
                    %s,
                    %s)
            '''
        values = (row_entity.get_name(),
                  row_entity.get_module().get_id(),
                  datetime.datetime.now(),
                  datetime.datetime.now())

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.get_cursor().execute('SELECT LASTVAL()')
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            logging.debug("Se creó la fila")
            return self.find_by_id(int(row["lastval"]))

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_row(self, row_entity:Row):
        """
        Modifies the row on database
        
        Arguments:
            row: Row
                Row entity to be modified
        """
        command = '''
                UPDATE tb_row
                SET
                name = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            row_entity.get_name(),
            datetime.datetime.now(),
            row_entity.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó la fila")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
