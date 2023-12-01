"""
ModuleDto module
"""
import datetime

class ModuleDto:
    """
    Class ModuleDto
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__created_at:datetime = None
        self.__updated_at:datetime = None

    def get_id(self):
        """
        Returns:
            id: int
                Module id
        """
        return self.__id

    def get_name(self):
        """
        Returns:
            name: str
                Module name
        """
        return self.__name

    def get_created_at(self):
        """
        Returns:
            created_at: datetime
                Module created_at
        """
        return self.__created_at

    def get_updated_at(self):
        """
        Returns:
            updated_at: datetime
                Module updated_at
        """
        return self.__updated_at

    def set_id(self, module_id:str):
        """
        Sets module id

        Arguments:
            module_id: int
                id to set
        """
        self.__id = module_id

    def set_name(self, name:str):
        """
        Sets name

        Arguments:
            name: str
                name to set
        """
        self.__name = name

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

    def new_module(self, name):
        """
        Loads data for a new module

        Arguments:
            name : str
                name for new module
        """
        self.__name = name

    def existing_module(self, module_id:int, name:str, created_at:datetime, updated_at:datetime):
        """
        Loads data for a new module

        Arguments:
            module_id: int
                id for new module
            name: str
                name for new module
            created_at: datetime
                created_at of new module
            updated_at: datetime
                updated_at of new module
        """
        self.__id = module_id
        self.__name = name
        self.__created_at = created_at
        self.__updated_at = updated_at
