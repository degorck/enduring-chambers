"""
HolderDaoMapper Module
"""
from niches.model.entity.holder import Holder
from niches.model.dto.holder_dto import HolderDto

class HolderMapper:
    """
    UserTypeMapper Class
    """
    def holder_to_holder_dto(self, holder:Holder):
        """
        Maps HolderDto from a Holder

        Arguments:
            holder : Holder
                Holder to be mapped
        Returns:
            holder_dto : HolderDto
                HolderDto mapped from Holder 
        """
        holder_dto = HolderDto()
        holder_dto.set_id(holder.get_id())
        holder_dto.set_name(holder.get_name())
        holder_dto.set_paternal_surname(holder.get_paternal_surname())
        holder_dto.set_maternal_surname(holder.get_maternal_surname())
        holder_dto.set_phone(holder.get_phone())
        holder_dto.set_active(holder.is_active())
        if holder.get_created_at() is None:
            pass
        else:
            holder_dto.set_created_at(holder.get_created_at())
        if holder.get_updated_at() is None:
            pass
        else:
            holder_dto.set_update_at(holder.get_updated_at())
        return holder_dto

    def holder_dto_to_holder(self, holder_dto:HolderDto):
        """
        Maps Holder from a HolderDto

        Arguments:
            holder_dto: HolderDto
                HolderDto to be mapped
        Returns:
            holder : Holder
                Holder mapped from HolderDto 
        """
        holder = Holder()
        holder.set_id(holder_dto.get_id())
        holder.set_name(holder_dto.get_name())
        holder.set_paternal_surname(holder_dto.get_paternal_surname())
        holder.set_maternal_surname(holder_dto.get_maternal_surname())
        holder.set_phone(holder_dto.get_phone())
        holder.set_active(holder_dto.is_active())
        if holder_dto.get_created_at() is None:
            pass
        else:
            holder.set_created_at(holder.get_created_at())
        if holder_dto.get_updated_at() is None:
            pass
        else:
            holder.set_update_at(holder.get_updated_at())
        return holder
