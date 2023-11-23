from niches.model.entity.User import User
from niches.model.dto.UserDto import UserDto
import datetime

class UserMapper:
    def __init__(self):
        pass

    def user_to_user_dto(self, user:User):
        user_dto = UserDto()
        user_dto.set_id(int(user.get_id()))
        user_dto.set_name(str(user.get_name()))
        user_dto.set_paternal_surname(str(user.get_paternal_surname()))
        user_dto.set_maternal_surname(str(user.get_maternal_surname()))
        user_dto.set_user_type_id(int(user.get_user_type_id()))
        user_dto.set_user_name(str(user.get_user_name()))
        user_dto.set_password(str(user.get_password()))
        user_dto.set_is_active(bool(user.is_active()))
        if user.get_created_at() == None:
            pass
        else:
            user_dto.set_created_at(user.get_created_at())
        if user.get_updated_at() == None:
            pass
        else:
            user_dto.set_updated_at(user.get_updated_at())
        return user_dto

    def user_dto_to_user(self, user_dto:UserDto):
        user = User()
        if user_dto.get_id() == None:
            pass
        else:
            user.set_id(int(user_dto.get_id()))
        user.set_name(str(user_dto.get_name()))
        user.set_paternal_surname(str(user_dto.get_paternal_surname()))
        user.set_maternal_surname(str(user_dto.get_maternal_surname()))
        user.set_user_type_id(int(user_dto.get_user_type_id()))
        user.set_user_name(str(user_dto.get_user_name()))
        user.set_password(str(user_dto.get_password()))
        user.set_is_active(bool(user_dto.is_active()))
        if user_dto.get_created_at() == None:
            pass
        else:
            user.set_created_at(user_dto.get_created_at())
        if user_dto.get_updated_at() == None:
            pass
        else:
            user.set_updated_at(user_dto.get_updated_at())
        return user
