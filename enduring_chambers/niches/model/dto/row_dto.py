"""
RowDto module
"""
import datetime
from niches.model.dto.module_dto import ModuleDto

class RowDto:
    """
    Class RowDto
        Properties:
            id: int
            name: str
            module: ModuleDto
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__module:ModuleDto = ModuleDto()
        self.__created_at:datetime = None
        self.__updated_at:datetime = None

    def get_id(self):
        """
        Returns
            id : int
        """
        return self.__id

    def get_name(self):
        """
        Returns
            name : str
        """
        return self.__name

    def get_module(self):
        """
        Returns
            module : Module
        """
        return self.__module

    def get_created_at(self):
        """
        Returns
            created_at : datetime
        """
        return self.__created_at

    def get_updated_at(self):
        """
        Returns
            updated_at : datetime
        """
        return self.__updated_at

    def set_id(self, row_id:int):
        """
        Sets id

        Arguments:
            id : int
                id to set
        """
        self.__id = row_id

    def set_name(self, name:str):
        """
        Sets name

        Arguments:
            name : str
                name to set
        """
        self.__name = name

    def set_module(self, module:ModuleDto):
        """
        Sets module

        Arguments:
            module : ModuleDto
                name to set
        """
        self.__module = module

    def set_created_at(self, created_at:datetime):
        """
        Sets created_at

        Arguments:
            created_at : datetime
                created_at to set
        """
        self.__created_at = created_at

    def set_updated_at(self, updated_at:datetime):
        """
        Sets updated_at

        Arguments:
            updated_at : datetime
                updated_at to set
        """
        self.__updated_at = updated_at

    def new_row(self, name:str, module_dto:ModuleDto):
        """
        Loads data for new row

        Arguments:
            name: str
                name of the row
            module_dto: ModuleDto
                Module where row is located
        """
        self.__name = name
        self.__module = module_dto

    def existing_row(self, row_id:int, name:str, module_dto:ModuleDto,
                     created_at:datetime, updated_at:datetime):
        """
        Loads data of an existing row

        Arguments:
            row_id: int
                id of the row
            name: str
                name of the row
            module_dto: ModuleDto
                Module where the row is located
            created_at: datetime
            updated_at: datetime
        """
        self.__id = row_id
        self.__name = name
        self.__module = module_dto
        self.__created_at = created_at
        self.__updated_at = updated_at

    def to_string(self):
        """
        Returns:
            row_dto:str
                Returns row_dto as string
        """
        if self.__module is None:
            module_str = None
        else:
            module_str = self.__module.to_string()

        return (f'id: \"{str(self.__id)}\" name: \"{self.__name}\" module: ' +
                f'\"[{module_str}]\" created_at \"{self.__created_at}\" ' +
                f'updated_at: \"{self.__updated_at}\"')
