import datetime

class UserTypeDto:
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__key:str = ""
        self.__created_at:datetime = None
        self.__updated_at:datetime = None

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_key(self):
        return self.__key

    def get_created_at(self):
        return self.__created_at

    def get_updated_at(self):
        return self.__updated_at

    def existing_user_type(self, user_type_id:int, name:str,
                           key:str, created_at:datetime, updated_at:datetime):
        self.__id = user_type_id
        self.__name = name
        self.__key = key
        self.__created_at = created_at
        self.__updated_at = updated_at
