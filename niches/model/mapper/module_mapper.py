"""
ModuleDaoMapper Module
"""
from niches.model.entity.module import Module
from niches.model.dto.module_dto import ModuleDto

def module_to_module_dto(module:Module):
    """
    Maps ModuleDto from a Module

    Arguments:
        module : Module
            Module to be mapped
    Returns:
        module_dto : ModuleDto
            ModuleDto mapped from Module 
    """
    if module is None:
        return None

    module_dto = ModuleDto()
    module_dto.set_id(module.get_id())
    module_dto.set_name(module.get_name())
    if module.get_created_at() is None:
        pass
    else:
        module_dto.set_created_at(module.get_created_at())
    if module.get_updated_at() is None:
        pass
    else:
        module_dto.set_updated_at(module.get_updated_at())
    return module_dto

def module_dto_to_module(module_dto:ModuleDto):
    """
    Maps Module from a ModuleDto

    Arguments:
        module_dto: ModuleDto
            ModuleDto to be mapped
    Returns:
        module : Module
             Module mapped from ModuleDto 
    """
    if module_dto is None:
        return None

    module = Module()
    module.set_id(module_dto.get_id())
    module.set_name(module_dto.get_name())
    if module_dto.get_created_at() is None:
        pass
    else:
        module.set_created_at(module_dto.get_created_at())
    if module_dto.get_updated_at() is None:
        pass
    else:
        module.set_update_at(module_dto.get_updated_at())
    return module
