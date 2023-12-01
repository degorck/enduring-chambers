"""
Holder entity module
"""
import datetime

class Holder:
    """
    Class holder entity
        Properties:
            id: int
            name: str
            paternal_surname: str
            maternal_surname: str
            phone: str
            is_active: bool
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__paternal_surname:str = ""
        self.__maternal_surname:str = ""
        self.__phone:str = ""
        self.__is_active:bool = False
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

    def get_paternal_surname(self):
        """
        Returns
            paternal_surname : str
        """
        return self.__paternal_surname

    def get_maternal_surname(self):
        """
        Returns
            maternal_surname : str
        """
        return self.__maternal_surname

    def get_phone(self):
        """
        Returns
            phone : str
        """
        return self.__phone

    def is_active(self):
        """
        Returns
            is_active : bool
        """
        return self.__is_active

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

    def set_id(self, holder_id:int):
        """
        Sets id

        Arguments:
            id : int
                id to set
        """
        self.__id = holder_id

    def set_name(self, name:str):
        """
        Sets name

        Arguments:
            name : str
                name to set
        """
        self.__name = name

    def set_paternal_surname(self, paternal_surname:str):
        """
        Sets paternal_surname

        Arguments:
            paternal_surname : str
                paternal_surname to set
        """
        self.__paternal_surname = paternal_surname

    def set_maternal_surname(self, maternal_surname:str):
        """
        Sets maternal_surname

        Arguments:
            maternal_surname : str
                maternal_surname to set
        """
        self.__maternal_surname = maternal_surname

    def set_phone(self, phone:str):
        """
        Sets phone

        Arguments:
            phone : str
                phone to set
        """
        self.__phone = phone

    def set_active(self, active:bool):
        """
        Sets active

        Arguments:
            active : bool
                active to set
        """
        self.__is_active = active

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

    def new_holder(self, name:str, paternal_surname:str, maternal_surname:str,
                   phone:str):
        """
        Loads data for new holder

        Arguments:
            name: str
                name of the holder
            paternal_surname: str
                paternal_surname of the holder
            maternal_surname: str
                maternal_surname of the hoder
            phone: str
                phone of the holder
        """
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__phone = phone

    def existing_holder(self, holder_id:int, name:str, paternal_surname:str,
                        maternal_surname:str, phone:str, is_active:bool,
                        created_at:datetime, updated_at:datetime):
        """
        Loads data of an existing holder

        Arguments:
            id: int
                id of the holder
            name: str
                name of the holder
            paternal_surname: str
                paternal_surname of the holder
            maternal_surname: str
                maternal_surname of the hoder
            phone: str
                phone of the holder
            is_active: bool
            created_at: datetime
            updated_at: datetime
        """
        self.__id = holder_id
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__phone = phone
        self.__is_active = is_active
        self.__created_at = created_at
        self.__updated_at = updated_at
