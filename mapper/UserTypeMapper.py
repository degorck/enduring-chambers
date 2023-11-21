import repackage
repackage.up()
from model.entity.UserType import UserType
from model.dto.UserTypeDto import UserTypeDto

class UserTypeMapper:
    def __init__(self):
        pass

    def user_type_to_user_type_dto(self, user_type:UserType):
        user_type_dto = UserTypeDto()
        user_type_dto.existing_user_type(
            user_type.get_id(),
            user_type.get_name(),
            user_type.get_key(),
            user_type.get_created_at(),
            user_type.get_updated_at()
        )
        return user_type_dto

    def user_type_dto_to_user_type(self, user_type_dto:UserTypeDto):
        user_type = UserType()
        user_type.existing_user_type(
            user_type_dto.get_id(),
            user_type_dto.get_name(),
            user_type_dto.get_key(),
            user_type_dto.get_created_at(),
            user_type_dto.get_updated_at()
        )
        return user_type