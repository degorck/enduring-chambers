"""
UserMapper Module
"""
from niches.model.entity.user import User
from niches.model.dto.user_dto import UserDto

def user_to_user_dto(user:User):
    """
    Maps UserDto from a User

    Arguments:
        user : User
            User to be mapped
    Returns:
        user_dto : UserDto
            UserDto mapped from User 
    """
    if user is None:
        return None

    user_dto = UserDto()
    user_dto.set_id(int(user.get_id()))
    user_dto.set_name(str(user.get_name()))
    user_dto.set_paternal_surname(str(user.get_paternal_surname()))
    user_dto.set_maternal_surname(str(user.get_maternal_surname()))
    user_dto.set_user_type_id(int(user.get_user_type_id()))
    user_dto.set_user_name(str(user.get_user_name()))
    user_dto.set_password(str(user.get_password()))
    user_dto.set_is_active(bool(user.is_active()))
    if user.get_created_at() is None:
        pass
    else:
        user_dto.set_created_at(user.get_created_at())
    if user.get_updated_at() is None:
        pass
    else:
        user_dto.set_updated_at(user.get_updated_at())
    return user_dto

def user_dto_to_user(user_dto:UserDto):
    """
    Maps User from a UserDto

    Arguments:
        user_dto : UserDto
            UserDto to be mapped
    Returns:
        user : User
            User mapped from UserDto 
    """
    if user_dto is None:
        return None

    user = User()
    if user_dto.get_id() is None:
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
    if user_dto.get_created_at() is None:
        pass
    else:
        user.set_created_at(user_dto.get_created_at())
    if user_dto.get_updated_at() is None:
        pass
    else:
        user.set_updated_at(user_dto.get_updated_at())
    return user
