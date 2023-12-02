"""
RowDaoMapper Module
"""
from psycopg2.extras import RealDictRow
from niches.model.entity.row import Row
from niches.model.entity.module import Module

class RowDaoMapper:
    """
    RowDaoMapper Class
    """
    def real_dict_row_to_row(self, real_dict_row:RealDictRow):
        """
        Maps Row from a RealDictRow

        Arguments:
            real_dict_row : RealDictRow
                RealDictRow to be mapped
        Returns:
            row : Row
                Row mapped from RealDictRow 
        """
        if real_dict_row is None:
            row = Row()
        module = Module()
        module.existing_module(
            real_dict_row["id_module"],
            real_dict_row["module_name"],
            real_dict_row["module_created_at"],
            real_dict_row["module_updated_at"]
        )
        row = Row()
        row.existing_row(
            real_dict_row["id_module"],
            real_dict_row["name"],
            module,
            real_dict_row["created_at"],
            real_dict_row["updated_at"]
            )
        return row
