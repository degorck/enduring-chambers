"""
Payment entity module
"""
import datetime
from niches.model.entity.niche import Niche

class Payment:
    """
    Class payment entity
        Properties:
            id: int
            niche: Niche
            quantity: floeat
            payment_date: datetime
            comments: str
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__niche:Niche = None
        self.__quantity:float = 0.0
        self.__payment_date:datetime = None
        self.__comments:str = None
        self.__created_at:datetime = None
        self.__updated_at:datetime = None

    def get_id(self):
        """
        Returns:
            id:int
                id of the payment
        """
        return self.__id

    def get_niche(self):
        """
        Returns:
            niche:Niche
                Niche related to the payment
        """
        return self.__niche

    def get_quantity(self):
        """
        Returns
            quantity:float
                quantity of the payment
        """
        return self.__quantity

    def get_payment_date(self):
        """
        Returns:
            payment_date:datetime
                payment_date of the payment
        """
        return self.__payment_date

    def get_comments(self):
        """
        Returns:
            comments:str
                comments of the payment
        """
        return self.__comments

    def get_created_at(self):
        """
        Returns:
            created_at:datetime
                created_at of the payment
        """
        return self.__created_at

    def get_updated_at(self):
        """
        Returns:
            updated_at:datetime
                updated_at of the payment
        """
        return self.__updated_at

    def set_id(self, payment_id:int):
        """
        Sets the id of the payment
        
        Arguments:
            payment_id:int
                id to set
        """
        self.__id = payment_id

    def set_niche(self, niche:Niche):
        """
        Sets niche of the payment
        
        Arguments:
            niche:Niche
                niche of the payment
        """
        if niche is None and self.__niche is None:
            pass
        else:
            self.__niche = niche

    def set_quantity(self, quantity:float):
        """
        Sets quantity of the payment

        Arguments:
            quantity:float
                quantity of the payment
        """
        self.__quantity = quantity

    def set_payment_date(self, payment_date:datetime):
        """
        Sets payment date of the payment

        Arguments:
            payment_date:datetime
                payment date of the payment 
        """
        if payment_date is None and self.__payment_date is None:
            pass
        else:
            self.__payment_date = payment_date

    def set_comments(self, comments:str):
        """
        Sets comments of the payment
        
        Arguments:
            comments:str
                comments of the payment
        """
        self.__comments = comments

    def set_created_at(self, created_at:datetime):
        """
        Sets created_at date of the payment

        Arguments:
            created_at:datetime
                created_at date of the payment 
        """
        if created_at is None and self.__created_at is None:
            pass
        else:
            self.__created_at = created_at

    def set_updated_at(self, updated_at:datetime):
        """
        Sets updated_at date of the payment

        Arguments:
            updated_at:datetime
                updated_at date of the payment 
        """
        if updated_at is None and self.__updated_at is None:
            pass
        else:
            self.__updated_at = updated_at

    def new_payment(self, niche:Niche, quantity:float, payment_date:datetime, comments:str):
        """
        Loads data for new payment
        
        Arguments:
            niche: Niche
            quantity: float
            payment_date: datetime
            comments: str
        """
        self.set_niche(niche)
        self.set_quantity(quantity)
        self.set_payment_date(payment_date)
        self.set_comments(comments)

    def existing_payment(self, payment_id:int, niche:Niche, quantity:float, payment_date:datetime,
                         comments:str, created_at:datetime, updated_at:datetime):
        """
        Loads data for new payment
        
        Arguments:
            id: int
            niche: Niche
            quantity: floeat
            payment_date: datetime
            comments: str
            created_at: datetime
            updated_at: datetime
        """
        self.set_id(payment_id)
        self.set_niche(niche)
        self.set_quantity(quantity)
        self.set_payment_date(payment_date)
        self.set_comments(comments)
        self.set_created_at(created_at)
        self.set_updated_at(updated_at)
