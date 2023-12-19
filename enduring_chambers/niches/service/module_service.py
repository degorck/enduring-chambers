"""
ModuleService Module for Enduring Chambers
"""
import logging
from niches.model.dto.module_dto import ModuleDto
from niches.model.dao.module_dao import ModuleDao
from niches.model.mapper.module_mapper import module_to_module_dto, module_dto_to_module
from niches.controller.error_controller import ErrorController

class ModuleService:
    """
    Class with the functionality of ModuleService
    """
    def __init__(self):
        self.__module_dao = ModuleDao()
        self.__error_controller = ErrorController()

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
        Find all active modules

        Returns:
            list_module_dto : list<ModuleDto>
                All the ModuleDto
        """
        list_module_dto = []
        list_module = self.__module_dao.find_all_active()
        for module in list_module:
            list_module_dto.append(module_to_module_dto(module))
        logging.debug("Se obtuvieron todos los módulos activos")
        return list_module_dto

    def find_all(self):
        """
        Find all modules

        Returns:
            list_module_dto : list<ModuleDto>
                All the ModuleDto
        """
        list_module_dto = []
        list_module = self.__module_dao.find_all()
        for module in list_module:
            list_module_dto.append(module_to_module_dto(module))
        logging.debug("Se obtuvieron todos los módulos")
        return list_module_dto

    def modify_module(self, module_dto:ModuleDto):
        """
        Modify module

        Arguments:
            module_dto: ModuleDto
                ModuleDto to be modified
        """
        self.__module_dao.modify_module(module_dto_to_module(module_dto))

    def create_module(self, module_dto:ModuleDto):
        """
        Saves the module on database.

        Arguments:
            module_dto: ModuleDto
                Data transfer object of the module to be saved
        Returns:
            module_dto: ModuleDto
                Module created
        """
        try:
            output = module_to_module_dto(
                self.__module_dao.create_module(
                    module_dto_to_module(module_dto)))

            logging.debug("Module created")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            logging.error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            logging.error(e)
            self.__error_controller.show()
            return None

    def reactivate_module(self, module_id:int):
        """
        Reactivate module by its id

        Arguments:
            module_id : int
                module_id of the module to be modified
        """
        self.__module_dao.reactivate_module(module_id)

    def deactivate_module(self, module_id:int):
        """
        Reactivate module by its id

        Arguments:
            module_id : int
                module_id of the module to be modified
        """
        self.__module_dao.deactivate_module(module_id)
