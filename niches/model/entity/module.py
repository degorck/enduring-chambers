"""
Module entity module
"""
import datetime

class Module:
    """
    Class module entity
        Properties:
            id: int
            name: str
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
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

    def set_id(self, module_id:int):
        """
        Sets id

        Arguments:
            id : int
                id to set
        """
        self.__id = module_id

    def set_name(self, name:str):
        """
        Sets name

        Arguments:
            name : str
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

    def set_update_at(self, updated_at:datetime):
        """
        Sets updated_at

        Arguments:
            updated_at : datetime
                updated_at to set
        """
        self.__created_at = updated_at

    def new_module(self, name:str):
        """
        Loads data for new module

        Arguments:
            name: str
                name of the module
        """
        self.__name = name

    def existing_module(self, module_id:int, name:str, created_at:datetime, updated_at:datetime):
        """
        Loads data of an existing module

        Arguments:
            module_id: int
                id of the module
            name: str
                name of the module
            created_at: datetime
            updated_at: datetime
        """
        self.__id = module_id
        self.__name = name
        self.__created_at = created_at
        self.__updated_at = updated_at
