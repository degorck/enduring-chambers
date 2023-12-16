"""
RowDaoMapper Module
"""
from niches.model.entity.row import Row
from niches.model.dto.row_dto import RowDto
from niches.model.mapper.module_mapper import module_dto_to_module, module_to_module_dto

def row_to_row_dto(row:Row):
    """
    Maps RowDto from a Row

    Arguments:
        row : Row
            Row to be mapped
    Returns:
        row_dto : RowDto
            RowDto mapped from Row 
    """
    if row is None:
        return None

    row_dto = RowDto()
    row_dto.set_id(row.get_id())
    row_dto.set_name(row.get_name())
    if row.get_module() is None:
        pass
    else:
        row_dto.set_module(module_to_module_dto(row.get_module()))

    if row.get_created_at() is None:
        pass
    else:
        row_dto.set_created_at(row.get_created_at())

    if row.get_updated_at() is None:
        pass
    else:
        row_dto.set_updated_at(row.get_updated_at())
    return row_dto

def row_dto_to_row(row_dto:RowDto):
    """
    Maps Row from a RowDto

    Arguments:
        row_dto: RowDto
            RowDto to be mapped
    Returns:
        row : Row
            Row mapped from RowDto 
    """
    if row_dto is None:
        return None
    row = Row()
    row.set_id(row_dto.get_id())
    row.set_name(row_dto.get_name())
    if row_dto.get_module() is None:
        pass
    else:
        row.set_module(module_dto_to_module(row_dto.get_module()))

    if row_dto.get_created_at() is None:
        pass
    else:
        row.set_created_at(row_dto.get_created_at())

    if row_dto.get_updated_at() is None:
        pass
    else:
        row.set_update_at(row_dto.get_updated_at())
    return row
