"""
HolderDaoMapper Module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.holder import Holder

class HolderDaoMapper:
    """
    HolderDaoMapper Class
    """
    def real_dict_row_to_holder(self, real_dict_row:RealDictRow):
        """
        Maps Holder from a RealDictRow

        Arguments:
            real_dict_row : RealDictRow
                RealDictRow to be mapped
        Returns:
            holder : Holder
                Holder mapped from RealDictRow 
        """
        if real_dict_row is None:
            holder = Holder()
        holder = Holder()
        holder.existing_holder(
            real_dict_row["id"],
            real_dict_row["name"],
            real_dict_row["paternal_surname"],
            real_dict_row["maternal_surname"],
            real_dict_row["phone"],
            real_dict_row["is_active"],
            real_dict_row["created_at"],
            real_dict_row["updated_at"]
            )
        return holder
