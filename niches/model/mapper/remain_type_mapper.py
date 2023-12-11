"""
RemainTypeMapper Module
"""
from niches.model.entity.remain_type import RemainType
from niches.model.dto.remain_type_dto import RemainTypeDto

class RemainTypeMapper:
    """
    RemainTypeMapper Class
    """
    def remain_type_to_remain_type_dto(self, remain_type:RemainType):
        """
        Maps RemainTypeDto from a RemainType
        
        Arguments:
            remain_type : RemainType
                RemainType to be mapped
        Returns:
            remain_type_dto : RemainTypeDto
                RemainTypeDto mapped from RemainType 
        """
        if remain_type is None:
            return None
        remain_type_dto = RemainTypeDto()
        remain_type_dto.existing_remain_type(
            remain_type.get_id(),
            remain_type.get_name(),
            remain_type.get_key(),
            remain_type.get_created_at(),
            remain_type.get_updated_at()
        )
        return remain_type_dto

    def remain_type_dto_to_remain_type(self, remain_type_dto:RemainTypeDto):
        """
        Maps RemainType from a RemainTypeDto
        
        Arguments:
            remain_type_dto : RemainTypeDto
                RemainTypeDto to be mapped
        Returns:
            remain_type : RemainType
                RemainType mapped from RemainTypeDto 
        """
        if remain_type_dto is None:
            return None
        remain_type = RemainType()
        remain_type.existing_remain_type(
            remain_type_dto.get_id(),
            remain_type_dto.get_name(),
            remain_type_dto.get_key(),
            remain_type_dto.get_created_at(),
            remain_type_dto.get_updated_at()
        )
        return remain_type
