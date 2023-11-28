from psycopg2.extras import RealDictRow
from niches.model.entity.user import User

class UserDaoMapper:
    def real_dict_row_to_user(self, real_dict_row:RealDictRow):
        if real_dict_row == None:
            user = User()
        user = User()
        user.existing_user(
            real_dict_row["id"],
            real_dict_row["name"],
            real_dict_row["paternal_surname"],
            real_dict_row["maternal_surname"],
            real_dict_row["user_type_id"],
            real_dict_row["user_name"],
            real_dict_row["password"],
            real_dict_row["is_active"],
            real_dict_row["created_at"],
            real_dict_row["updated_at"]
            )
        return user