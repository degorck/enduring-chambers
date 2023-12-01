"""
UserDaoMapper Module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.user import User

class UserDaoMapper:
    """
    UserDaoMapper Class
    """
    def real_dict_row_to_user(self, real_dict_row:RealDictRow):
        """
        Maps User from a RealDictRow

        Arguments:
            real_dict_row : RealDictRow
                RealDictRow to be mapped
        Returns:
            user : User
                User mapped from RealDictRow 
        """
        if real_dict_row is None:
            user = User()
        user = User()
        user.existing_user(
            real_dict_row["id_user"],
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
