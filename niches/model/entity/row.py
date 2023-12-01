"""
Row entity module
"""
import datetime
from niches.model.entity.module import Module

class Row:
    """
    Class row entity
        Properties:
            id: int
            name: str
            module: Module
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__module:Module = Module()
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

    def set_module(self, module:Module):
        """
        Sets module

        Arguments:
            module : Module
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

    def set_update_at(self, updated_at:datetime):
        """
        Sets updated_at

        Arguments:
            updated_at : datetime
                updated_at to set
        """
        self.__created_at = updated_at

    def new_row(self, name:str, module:Module):
        """
        Loads data for new row

        Arguments:
            name: str
                name of the row
        """
        self.__name = name
        self.__module = module

    def existing_row(self, row_id:int, name:str, module:Module, created_at:datetime, updated_at:datetime):
        """
        Loads data of an existing row

        Arguments:
            row_id: int
                id of the row
            name: str
                name of the row
            created_at: datetime
            updated_at: datetime
        """
        self.__id = row_id
        self.__name = name
        self.__module = module
        self.__created_at = created_at
        self.__updated_at = updated_at
