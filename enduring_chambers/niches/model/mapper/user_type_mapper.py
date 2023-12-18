"""
UserTypeMapper Module
"""
from niches.model.entity.user_type import UserType
from niches.model.dto.user_type_dto import UserTypeDto

def user_type_to_user_type_dto(user_type:UserType):
    """
    Maps UserTypeDto from a UserType
        
    Arguments:
        user_type : UserType
            UserType to be mapped
    Returns:
        user_type_dto : UserTypeDto
            UserTypeDto mapped from UserType 
    """
    if user_type is None:
        return None

    user_type_dto = UserTypeDto()
    user_type_dto.existing_user_type(
        user_type.get_id(),
        user_type.get_name(),
        user_type.get_key(),
        user_type.get_created_at(),
        user_type.get_updated_at()
    )
    return user_type_dto

def user_type_dto_to_user_type(user_type_dto:UserTypeDto):
    """
    Maps UserType from a UserTypeDto

    Arguments:
        user_type_dto : UserType_dto
            UserTypeDto to be mapped
    Returns:
        user_type : UserType
            UserType mapped from UserTypeDto 
    """
    if user_type_dto is None:
        return None
    user_type = UserType()
    user_type.existing_user_type(
        user_type_dto.get_id(),
        user_type_dto.get_name(),
        user_type_dto.get_key(),
        user_type_dto.get_created_at(),
        user_type_dto.get_updated_at()
    )
    return user_type
