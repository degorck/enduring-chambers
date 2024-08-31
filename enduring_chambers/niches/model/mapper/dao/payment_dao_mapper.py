"""
RealDictRowMapper to Payment module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.payment import Payment
from niches.model.entity.niche import Niche
from niches.model.entity.row import Row
from niches.model.entity.module import Module
from niches.model.entity.holder import Holder

def real_dict_row_to_payment(real_dict_row:RealDictRow):
    """
    Maps Payment from a RealDictRow

    Arguments:
        real_dict_row : RealDictRow
            RealDictRow to be mapped
    Returns:
        payment : Payment
            Payment mapped from RealDictRow 
    """
    if real_dict_row is None:
        return None

    if "module_id" in real_dict_row:
        module = Module()
        module.existing_module(
            real_dict_row["module_id"],
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
            real_dict_row["row_id"],
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
                real_dict_row["holder_id"],
                real_dict_row["holder_name"],
                real_dict_row["holder_paternal_surname"],
                real_dict_row["holder_maternal_surname"],
                real_dict_row["holder_phone"],
                real_dict_row["holder_is_active"],
                real_dict_row["holder_created_at"],
                real_dict_row["holder_updated_at"]
            )
    else:
        holder = None

    if "niche_id" in real_dict_row:
        niche = Niche()
        niche.existing_niche(
            real_dict_row["niche_id"],
            row,
            real_dict_row["niche_number"],
            real_dict_row["niche_is_busy"],
            real_dict_row["niche_is_paid_off"],
            real_dict_row["niche_is_donated"],
            holder,
            real_dict_row["niche_is_active"],
            real_dict_row["niche_created_at"],
            real_dict_row["niche_updated_at"]
        )
    else:
        niche = None

    payment = Payment()
    payment.existing_payment(
        real_dict_row["id"],
        niche,
        real_dict_row["quantity"],
        real_dict_row["payment_date"],
        real_dict_row["comments"],
        real_dict_row["created_at"],
        real_dict_row["updated_at"]
        )
    return payment
