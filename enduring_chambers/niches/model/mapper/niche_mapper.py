"""
NicheMapper Module
"""
from niches.model.entity.niche import Niche
from niches.model.dto.niche_dto import NicheDto
from niches.model.mapper.row_mapper import row_to_row_dto, row_dto_to_row
from niches.model.mapper.holder_mapper import holder_dto_to_holder, holder_to_holder_dto

def niche_to_niche_dto(niche:Niche):
    """
    Maps NicheDto from a Niche

    Arguments:
        niche : Niche
            Niche to be mapped
    Returns:
        niche_dto : NicheDto
            NicheDto mapped from Niche 
    """
    if niche is None:
        return None

    niche_dto = NicheDto()
    niche_dto.set_id(niche.get_id())
    if niche.get_row() is None:
        pass
    else:
        niche_dto.set_row(row_to_row_dto(niche.get_row()))

    niche_dto.set_number(niche.get_number())
    niche_dto.set_is_busy(niche.is_busy())
    niche_dto.set_is_paid_off(niche.is_paid_off())
    niche_dto.set_is_donated(niche.is_donated())
    if niche.get_holder() is None:
        pass
    else:
        niche_dto.set_holder(holder_to_holder_dto(niche.get_holder()))

    niche_dto.set_active(niche.is_active())

    if niche.get_created_at() is None:
        pass
    else:
        niche_dto.set_created_at(niche.get_created_at())
    if niche.get_updated_at() is None:
        pass
    else:
        niche_dto.set_updated_at(niche.get_updated_at())
    return niche_dto

def niche_dto_to_niche(niche_dto:NicheDto):
    """
    Maps Niche from a NicheDto

    Arguments:
        niche_dto: NicheDto
            NicheDto to be mapped
    Returns:
        niche : Niche
            Niche mapped from NicheDto 
    """
    if niche_dto is None:
        return None

    niche = Niche()
    niche.set_id(niche_dto.get_id())

    if niche_dto.get_row() is None:
        pass
    else:
        niche.set_row(row_dto_to_row(niche_dto.get_row()))

    niche.set_number(niche_dto.get_number())
    niche.set_is_busy(niche_dto.is_busy())
    niche.set_is_paid_off(niche_dto.is_paid_off())
    niche.set_is_donated(niche_dto.is_donated())

    if niche_dto.get_holder() is None:
        pass
    else:
        niche.set_holder(holder_dto_to_holder(niche_dto.get_holder()))

    niche.set_active(niche_dto.is_active())

    if niche_dto.get_created_at() is None:
        pass
    else:
        niche.set_created_at(niche_dto.get_created_at())

    if niche_dto.get_updated_at() is None:
        pass
    else:
        niche.set_updated_at(niche_dto.get_updated_at())

    return niche
