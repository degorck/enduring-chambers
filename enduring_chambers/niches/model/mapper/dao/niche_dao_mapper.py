"""
NicheDaoMapper Module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.niche import Niche
from niches.model.entity.holder import Holder
from niches.model.entity.row import Row
from niches.model.entity.module import Module

def real_dict_row_to_niche(real_dict_row:RealDictRow):
    """
    Maps Niche from a RealDictRow

    Arguments:
        real_dict_row : RealDictRow
            RealDictRow to be mapped
    Returns:
        niche : Niche
            Niche mapped from RealDictRow 
    """
    if real_dict_row is None:
        return None

    niche = Niche()
    if "module_id" in real_dict_row:
        module = Module()
        module.existing_module(
            int(real_dict_row["module_id"]),
            real_dict_row["module_name"],
            real_dict_row["module_is_active"],
            real_dict_row["module_created_at"],
            real_dict_row["module_updated_at"]
            )
    else:
        module = None

    if "row_id" in real_dict_row:
        row = Row()
        row.existing_row(
            int(real_dict_row["row_id"]),
            real_dict_row["row_name"],
            module,
            real_dict_row["row_created_at"],
            real_dict_row["row_updated_at"]
        )
    else:
        row = None

    if "holder_id" in real_dict_row:
        if real_dict_row["holder_id"] is None:
            holder = None
        else:
            holder = Holder()
            holder.existing_holder(
                int(real_dict_row["holder_id"]),
                real_dict_row["holder_name"],
                real_dict_row["paternal_surname"],
                real_dict_row["maternal_surname"],
                real_dict_row["phone"],
                real_dict_row["holder_is_active"],
                real_dict_row["holder_created_at"],
                real_dict_row["holder_updated_at"]
        )
    else:
        holder = None

    niche.existing_niche(
    real_dict_row["id"],
    row,
    str(real_dict_row["number"]),
    bool(real_dict_row["is_busy"]),
    bool(real_dict_row["is_paid_off"]),
    bool(real_dict_row["is_donated"]),
    holder,
    real_dict_row["is_active"],
    real_dict_row["created_at"],
    real_dict_row["updated_at"]
    )

    return niche
