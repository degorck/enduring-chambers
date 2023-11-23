from UserTypeDao import UserTypeDao
from UserTypeDto import UserTypeDto
from UserTypeMapper import UserTypeMapper

class UserTypeService:
    def __init__(self):
        self.__user_type_dao = UserTypeDao()
        self.__user_type_mapper = UserTypeMapper()

    def get_all(self):
        user_type_list = []
        user_type_dto_list = []
        user_type_list = self.__user_type_dao.find_all()
        for user_type in user_type_list:
            user_type_dto = UserTypeDto()
            user_type_dto = self.__user_type_mapper.user_type_to_user_type_dto(user_type)
            user_type_dto_list.append(user_type_dto)
        return user_type_dto_list


