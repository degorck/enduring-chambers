"""
RemainTypeDao module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.remain_type import RemainType

def real_dict_row_to_remain_type(real_dict_row:RealDictRow):
    """
    Maps RemainType from a RealDictRow

    Arguments:
        real_dict_row : RealDictRow
            RealDictRow to be mapped
    Returns:
        remain_type : RemainType
            RemainType mapped from RealDictRow 
    """
    if real_dict_row is None:
        return None

    user_type = RemainType()
    user_type.existing_remain_type(
        real_dict_row["id"],
        real_dict_row["name"],
        real_dict_row["key"],
        real_dict_row["created_at"],
        real_dict_row["updated_at"]
        )
    return user_type
