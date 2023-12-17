"""
DeceasedDao Module. Includes all the functions to load and read data
from database. 
"""
import datetime
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.deceased import Deceased
from niches.model.mapper.dao.deceased_dao_mapper import real_dict_row_to_deceased

class DeceasedDao:
    """
    Class with the functionality of DeceasedDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def create_deceased(self, deceased:Deceased):
        """
        Saves the deceased on database

        Arguments:
            deceased: Deceased
                Deceased entity to be created
        Returns:
            deceased : Deceased
                Created deceased entity 
        """
        command = '''
                INSERT INTO tb_deceased(
                    name,
                    paternal_surname,
                    maternal_surname,
                    birth_date,
                    death_date,
                    remain_type_id,
                    niche_id,
                    book,
                    sheet,
                    image_route,
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
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)
                '''
        values = (
            deceased.get_name(),
            deceased.get_paternal_surname(),
            deceased.get_maternal_surname(),
            deceased.get_birth_date(),
            deceased.get_death_date(),
            deceased.get_remain_type().get_id(),
            deceased.get_niche().get_id(),
            deceased.get_book(),
            deceased.get_sheet(),
            deceased.get_image_route(),
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
            logging.debug("Se creó el difunto")
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_deceased(self, deceased:Deceased):
        """
        Modify the deceased on database

        Arguments:
            deceased: Deceased
                Deceased entity to be created
        Returns:
            deceased : Deceased
                Created deceased entity 
        """
        command = '''
                UPDATE tb_deceased
                SET
                name = %s,
                paternal_surname = %s,
                maternal_surname = %s,
                birth_date = %s,
                death_date = %s,
                remain_type_id = %s,
                niche_id = %s,
                book = %s,
                sheet = %s,
                image_route = %s,
                is_active = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            deceased.get_name(),
            deceased.get_paternal_surname(),
            deceased.get_maternal_surname(),
            deceased.get_birth_date(),
            deceased.get_death_date(),
            deceased.get_remain_type().get_id(),
            deceased.get_niche().get_id(),
            deceased.get_book(),
            deceased.get_sheet(),
            deceased.get_image_route(),
            True,
            datetime.datetime.now(),
            deceased.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el difunto")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_by_id(self, deceased_id:int):
        """
        Find deceased by its deceased_id
        
        Arguments:
            deceased_id: int
                deceased_id of the deceased to find
        Returns:
            deceased: Deceased
                Deceased found
        """
        command = '''
                SELECT tb_deceased.id,
                tb_deceased.name,
                tb_deceased.paternal_surname,
                tb_deceased.maternal_surname,
                tb_deceased.birth_date,
                tb_deceased.death_date,
                tb_deceased.book,
                tb_deceased.sheet,
                tb_deceased.image_route,
                tb_deceased.is_active,
                tb_deceased.created_at,
                tb_deceased.updated_at,
                tb_remain_type.id as remain_type_id,
                tb_remain_type.name as remain_type_name,
                tb_remain_type.key as remain_type_key,
                tb_remain_type.created_at as remain_type_created_at,
                tb_remain_type.updated_at as remain_type_updated_at,
                tb_niche.id as niche_id,
                tb_niche.number as niche_number,
                tb_niche.is_busy as niche_is_busy,
                tb_niche.is_paid_off as niche_is_paid_off,
                tb_niche.is_active as niche_is_active,
                tb_niche.created_at as niche_created_at,
                tb_niche.updated_at as niche_updated_at,
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
                tb_holder.paternal_surname as holder_paternal_surname,
                tb_holder.maternal_surname as holder_maternal_surname,
                tb_holder.phone as holder_phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_deceased
                INNER JOIN tb_remain_type ON tb_deceased.remain_type_id = tb_remain_type.id
                INNER JOIN tb_niche ON tb_deceased.niche_id = tb_niche.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE tb_deceased.id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % deceased_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            deceased:Deceased = real_dict_row_to_deceased(row)
            logging.debug("Se buscó el difunto por su id")
            return deceased
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_all_deceased(self, search_string:str):
        """
        Search all deceased by search_string
        
        Arguments:
            search_string: str
                String to match with the deceased search
        Returns:
            deceased_list = list<Deceased>
        """
        search_string = "%" + search_string + "%"
        deceased_list = []
        command = '''
                SELECT tb_deceased.id,
                tb_deceased.name,
                tb_deceased.paternal_surname,
                tb_deceased.maternal_surname,
                tb_deceased.birth_date,
                tb_deceased.death_date,
                tb_deceased.book,
                tb_deceased.sheet,
                tb_deceased.image_route,
                tb_deceased.is_active,
                tb_deceased.created_at,
                tb_deceased.updated_at,
                tb_remain_type.id as remain_type_id,
                tb_remain_type.name as remain_type_name,
                tb_remain_type.key as remain_type_key,
                tb_remain_type.created_at as remain_type_created_at,
                tb_remain_type.updated_at as remain_type_updated_at,
                tb_niche.id as niche_id,
                tb_niche.number as niche_number,
                tb_niche.is_busy as niche_is_busy,
                tb_niche.is_paid_off as niche_is_paid_off,
                tb_niche.is_active as niche_is_active,
                tb_niche.created_at as niche_created_at,
                tb_niche.updated_at as niche_updated_at,
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
                tb_holder.paternal_surname as holder_paternal_surname,
                tb_holder.maternal_surname as holder_maternal_surname,
                tb_holder.phone as holder_phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_deceased
                INNER JOIN tb_remain_type ON tb_deceased.remain_type_id = tb_remain_type.id
                INNER JOIN tb_niche ON tb_deceased.niche_id = tb_niche.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE
                tb_deceased.name LIKE %s OR
                tb_deceased.paternal_surname LIKE %s OR
                tb_deceased.maternal_surname LIKE %s OR
                CONCAT (tb_deceased.name , ' ', tb_deceased.paternal_surname, ' ', tb_deceased.maternal_surname) LIKE %s
                ORDER BY id
                '''
        values = (
            search_string,
            search_string,
            search_string,
            search_string)
        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                deceased = real_dict_row_to_deceased(row)
                deceased_list.append(deceased)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los difuntos")
            return deceased_list
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
