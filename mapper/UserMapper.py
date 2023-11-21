import repackage
repackage.up()
from model.entity.User import User
from model.dto.UserDto import UserDto
class UserMapper:
    def __init__(self):
        pass

    def user_to_user_dto(self, user:User):
        user_dto = UserDto()
        user_dto.set_id(user.get_id())
        user_dto.set_name(user.get_name())
        user_dto.set_paternal_surname(user.get_paternal_surname())
        user_dto.set_maternal_surname(user.get_maternal_surname())
        user_dto.set_user_type_id(user.get_user_type_id())
        user_dto.set_user_name(user.get_user_name())

    def user_dto_to_user(self, user_dto:UserDto):
        user = User()
        user.set_id(user_dto.get_id())
        user.set_name(user_dto.get_name())
        user.set_paternal_surname(user_dto.get_paternal_surname())
        user.set_maternal_surname(user_dto.get_maternal_surname())
        user.set_user_type_id(user_dto.get_user_type_id())
        user.set_user_name(user_dto.get_user_name())