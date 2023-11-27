"""
User Service Module for Enduring Chambers
"""
from niches.model.dto.UserDto import UserDto
from niches.model.dao.UserDao import UserDao
from niches.model.mapper.UserMapper import UserMapper
from niches.controller.error_controller import ErrorController
from niches.util.LoggingConfiguration import get_loging
logging = get_loging()

class UserService:
    """
    Class with the functionality of UserService
    """
    def __init__(self):
        self.__error_controller = ErrorController()
        self.__user_dao = UserDao()
        self.__user_mapper = UserMapper()

    def create_user(self, user_dto:UserDto):
        """
        Saves the user on database.
        Args:
            user_dto: UserDto
                Data transfer object of the user to be saved
        Returns:
            __user_type_key : str
                User type key of the logged user.
        """
        try:
            self.__user_dao.create_user(self.__user_mapper.user_dto_to_user(user_dto))
        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()

        logging.debug("User created")

    def search_users(self, search_string:str):
        """
        Search users on database.
        Args:
            search_string: str
                String to search users
        Returns:
            list_user_dto : list<UserDto> 
                User type key of the logged user.
        """
        list_user_dto = []
        list_user = []
        list_user = self.__user_dao.search_users(search_string)
        for user in list_user:
            user_dto = UserDto()
            user_dto = self.__user_mapper.user_to_user_dto(user)
            list_user_dto.append(user_dto)
        return list_user_dto

    def find_user_by_user_name(self, user_name:str):
        """
        Find user by its user_name
        Args:
            user_name: str
                User name of the user to find
        Returns:
            user_dto : UserDto 
                Finded UserDto.
        """
        return self.__user_mapper.user_to_user_dto(
            self.__user_dao.find_user_by_user_name(user_name))

    def modify_user(self, user_dto:UserDto):
        """
        Modify user
        Args:
            user_dto: UserDto
                UserDto to be modified
        """
        self.__user_dao.modify_user(self.__user_mapper.user_dto_to_user(user_dto))

    def deactivate_user(self, id:int):
        """
        Deactivate user by its id
        Args:
            id : int
                id of the user to be modified
        """
        self.__user_dao.deactivate_user(id)

    def reactivate_user(self, id:int):
        """
        Activate user by its id
        Args:
            id : int
                id of the user to be modified
        """
        self.__user_dao.reactivate_user(id)
