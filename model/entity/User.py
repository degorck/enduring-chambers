import datetime

class User:
    def __init__(self):
        self.__id = 0
        self.__name = ""
        self.__paternal_surname = ""
        self.__maternal_surname = ""
        self.__user_type_id = 0
        self.__user_name = ""
        self.__password = ""
        self.__is_active = ""
        self.__created_at = ""
        self.__updated_at = ""
    
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
    
    def get_password(self):
        return self.__password
    
    def is_active(self):
        return self.__is_active
    
    def get_created_at(self):
        return self.__created_at
    
    def get_updated_at(self):
        return self.__updated_at
    
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name
    
    def set_paternal_surname(self, paternal_surname):
        self.__paternal_surname = paternal_surname
    
    def set_maternal_surname(self, maternal_surname):
        self.__maternal_surname = maternal_surname
    
    def set_user_type_id(self, user_type_id:int):
        self.__user_type_id = user_type_id
    
    def set_user_name(self, user_name):
        self.__user_name = user_name

    def existing_user(self, id:int, name:str, paternal_surname:str, maternal_surname:str,
                     user_type_id:int, user_name:str, password:str, is_active:bool, 
                     created_at:datetime, updated_at:datetime):
        self.__id = id
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__user_type_id = user_type_id
        self.__user_name = user_name
        self.__password = password
        self.__is_active = is_active
        self.__created_at = created_at
        self.__updated_at = updated_at
    
    def new_user(self, name:str, paternal_surname:str, maternal_surname:str, user_type:int, user_name:str):
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__user_type_id = user_type
        self.__user_name = user_name

    def update_user(self, id:int, name:str, paternal_surname:str, maternal_surname:str,
                    user_type_id:int, user_name:str):
        self.__id = id
        self.__name = name
        self.__paternal_surname = paternal_surname
        self.__maternal_surname = maternal_surname
        self.__user_type_id = user_type_id
        self.__user_name = user_name
    