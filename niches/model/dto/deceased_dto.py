"""
DeceasedDto module
"""
import datetime
from niches.model.dto.niche_dto import NicheDto
from niches.model.dto.remain_type_dto import RemainTypeDto

class DeceasedDto:
    """
    Class DeceasedDto
        Properties:
            id: int
            name: str
            paternal_surname: str
            maternal_surname: str
            birth_date: datetime
            death_date: datetime
            remain_type: RemainType
            niche: Niche
            book: str
            sheet: str
            image_route: str
            created_at: datetime
            updated_at: datetime
    """
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__paternal_surname:str = ""
        self.__maternal_surname:str = ""
        self.__birth_date:datetime = None
        self.__death_date:datetime = None
        self.__remain_type_dto:RemainTypeDto = None
        self.__niche_dto: NicheDto = None
        self.__book:str = ""
        self.__sheet:str = ""
        self.__image_route:str = ""
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

    def get_birth_date(self):
        """
        Returns
            birth_date : datetime
        """
        return self.__birth_date

    def get_death_date(self):
        """
        Returns
            death_date : datetime
        """
        return self.__death_date

    def get_remain_type(self):
        """
        Returns
            remain_type : RemainTyep
        """
        return self.__remain_type_dto

    def get_niche(self):
        """
        Returns
            niche : Niche
        """
        return self.__niche_dto

    def get_book(self):
        """
        Returns
            book : str
        """
        return self.__book

    def get_sheet(self):
        """
        Returns
            sheet : str
        """
        return self.__sheet

    def get_image_route(self):
        """
        Returns
            image_route : str
        """
        return self.__image_route

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

    def set_id(self, deceased_id:int):
        """
        Sets id

        Arguments:
            id : int
                id to set
        """
        if deceased_id is None:
            pass
        else:
            self.__id = deceased_id

    def set_name(self, name:str):
        """
        Sets name

        Arguments:
            name : str
                name to set
        """
        if name is None:
            pass
        else:
            self.__name = name

    def set_paternal_surname(self, paternal_surname:str):
        """
        Sets paternal_surname

        Arguments:
            paternal_surname : str
                paternal_surname to set
        """
        if paternal_surname is None:
            pass
        else:
            self.__paternal_surname = paternal_surname

    def set_maternal_surname(self, maternal_surname:str):
        """
        Sets maternal_surname

        Arguments:
            maternal_surname : str
                maternal_surname to set
        """
        if maternal_surname is None:
            pass
        else:
            self.__maternal_surname = maternal_surname

    def set_birth_date(self, birth_date:datetime):
        """
        Sets birth_date

        Arguments:
            birth_date : datetime
                birth_date to set
        """
        if birth_date is None:
            pass
        else:
            self.__birth_date = birth_date

    def set_death_date(self, death_date:datetime):
        """
        Sets death_date

        Arguments:
            death_date : datetime
                death_date to set
        """
        if death_date is None:
            pass
        else:
            self.__death_date = death_date

    def set_remain_type(self, remain_type:RemainTypeDto):
        """
        Sets remain_type

        Arguments:
            remain_type : RemainType
                remain_type to set
        """
        if remain_type is None:
            pass
        else:
            self.__remain_type_dto = remain_type

    def set_niche(self, niche:NicheDto):
        """
        Sets niche

        Arguments:
            niche : Niche
                niche to set
        """
        if niche is None:
            pass
        else:
            self.__niche_dto = niche

    def set_book(self, book:str):
        """
        Sets book

        Arguments:
            book : str
                book to set
        """
        if book is None:
            pass
        else:
            self.__book = book

    def set_sheet(self, sheet:str):
        """
        Sets sheet

        Arguments:
            sheet : str
                sheet to set
        """
        if sheet is None:
            pass
        else:
            self.__sheet = sheet

    def set_image_route(self, image_route:str):
        """
        Sets image_route

        Arguments:
            image_route : str
                image_route to set
        """
        if image_route is None:
            pass
        else:
            self.__image_route = image_route

    def set_is_active(self, is_active:bool):
        """
        Sets is_active

        Arguments:
            is_active : bool
        """
        self.__is_active = is_active

    def set_created_at(self, created_at:datetime):
        """
        Sets created_at

        Arguments:
            created_at : datetime
                created_at to set
        """
        if created_at is None:
            pass
        else:
            self.__created_at = created_at

    def set_updated_at(self, updated_at:datetime):
        """
        Sets updated_at

        Arguments:
            updated_at : datetime
                updated_at to set
        """
        if updated_at is None:
            pass
        else:
            self.__updated_at = updated_at

    def new_deceased(self, name:str, paternal_surname:str, maternal_surname:str,
                     birth_date:datetime, death_date:datetime, remain_type:RemainTypeDto,
                     niche:NicheDto, book:str, sheet:str, image_route:str):
        """
        Loads data for new deceased

        Arguments:
            name: str
                name of the deceased
            paternal_surname: str
                paternal_surname of the deceased
            maternal_surname: str
                maternal_surname of the deceased
            birth_date: datetime
                datetime of the deceased
            death_date: datetime
                death_date of the deceased
            remain_type: RemainType
                remain_type of the deceased
            niche: Niche
                niche of the deceased
            book: str
                book of the deceased
            sheet: str
                sheet of the deceased
            image_route: str
                image_route of the deceased
        """
        self.set_name(name)
        self.set_paternal_surname(paternal_surname)
        self.set_maternal_surname(maternal_surname)
        self.set_birth_date(birth_date)
        self.set_death_date(death_date)
        self.set_remain_type(remain_type)
        self.set_niche(niche)
        self.set_book(book)
        self.set_sheet(sheet)
        self.set_image_route(image_route)

    def existing_deceased(self, deceased_id:int, name:str, paternal_surname:str,
                          maternal_surname:str, birth_date:datetime, death_date:datetime,
                          remain_type:RemainTypeDto, niche:NicheDto, book:str, sheet:str,
                          image_route:str, is_active:bool, created_at:datetime, 
                          updated_at:datetime):
        """
        Loads data for existing deceased

        Arguments:
            id: int
                id of the deceased
            name: str
                name of the deceased
            paternal_surname: str
                paternal_surname of the deceased
            maternal_surname: str
                maternal_surname of the deceased
            birth_date: datetime
                datetime of the deceased
            death_date: datetime
                death_date of the deceased
            remain_type: RemainType
                remain_type of the deceased
            niche: Niche
                niche of the deceased
            book: str
                book of the deceased
            sheet: str
                sheet of the deceased
            image_route: str
                image_route of the deceased
            is_active: bool
            created_at: datetime
                created_at of the deceased
            updated_at: datetime
                updated_at of the deceased
        """
        self.set_id(deceased_id)
        self.set_name(name)
        self.set_paternal_surname(paternal_surname)
        self.set_maternal_surname(maternal_surname)
        self.set_birth_date(birth_date)
        self.set_death_date(death_date)
        self.set_remain_type(remain_type)
        self.set_niche(niche)
        self.set_book(book)
        self.set_sheet(sheet)
        self.set_image_route(image_route)
        self.set_is_active(is_active)
        self.set_created_at(created_at)
        self.set_updated_at(updated_at)

    def to_string(self):
        """
        Returns:
            deceased_dto:str
                deceased_dto as string
        """
        if self.__remain_type_dto is None:
            remain_type_dto_str = None
        else:
            remain_type_dto_str = self.__remain_type_dto.to_string()

        if self.__niche_dto is None:
            niche_dto_str = None
        else:
            niche_dto_str = self.__niche_dto.to_string()

        return (f'id: \"{str(self.__id)}\" name:  \"{self.__name}\" paternal_surname: ' +
                f'\"{self.__paternal_surname}\" maternal_surname: \"{self.__maternal_surname}\" ' +
                f'bith_date: \"{self.__birth_date}\" death_date: ' +
                f'\"{self.__death_date}\" remain_type: ' +
                f'\"[{remain_type_dto_str}]\" ' +
                f'niche: \"[{niche_dto_str}]\" book: \"{self.__book}\" ' +
                f'sheet: \"{self.__sheet}\" image_route: \"{self.__image_route}\" ' +
                f'is_active: \"{self.__is_active}\" created_at \"{self.__created_at}\" ' +
                f'updated_at \"{self.__updated_at}\"')
