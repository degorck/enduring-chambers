"""
ModuleDao Module. Includes all the functions to load and read data
from database. 
"""
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.module import Module
from niches.model.mapper.dao.module_dao_mapper import ModuleDaoMapper

class ModuleDao:
    """
    Class with the functionality of UserTypeDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()
        self.__module_dao_mapper = ModuleDaoMapper()

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
                id_module = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % module_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            module = Module()
            module =  self.__module_dao_mapper.real_dict_row_to_module(row)
            logging.debug("Se encontró un usuario por su id")
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
                ORDER BY id_module
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command)
            list_module = []
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                module = Module()
                module =  self.__module_dao_mapper.real_dict_row_to_module(row)
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
            module =  self.__module_dao_mapper.real_dict_row_to_module(row)
            logging.debug("Se encontró un usuario por su id")
            return module
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
