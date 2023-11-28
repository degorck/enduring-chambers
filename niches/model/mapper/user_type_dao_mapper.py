"""
UserTypeDao module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.user_type import UserType

class UserTypeDaoMapper:
    """
    UserTypeDaoMapper Class
    """
    def real_dict_row_to_user(self, real_dict_row:RealDictRow):
        """
        Maps UserType from a RealDictRow

        Arguments:
            real_dict_row : RealDictRow
                RealDictRow to be mapped
        Returns:
            user_type : UserType
                UserType mapped from RealDictRow 
        """
        user_type = UserType()
        user_type.existing_user_type(
            real_dict_row["id"],
            real_dict_row["name"],
            real_dict_row["key"],
            real_dict_row["created_at"],
            real_dict_row["updated_at"]
            )
        return user_type
