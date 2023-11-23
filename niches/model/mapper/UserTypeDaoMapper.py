from psycopg2.extras import RealDictRow
from niches.model.entity.UserType import UserType

class UserTypeDaoMapper:
    def real_dict_row_to_user(self, real_dict_row:RealDictRow):
        user_type = UserType()
        user_type.existing_user_type(
            real_dict_row["id"],
            real_dict_row["name"],
            real_dict_row["key"],
            real_dict_row["created_at"],
            real_dict_row["updated_at"]
            )
        return user_type