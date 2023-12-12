"""
DeceasedMapper Module
"""
from niches.model.entity.deceased import Deceased
from niches.model.dto.deceased_dto import DeceasedDto

def deceased_to_deceased_dto(deceased:Deceased):
    """
    Maps DeceasedDto from a Deceased

    Arguments:
        deceased : Deceased
            Deceased to be mapped
    Returns:
        deceased_dto : DeceasedDto
            DeceasedDto mapped from Deceased 
    """
    if deceased is None:
        return None

    deceased_dto = DeceasedDto()
    deceased_dto.existing_deceased(
        deceased.get_id(),
        deceased.get_name(),
        deceased.get_paternal_surname(),
        deceased.get_maternal_surname(),
        deceased.get_birth_date() if (deceased.get_birth_date() is not None) else None,
        deceased.get_death_date() if (deceased.get_death_date() is not None) else None,
        deceased.get_remain_type() if (deceased.get_remain_type() is not None) else None,
        deceased.get_niche() if (deceased.get_niche() is not None) else None,
        deceased.get_book(),
        deceased.get_sheet(),
        deceased.get_image_route(),
        deceased.get_created_at() if (deceased.get_created_at() is not None) else None,
        deceased.get_updated_at() if (deceased.get_updated_at() is not None) else None
    )

    return deceased_dto

def deceased_dto_to_deceased(deceased_dto:DeceasedDto):
    """
    Maps Deceased from a DeceasedDto

    Arguments:
        deceased_dto: DeceasedDto
            DeceasedDto to be mapped
    Returns:
        deceased : Deceased
            Deceased mapped from DeceasedDto 
    """
    if deceased_dto is None:
        return None

    deceased = Deceased()
    deceased.existing_deceased(
        deceased_dto.get_id(),
        deceased_dto.get_name(),
        deceased_dto.get_paternal_surname(),
        deceased_dto.get_maternal_surname() if (
            deceased_dto.get_maternal_surname() is not None) else None,
        deceased_dto.get_birth_date() if (deceased_dto.get_birth_date() is not None) else None,
        deceased_dto.get_death_date() if (deceased_dto.get_death_date() is not None) else None,
        deceased_dto.get_remain_type() if (deceased_dto.get_remain_type() is not None) else None,
        deceased_dto.get_niche() if (deceased_dto.get_niche() is not None) else None,
        deceased_dto.get_book(),
        deceased_dto.get_sheet(),
        deceased_dto.get_image_route() if (deceased_dto.get_image_route() is not None) else None,
        deceased_dto.get_created_at() if (deceased_dto.get_created_at() is not None) else None,
        deceased_dto.get_updated_at() if (deceased_dto.get_updated_at() is not None) else None,
    )

    return deceased
