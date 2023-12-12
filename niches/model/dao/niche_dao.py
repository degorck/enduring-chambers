"""
NicheDao Module. Includes all the functions to load and read data
from database. 
"""
import datetime
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.niche import Niche
from niches.model.mapper.dao.niche_dao_mapper import real_dict_row_to_niche

class NicheDao:
    """
    Class with the functionality of NicheDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def create_niche(self, niche:Niche):
        """
        Saves the niche on database

        Arguments:
            niche: Niche
                Niche entity to be created
        Returns:
            niche : Niche
                Created niche entity 
        """
        if niche.get_holder() is None:
            niche_id = None
        else:
            niche_id = niche.get_holder().get_id()

        command = '''
                INSERT INTO tb_niche(
                    row_id,
                    number,
                    is_busy,
                    is_paid_off,
                    holder_id,
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
                    %s)
                '''
        values = (
            niche.get_row().get_id(),
            niche.get_number(),
            niche.is_busy(),
            niche.is_paid_off(),
            niche_id,
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
            logging.debug("Se creó el nicho")
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_by_id(self, niche_id:int):
        """
        Find niche by its niche_id
        
        Arguments:
            niche_id: int
                niche_id of the niche to find
        Returns:
            niche: Niche
                Niche found
        """
        command = '''
                SELECT tb_niche.id,
                tb_niche.number,
                tb_niche.is_busy,
                tb_niche.is_paid_off,
                tb_niche.is_active,
                tb_niche.created_at,
                tb_niche.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname,
                tb_holder.maternal_surname,
                tb_holder.phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_niche
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE tb_niche.id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % niche_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            niche = real_dict_row_to_niche(row)
            logging.debug("Se buscó el nicho por su id")
            return niche
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_niches(self, search_string:str):
        """
        Search all niches by search_string
        
        Arguments:
            search_string: str
                String to match with the niches search

        Returns:
            niche_list = list<Niche>
        """
        search_string = "%" + search_string + "%"
        niche_list = []
        command = '''
                SELECT tb_niche.id,
                tb_niche.number,
                tb_niche.is_busy,
                tb_niche.is_paid_off,
                tb_niche.is_active,
                tb_niche.created_at,
                tb_niche.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname,
                tb_holder.maternal_surname,
                tb_holder.phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_niche
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE
                (tb_module.name LIKE %s OR
                tb_row.name LIKE %s)
                OR (CONCAT (tb_module.name, tb_row.name, CAST(tb_niche.number AS VARCHAR(3))) LIKE %s)
                ORDER BY tb_module.name, tb_row.name, tb_niche.number, tb_niche.id
                '''
        values = (
            search_string,
            search_string,
            search_string)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                niche = real_dict_row_to_niche(row)
                niche_list.append(niche)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los nichos")
            return niche_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_niches_by_module_id_and_row_id(self, search_string:str, module_id:int, row_id:int):
        """
        Search all niches by search_string
        
        Arguments:
            search_string: str
                String to match with the niches search
            module_id: int
                module to filter list
            row_id: int
                row to filter list

        Returns:
            niche_list = list<Niche>
        """
        search_string = "%" + search_string + "%"
        niche_list = []
        command = '''
                SELECT tb_niche.id,
                tb_niche.number,
                tb_niche.is_busy,
                tb_niche.is_paid_off,
                tb_niche.is_active,
                tb_niche.created_at,
                tb_niche.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname,
                tb_holder.maternal_surname,
                tb_holder.phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_niche
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE
                (tb_module.name LIKE %s OR
                tb_row.name LIKE %s OR
                CAST (tb_niche.number AS VARCHAR(3)) LIKE %s OR
                CONCAT (tb_module.name, tb_row.name, CAST(tb_niche.number AS VARCHAR(3))) LIKE %s)
                AND (tb_row.module_id = %s)
                AND (tb_niche.row_id = %s)
                ORDER BY tb_module.name, tb_row.name, tb_niche.number, tb_niche.id
                '''
        values = (
            search_string,
            search_string,
            search_string,
            search_string,
            module_id,
            row_id)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                niche = real_dict_row_to_niche(row)
                niche_list.append(niche)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los nichos")
            return niche_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_niches_by_module_id(self, search_string:str, module_id:int):
        """
        Search all niches by search_string
        
        Arguments:
            search_string: str
                String to match with the niches search
            module_id: int
                module to filter list

        Returns:
            niche_list = list<Niche>
        """
        search_string = "%" + search_string + "%"
        niche_list = []
        command = '''
                SELECT tb_niche.id,
                tb_niche.number,
                tb_niche.is_busy,
                tb_niche.is_paid_off,
                tb_niche.is_active,
                tb_niche.created_at,
                tb_niche.updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname,
                tb_holder.maternal_surname,
                tb_holder.phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_niche
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE
                (tb_module.name LIKE %s OR
                tb_row.name LIKE %s OR
                CAST (tb_niche.number AS VARCHAR(3)) LIKE %s OR
                CONCAT (tb_module.name, tb_row.name, CAST(tb_niche.number AS VARCHAR(3))) LIKE %s)
                AND (tb_row.module_id = %s)
                ORDER BY tb_module.name, tb_row.name, tb_niche.number, tb_niche.id
                '''
        values = (
            search_string,
            search_string,
            search_string,
            search_string,
            module_id)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                niche = real_dict_row_to_niche(row)
                niche_list.append(niche)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los nichos")
            return niche_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_niche(self, niche:Niche):
        """
        Modifies the niche on database
        
        Arguments:
            niche: Niche
                Niche entity to be modified
        """
        if niche.get_holder() is None:
            holder_id = None
        else:
            holder_id = niche.get_holder().get_id()
        command = '''
                UPDATE tb_niche
                SET
                row_id = %s,
                is_busy = %s,
                is_paid_off = %s,
                holder_id = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            niche.get_row().get_id(),
            niche.is_busy(),
            niche.is_paid_off(),
            holder_id,
            datetime.datetime.now(),
            niche.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el nicho")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def deactivate_niche(self, niche_id:int):
        """
        Deactivates the niche on database
        
        Arguments:
            niche_id: int
                niche_id of the user to deactivate
        """
        command = '''
                UPDATE tb_niche
                SET
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            False,
            datetime.datetime.now(),
            niche_id
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se desactivó el nicho")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def reactivate_niche(self, niche_id:int):
        """
        Reactivates the niche on database
        
        Arguments:
            niche_id: int
                niche_id of the user to reactivate
        """
        command = '''
                UPDATE tb_niche
                SET
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            True,
            datetime.datetime.now(),
            niche_id
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se reactivó el nicho")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
