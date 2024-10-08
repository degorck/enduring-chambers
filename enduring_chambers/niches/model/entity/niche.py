"""
Niche entity module
"""
import datetime
from niches.model.entity.row import Row
from niches.model.entity.holder import Holder

class Niche:
    """
    Class niche entity
        Properties:
            id: int
            row: Row
            number: str
            is_busy: bool
            is_paid_off: bool
            is_donated: bool
            holder: Holder
            is_active: bool
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__row:Row = None
        self.__number:str = ""
        self.__is_busy:bool = False
        self.__is_paid_off:bool = False
        self.__is_donated:bool = False
        self.__holder:Holder = None
        self.__is_active:bool = False
        self.__created_at:datetime = None
        self.__updated_at:datetime = None

    def get_id(self):
        """
        Returns
            id : int
        """
        return self.__id

    def get_row(self):
        """
        Returns
            row : Row
        """
        return self.__row

    def get_number(self):
        """
        Returns
            number : str
        """
        return self.__number

    def is_busy(self):
        """
        Returns
            is_busy : bool
        """
        return self.__is_busy

    def is_paid_off(self):
        """
        Returns
            is_paid_off : bool
        """
        return self.__is_paid_off

    def is_donated(self):
        """
        Returns
            is_donated : bool
        """
        return self.__is_donated

    def get_holder(self):
        """
        Returns
            holder : Holder
        """
        return self.__holder

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

    def set_id(self, niche_id:int):
        """
        Sets id

        Arguments:
            id : int
                id to set
        """
        self.__id = niche_id

    def set_row(self, row:Row):
        """
        Sets row

        Arguments:
            row : Row
                row to set
        """
        self.__row = row

    def set_number(self, number:str):
        """
        Sets number

        Arguments:
            number : str
                number to set
        """
        self.__number = number

    def set_is_busy(self, is_busy:bool):
        """
        Sets is_busy

        Arguments:
            is_busy : bool
                is_busy to set
        """
        self.__is_busy = is_busy

    def set_is_paid_off(self, is_paid_off:bool):
        """
        Sets is_paid_off

        Arguments:
            is_paid_off : bool
                is_paid_off to set
        """
        self.__is_paid_off = is_paid_off

    def set_is_donated(self, is_donated:bool):
        """
        Sets is_donated

        Arguments:
            is_donated : bool
                is_donated to set
        """
        self.__is_donated = is_donated

    def set_holder(self, holder:Holder):
        """
        Sets holder

        Arguments:
            holder : Holder
                Holder to set
        """
        self.__holder = holder

    def set_active(self, is_active:bool):
        """
        Sets is_active

        Arguments:
            is_active : bool
                is_active to set
        """
        self.__is_active = is_active

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

    def new_niche(self, row:Row, number:str, is_busy:bool, is_paid_off:bool,
                  is_donated:bool,
                  holder:Holder):
        """
        Loads data for new niche

        Arguments:
            row: Row
                Row of the niche
            number: str
                number of the niche
            is_busy: bool
                if the niche is busy
            is_paid_off: bool
                if the niche is paid off
            holder: Holder
                holder of the niche
        """
        self.__row = row
        self.__number = number
        self.__is_busy = is_busy
        self.__is_paid_off = is_paid_off
        self.__is_donated = is_donated
        self.__holder:Holder = holder

    def existing_niche(self, niche_id:int, row:Row, number:str, is_busy:bool,
                       is_paid_off:bool, is_donated:bool, holder:Holder, is_active:bool,
                       created_at:datetime, updated_at:datetime):
        """
        Loads data of an existing niche

        Arguments:
            niche_id: int
                id of the niche
            name: str
                name of the niche
            created_at: datetime
            updated_at: datetime
        """
        self.__id = niche_id
        self.__row = row
        self.__number = number
        self.__is_busy = is_busy
        self.__is_paid_off = is_paid_off
        self.__is_donated = is_donated
        self.__holder = holder
        self.__is_active = is_active
        self.__created_at = created_at
        self.__updated_at = updated_at
