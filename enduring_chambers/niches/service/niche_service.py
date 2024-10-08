"""
Niche Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.niche_dto import NicheDto
from niches.model.dao.niche_dao import NicheDao
from niches.model.mapper.niche_mapper import niche_dto_to_niche, niche_to_niche_dto
from niches.controller.error_controller import ErrorController
from niches.constant.constants import STARTS_LOGGING_CONSTANT, ENDS_LOGGING_CONSTANT

class NicheService:
    """
    Class with the functionality of NicheService
    """
    def __init__(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.__error_controller = ErrorController()
        self.__niche_dao = NicheDao()
        logging.debug(ENDS_LOGGING_CONSTANT)

    def create_niche(self, niche_dto:NicheDto):
        """
        Saves the niche on database.

        Arguments:
            niche_dto: NicheDto
                Data transfer object of the niche to be saved
        Returns:
            niche_dto: NicheDto
                Niche created
        """
        try:
            output = niche_to_niche_dto(
                self.__niche_dao.create_niche(niche_dto_to_niche(niche_dto)))

            logging.debug("Niche created")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
            return None

    def search_niches(self, search_string:str):
        """
        Search niches on database.

        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
            row_id: int
                row_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_niches(search_string)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto

    def search_niches_by_module_id_and_row_id(self, search_string:str, module_id:int, row_id:int):
        """
        Search niches on database.
        
        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
            row_id: int
                row_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_niches_by_module_id_and_row_id(search_string,
                                                                            module_id, row_id)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto


    def search_niches_by_module_id(self, search_string:str, module_id:int):
        """
        Search niches on database.

        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_niches_by_module_id(search_string,
                                                                 module_id)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto

    def find_by_id(self, id_niche:int):
        """
        Find niche by its id

        Arguments:
            id_niche : int
                id of the Niche
        Returns:
            niche_dto : NicheDto
                Founded NicheDto.
        """
        niche_dto = NicheDto()
        niche_dto = niche_to_niche_dto(
            self.__niche_dao.find_by_id(id_niche))
        logging.debug("Se encontró el nicho por su id")
        return niche_dto

    def modify_niche(self, niche_dto:NicheDto):
        """
        Modify niche

        Arguments:
            niche_dto: NicheDto
                NicheDto to be modified
        """
        self.__niche_dao.modify_niche(niche_dto_to_niche(niche_dto))

    def reactivate_niche(self, niche_id:int):
        """
        Reactivate niche by its id

        Arguments:
            niche_id : int
                niche_id of the niche to be modified
        """
        self.__niche_dao.reactivate_niche(niche_id)

    def deactivate_niche(self, niche_id:int):
        """
        Reactivate niche by its id

        Arguments:
            niche_id : int
                niche_id of the niche to be modified
        """
        self.__niche_dao.deactivate_niche(niche_id)

    def search_not_busy_niches_by_module_id_and_row_id(self, search_string:str,
                                                       module_id:int, row_id:int):
        """
        Search not busy niches on database.
        
        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
            row_id: int
                row_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_not_busy_niches_by_module_id_and_row_id(search_string,
                                                                                     module_id,
                                                                                     row_id)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto

    def occupy_niche(self, niche_id:int):
        """
        Marks niche as occupied by its id

        Arguments:
            niche_id : int
                niche_id of the niche to be modified
        """
        self.__niche_dao.occupy_niche(niche_id)

    def pay_niche(self, niche_id:int):
        """
        Marks niche as paid off by its id

        Arguments:
            niche_id : int
                niche_id of the niche to be modified
        """
        self.__niche_dao.pay_niche(niche_id)

    def search_active_niches_by_module_id_and_row_id(self, search_string:str,
                                                       module_id:int, row_id:int):
        """
        Search active niches on database.
        
        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
            row_id: int
                row_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_active_niches_by_module_id_and_row_id(search_string,
                                                                                     module_id,
                                                                                     row_id)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto

    def search_active_niches_by_module_id_and_row_id_no_limit(self, search_string:str,
                                                       module_id:int, row_id:int):
        """
        Search active niches on database.
        
        Arguments:
            search_string: str
                String to search niches
            module_id: int
                module_id to filter the list
            row_id: int
                row_id to filter the list
        Returns:
            list_niche_dto : list<NicheDto> 
                Niche list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_niche_dto = []
        list_niche = []
        list_niche = self.__niche_dao.search_active_niches_by_module_id_and_row_id_no_limit(
            search_string,
            module_id,
            row_id)
        for niche in list_niche:
            niche_dto = NicheDto()
            niche_dto = niche_to_niche_dto(niche)
            list_niche_dto.append(niche_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_niche_dto

    def get_last_record_by_module_id_and_row_id(self, module_id:int, row_id:int):
        """
        Get last record by module_id and row_id

        Arguments:
            module_id : int
                module_id of the niche
            row_id : int
                row_id of the niche
        Returns:
            niche_dto : NicheDto
                niche_dto of the niche
        """
        niche = self.__niche_dao.get_last_record_by_module_id_and_row_id(module_id, row_id)
        niche_dto = niche_to_niche_dto(niche)
        return niche_dto
