"""
ModuleDao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import datetime
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.module import Module
from niches.model.mapper.dao.module_dao_mapper import real_dict_row_to_module

class ModuleDao:
    """
    Class with the functionality of UserTypeDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def find_by_id(self, module_id:int):
        """
        Find the module by its id

        Arguments:
            module_id: int
                module_id of the module to find
        Returns:
            module : Module
                 Module entity found 
        """
        command = '''
                SELECT * 
                FROM tb_module
                WHERE
                id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % module_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            module = Module()
            module =  real_dict_row_to_module(row)
            logging.debug("Se encontró un usuario por su id")
            return module
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all_active(self):
        """
        Find the all the modules

        Returns:
            module_list : list<Module>
                All the module list
        """
        command = '''
                SELECT * 
                FROM tb_module
                WHERE tb_module.is_active = True
                ORDER BY id                
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_module = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                module = Module()
                module =  real_dict_row_to_module(row)
                list_module.append(module)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los modulos activos")
            return list_module

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_by_name(self, module_name:str):
        """
        Find the module by its id

        Arguments:
            module_id: int
                module_id of the module to find
        Returns:
            module : Module
                 Module entity found 
        """
        command = '''
                SELECT * 
                FROM tb_module
                WHERE
                name = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % module_name)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            module = Module()
            module =  real_dict_row_to_module(row)
            logging.debug("Se encontró un módulo por su nombre")
            return module
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_all(self):
        """
        Find the all the modules

        Returns:
            module_list : list<Module>
                All the module list
        """
        command = '''
                SELECT * 
                FROM tb_module
                ORDER BY id                
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_module = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                module = Module()
                module =  real_dict_row_to_module(row)
                list_module.append(module)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los modulos")
            return list_module

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def create_module(self, module:Module):
        """
        Create new module on database

        Arguments:
            module: Module
                module to save
        Returns:
            module: Module
                module created
        """
        command = '''
                INSERT INTO tb_module(
                name,
                is_active,
                created_at,
                updated_at) 
                VALUES(
                    %s,
                    %s,
                    %s,
                    %s)
            '''
        values = (module.get_name(),
                  True,
                  datetime.datetime.now(),
                  datetime.datetime.now())

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.get_cursor().execute('SELECT LASTVAL()')
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            logging.debug("Se creó el pago")
            return self.find_by_id(int(row["lastval"]))

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_module(self, module:Module):
        """
        Modifies the module on database
        
        Arguments:
            module: Module
                Module entity to be modified
        """
        command = '''
                UPDATE tb_module
                SET
                name = %s,
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            module.get_name(),
            module.is_active(),
            datetime.datetime.now(),
            module.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el módulo")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def deactivate_module(self, module_id:int):
        """
        Deactivates the module on database
        
        Arguments:
            module_id: int
                module_id of the module to deactivate
        """
        command = '''
                UPDATE tb_module
                SET
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            False,
            datetime.datetime.now(),
            module_id
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se desactivó el módulo")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def reactivate_module(self, module_id:int):
        """
        Activates the module on database
        
        Arguments:
            module_id: int
                module_id of the module to activate
        """
        command = '''
                UPDATE tb_module
                SET
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            True,
            datetime.datetime.now(),
            module_id
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se reactivó el módulo")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.error(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
