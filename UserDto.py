import datetime

class UserDto:
    def __init__(self):
        self.__id:int = 0
        self.__name:str = ""
        self.__paternal_surname:str = ""
        self.__maternal_surname:str = ""
        self.__user_type_id:int = 0
        self.__user_name:str = ""
        self.__is_active:bool = False
        self.__created_at:datetime = None
        self.__updated_at:datetime = None


    def new_user(self, name:str, paternal_surname:str, maternal_surname:str, user_type:int, user_name:str):
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__user_type_id = user_type
        self.__user_name = user_name
    
    def existing_user(self, id:int, name:str, paternal_surname:str, maternal_surname:str, user_type:int, user_name:str):
        self.__id = id
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__user_type_id = user_type
        self.__user_name = user_name

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_paternal_surname(self):
        return self.__paternal_surname
    
    def get_maternal_surname(self):
        return self.__maternal_surname
    
    def get_user_type_id(self):
        return self.__user_type_id
    
    def get_user_name(self):
        return self.__user_name
    
    def is_active(self):
        return self.__is_active
    
    def get_created_at(self):
        return self.__created_at
    
    def get_updated_at(self):
        return self.__updated_at
    
    def set_id(self, id:int):
        self.__id = id
       
    def set_name(self, name:str):
        self.__name = name
    
    def set_paternal_surname(self, paternal_surname:str):
        self.__paternal_surname = paternal_surname
    
    def set_maternal_surname(self, maternal_surname:str):
        self.__maternal_surname = maternal_surname
    
    def set_user_type_id(self, user_type:int):
        self.__user_type_id = user_type
    
    def set_user_name(self, user_name:str):
        self.__user_name = user_name

    def set_is_active(self, is_active:bool):
        self.__is_active = is_active
    
    def set_created_at(self, created_at:datetime):
        self.__created_at = created_at
    
    def set_updated_at(self, updated_at:datetime):
        self.__updated_at = updated_at
