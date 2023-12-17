"""
User Type Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.user_type_dto import UserTypeDto
from niches.model.dao.user_type_dao import UserTypeDao
from niches.model.mapper.user_type_mapper import user_type_to_user_type_dto

class UserTypeService:
    """
    Class with the functionality of UserTypeService
    """
    def __init__(self):
        self.__user_type_dao = UserTypeDao()

    def find_by_id(self, id_user_type:int):
        """
        Find user_type by its id
        Arguments:
            id_user_type : int
                Data transfer object of the user to be saved
        Returns:
            user_type_dto : UserTypeDto
                Founded UserTypeDto.
        """
        user_type_dto = UserTypeDto()
        user_type_dto = user_type_to_user_type_dto(
            self.__user_type_dao.find_by_id(id_user_type))
        return user_type_dto

    def find_all(self):
        """
        Find all user types
        Arguments:
            id : int
                Data transfer object of the user to be saved
        Returns:
            list_user_type_dto : list<UserTypeDto>
                All the UserTypeDto
        """
        list_user_type_dto = []
        list_user_type = self.__user_type_dao.find_all()
        for user_type in list_user_type:
            list_user_type_dto.append(user_type_to_user_type_dto(user_type))
        return list_user_type_dto
