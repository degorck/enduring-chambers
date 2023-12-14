import datetime

class RemainTypeDto:
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

    def existing_remain_type(self, remain_type_id:int, name:str,
                             key:str, created_at:datetime, updated_at:datetime):
        self.__id = remain_type_id
        self.__name = name
        self.__key = key
        self.__created_at = created_at
        self.__updated_at = updated_at

    def to_string(self):
        return (f'id: \"{str(self.__id)}\" name: \"{self.__name}\" key: \"{self.__key}\" ' +
                f'created_at: \"{self.__created_at}\" updated_at: \"{self.__updated_at}\"')
