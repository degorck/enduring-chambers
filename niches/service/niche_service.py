"""
Niche Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.niche_dto import NicheDto
from niches.model.dao.niche_dao import NicheDao
from niches.model.mapper.niche_mapper import NicheMapper
from niches.controller.error_controller import ErrorController

class NicheService:
    """
    Class with the functionality of NicheService
    """
    def __init__(self):
        self.__error_controller = ErrorController()
        self.__niche_dao = NicheDao()
        self.__niche_mapper = NicheMapper()

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
            output = self.__niche_mapper.niche_to_niche_dto(
                self.__niche_dao.create_niche(self.__niche_mapper.niche_dto_to_niche(niche_dto)))

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
