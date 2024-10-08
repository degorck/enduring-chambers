"""
Holder Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.holder_dto import HolderDto
from niches.model.dao.holder_dao import HolderDao
from niches.model.mapper.holder_mapper import holder_dto_to_holder, holder_to_holder_dto
from niches.controller.error_controller import ErrorController
from niches.constant.constants import STARTS_LOGGING_CONSTANT, ENDS_LOGGING_CONSTANT

class HolderService:
    """
    Class with the functionality of HolderService
    """
    def __init__(self):
        logging.debug(STARTS_LOGGING_CONSTANT)
        self.__error_controller = ErrorController()
        self.__holder_dao = HolderDao()
        logging.debug(ENDS_LOGGING_CONSTANT)

    def create_holder(self, holder_dto:HolderDto):
        """
        Saves the holder on database.

        Arguments:
            holder_dto: HolderDto
                Data transfer object of the holder to be saved
        Returns:
            holder_dto: HolderDto
                Holder created
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        try:
            output = holder_to_holder_dto(
                self.__holder_dao.create_holder(
                    holder_dto_to_holder(holder_dto)))

            logging.debug("Holder created")
            logging.debug(ENDS_LOGGING_CONSTANT)
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
            return None

    def search_holders(self, search_string:str):
        """
        Search holders on database.
        Args:
            search_string: str
                String to search holders
        Returns:
            list_holder_dto : list<HolderDto> 
                Holder list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_holder_dto = []
        list_holder = []
        list_holder = self.__holder_dao.search_holders(search_string)
        for holder in list_holder:
            holder_dto = HolderDto()
            holder_dto = holder_to_holder_dto(holder)
            list_holder_dto.append(holder_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_holder_dto

    def search_active_holders(self, search_string:str):
        """
        Search active holders on database.
        Args:
            search_string: str
                String to search holders
        Returns:
            list_holder_dto : list<HolderDto> 
                Holder list found
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        list_holder_dto = []
        list_holder = []
        list_holder = self.__holder_dao.search_active_holders(search_string)
        for holder in list_holder:
            holder_dto = HolderDto()
            holder_dto = holder_to_holder_dto(holder)
            list_holder_dto.append(holder_dto)
        logging.debug(ENDS_LOGGING_CONSTANT)
        return list_holder_dto

    def find_by_id(self, holder_id:int):
        """
        Search active holder by its id
        Args:
            holder_id: int
                id of the holder to find
        Returns:
            holder_dto : HolderDto 
                HolderDto founded
        """
        logging.debug(STARTS_LOGGING_CONSTANT)
        holder_dto = HolderDto()
        holder_dto = holder_to_holder_dto(
            self.__holder_dao.find_by_id(holder_id))
        logging.debug(ENDS_LOGGING_CONSTANT)
        return holder_dto

    def modify_holder(self, holder_dto:HolderDto):
        """
        Modify holder
        Arguments:
            holder_dto: HolderDto
                HolderDto to be modified
        """
        self.__holder_dao.modify_holder(holder_dto_to_holder(holder_dto))

    def deactivate_holder(self, holder_id:int):
        """
        Deactivate holder by its id
        Arguments:
            holder_id : int
                holder_id of the holder to be modified
        """
        self.__holder_dao.deactivate_holder(holder_id)

    def reactivate_holder(self, holder_id:int):
        """
        Activate holder by its id
        Arguments:
            holder_id : int
                holder_id of the holder to be modified
        """
        self.__holder_dao.reactivate_holder(holder_id)
