"""
Remain Type Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.remain_type_dto import RemainTypeDto
from niches.model.dao.remain_type_dao import RemainTypeDao
from niches.model.mapper.remain_type_mapper import remain_type_to_remain_type_dto

class RemainTypeService:
    """
    Class with the functionality of RemainTypeService
    """
    def __init__(self):
        self.__remain_type_dao = RemainTypeDao()

    def find_by_id(self, id_remain_type:int):
        """
        Find remain_type by its id
        
        Arguments:
            id_remain_type : int
                Data transfer object of the remain to be find
        Returns:
            remain_type_dto : RemainTypeDto
                Founded RemainTypeDto.
        """
        remain_type_dto = RemainTypeDto()
        remain_type_dto = remain_type_to_remain_type_dto(
            self.__remain_type_dao.find_by_id(id_remain_type))
        return remain_type_dto

    def find_all(self):
        """
        Find all remain types
        
        Arguments:
            id : int
                Data transfer object of the remain to be saved
        Returns:
            list_remain_type_dto : list<RemainTypeDto>
                All the RemainTypeDto
        """
        list_remain_type_dto = []
        list_remain_type = self.__remain_type_dao.find_all()
        for remain_type in list_remain_type:
            list_remain_type_dto.append(remain_type_to_remain_type_dto(remain_type))
        return list_remain_type_dto
