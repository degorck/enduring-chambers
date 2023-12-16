"""
RowService Module for Enduring Chambers
"""
import logging
from niches.model.dto.row_dto import RowDto
from niches.model.dao.row_dao import RowDao
from niches.model.mapper.row_mapper import row_to_row_dto

class RowService:
    """
    Class with the functionality of RowService
    """
    def __init__(self):
        self.__row_dao = RowDao()

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
