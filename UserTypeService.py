from UserTypeDao import UserTypeDao
from UserTypeDto import UserTypeDto
from UserTypeMapper import UserTypeMapper
class UserTypeService:
    def __init__(self):
        pass

    def get_all(self):
        user_type_list = []
        user_type_dto_list = []
        user_type_list = user_type_dao.find_all()
        for user_type in user_type_list:
            user_type_dto = UserTypeDto()
            user_type_dto = user_type_mapper.user_type_to_user_type_dto(user_type)
            user_type_dto_list.append(user_type_dto)
        return user_type_dto_list

        
if __name__ == "__main__": 
    user_type_dao = UserTypeDao()
    user_type_mapper = UserTypeMapper()
    user_type_service = UserTypeService()
    user_type_dto = UserTypeDto()
    for user_type_dto in user_type_service.get_all():
        print(user_type_dto.get_id())
        print(user_type_dto.get_name())

