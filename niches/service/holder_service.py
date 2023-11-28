"""
Holder Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.holder_dto import HolderDto
from niches.model.dao.holder_dao import HolderDao
from niches.model.mapper.holder_mapper import HolderMapper
from niches.controller.error_controller import ErrorController

class HolderService:
    """
    Class with the functionality of HolderService
    """
    def __init__(self):
        self.__error_controller = ErrorController()
        self.__holder_dao = HolderDao()
        self.__holder_mapper = HolderMapper()

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
        try:
            output = self.__holder_mapper.holder_to_holder_dto(
                self.__holder_dao.create_holder(
                    self.__holder_mapper.holder_dto_to_holder(holder_dto)))

            logging.debug("Holder created")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
            return None
