"""
Deceased Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.deceased_dto import DeceasedDto
from niches.model.dao.deceased_dao import DeceasedDao
from niches.model.mapper.deceased_mapper import deceased_dto_to_deceased, deceased_to_deceased_dto
from niches.controller.error_controller import ErrorController

class DeceasedService:
    """
    Class with the functionality of DeceasedService
    """
    def __init__(self):
        self.__error_controller = ErrorController()
        self.__deceased_dao = DeceasedDao()

    def create_deceased(self, deceased_dto:DeceasedDto):
        """
        Saves the deceased on database.

        Arguments:
            deceased_dto: DeceasedDto
                Data transfer object of the deceased to be saved
        Returns:
            deceased_dto: DeceasedDto
                Deceased created
        """
        try:
            output = deceased_to_deceased_dto(
                self.__deceased_dao.create_deceased(
                    deceased_dto_to_deceased(deceased_dto)))

            logging.debug("Deceased created")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
            return None

    def find_by_id(self, deceased_id:int):
        """
        Search active deceased by its id
        Args:
            deceased_id: int
                id of the deceased to find
        Returns:
            deceased_dto : DeceasedDto 
                DeceasedDto founded
        """
        deceased_dto = DeceasedDto()
        deceased_dto = deceased_to_deceased_dto(
            self.__deceased_dao.find_by_id(deceased_id))
        return deceased_dto
