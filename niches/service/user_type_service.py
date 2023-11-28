"""
User Type Service Module for Enduring Chambers
"""
from niches.model.dto.user_type_dto import UserTypeDto
from niches.model.dao.user_type_dao import UserTypeDao
from niches.model.mapper.user_type_mapper import UserTypeMapper
from niches.util.logging_configuration import get_loging
logging = get_loging()

class UserTypeService:
    """
    Class with the functionality of UserTypeService
    """
    def __init__(self):
        self.__user_type_dao = UserTypeDao()
        self.__user_type_mapper = UserTypeMapper()

    def find_by_id(self, id:int):
        """
        Find user_type by its id
        Args:
            id : int
                Data transfer object of the user to be saved
        Returns:
            user_type_dto : UserTypeDto
                Founded UserTypeDto.
        """
        user_type_dto = UserTypeDto()
        user_type_dto = self.__user_type_mapper.user_type_to_user_type_dto(
            self.__user_type_dao.find_by_id(id))
        return user_type_dto

    def find_all(self):
        """
        Find all user types
        Args:
            id : int
                Data transfer object of the user to be saved
        Returns:
            list_user_type_dto : list<UserTypeDto>
                All the UserTypeDto
        """
        list_user_type_dto = []
        list_user_type = self.__user_type_dao.find_all()
        for user_type in list_user_type:
            list_user_type_dto.append(self.__user_type_mapper.user_type_to_user_type_dto(user_type))
        return list_user_type_dto
