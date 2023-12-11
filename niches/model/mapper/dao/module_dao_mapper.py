"""
ModuleDaoMapper Module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.module import Module

def real_dict_row_to_module(real_dict_row:RealDictRow):
    """
    Maps Module from a RealDictRow

    Arguments:
        real_dict_row : RealDictRow
            RealDictRow to be mapped
    Returns:
        module : Module
            Module mapped from RealDictRow 
    """
    if real_dict_row is None:
        return None

    module = Module()
    module.existing_module(
        real_dict_row["id"],
        real_dict_row["name"],
        real_dict_row["created_at"],
        real_dict_row["updated_at"]
        )
    return module
