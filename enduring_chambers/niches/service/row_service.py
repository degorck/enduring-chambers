"""
RowService Module for Enduring Chambers
"""
import logging
from niches.model.dto.row_dto import RowDto
from niches.model.dao.row_dao import RowDao
from niches.model.mapper.row_mapper import row_to_row_dto, row_dto_to_row
from niches.controller.error_controller import ErrorController

class RowService:
    """
    Class with the functionality of RowService
    """
    def __init__(self):
        self.__row_dao = RowDao()
        self.__error_controller = ErrorController()

    def find_by_id(self, id_row:int):
        """
        Find row by its id
        Arguments:
            id_row : int
                id of the Row
        Returns:
            row_dto : RowDto
                Founded RowDto.
        """
        row_dto = RowDto()
        row_dto = row_to_row_dto(
            self.__row_dao.find_by_id(id_row))
        logging.debug("Se encontró la fila por su id")
        return row_dto

    def find_all(self):
        """
        Find all rows

        Returns:
            list_row_dto : list<RowDto>
                All the RowDto
        """
        list_row_dto = []
        list_row = self.__row_dao.find_all()
        for row in list_row:
            list_row_dto.append(row_to_row_dto(row))
        logging.debug("Se obtuvieron todas las filas")
        return list_row_dto

    def find_all_by_module_id(self, module_id:int):
        """
        Find all rows

        Argunments:
            module_id: int
                Module to filter list_row_dto

        Returns:
            list_row_dto : list<RowDto>
                All the RowDto
        """
        list_row_dto = []
        list_row = self.__row_dao.find_all_by_module_id(module_id)
        for row in list_row:
            list_row_dto.append(row_to_row_dto(row))
        logging.debug("Se obtuvieron todas las filas de módulo")
        return list_row_dto

    def modify_row(self, row_dto:RowDto):
        """
        Modify row

        Arguments:
            row_dto: RowDto
                RowDto to be modified
        """
        self.__row_dao.modify_row(row_dto_to_row(row_dto))

    def create_row(self, row_dto:RowDto):
        """
        Saves the row on database.

        Arguments:
            row_dto: RowDto
                Data transfer object of the row to be saved
        Returns:
            row_dto: RowDto
                Row created
        """
        try:
            output = row_to_row_dto(
                self.__row_dao.create_row(
                    row_dto_to_row(row_dto)))

            logging.debug("Row created")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()
            return None
