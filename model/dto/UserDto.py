class UserDto:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__paternal_surname = ""
        self.__maternal_surname = ""
        self.__user_type_id = 0
        self.__user_name = ""


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
       
    def set_name(self, name):
        self.__name = name
    
    def set_paternal_surname(self, paternal_surname:str):
        self.__paternal_surname = paternal_surname
    
    def set_maternal_surname(self, maternal_surname:str):
        self.__maternal_surname = maternal_surname
    
    def set_user_type_id(self, user_type:int):
        self.__user_type_id = user_type
    
    def set_user_name(self, user_name:str):
        self.__user_name = user_name
    
