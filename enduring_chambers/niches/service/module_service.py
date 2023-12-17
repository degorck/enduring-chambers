"""
ModuleService Module for Enduring Chambers
"""
import logging
from niches.model.dto.module_dto import ModuleDto
from niches.model.dao.module_dao import ModuleDao
from niches.model.mapper.module_mapper import module_to_module_dto

class ModuleService:
    """
    Class with the functionality of ModuleService
    """
    def __init__(self):
        self.__module_dao = ModuleDao()

    def find_by_id(self, id_module:int):
        """
        Find module by its id
        Arguments:
            id_module : int
                id of the Module
        Returns:
            module_dto : ModuleDto
                Founded ModuleDto.
        """
        module_dto = ModuleDto()
        module_dto = module_to_module_dto(
            self.__module_dao.find_by_id(id_module))
        logging.debug("Se encontró el módulo por su id")
        return module_dto

    def find_all_active(self):
        """
        Find all modules

        Returns:
            list_module_dto : list<ModuleDto>
                All the ModuleDto
        """
        list_module_dto = []
        list_module = self.__module_dao.find_all_active()
        for module in list_module:
            list_module_dto.append(module_to_module_dto(module))
        logging.debug("Se obtuvieron todos los módulos")
        return list_module_dto
