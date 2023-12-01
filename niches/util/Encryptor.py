import bcrypt
from dotenv import load_dotenv
import os
from niches.constants.constants import UTF_8
import logging

class Encryptor:
    def __init__(self):
        load_dotenv()
        self.__salt = os.getenv("SALT").encode(UTF_8)

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode(UTF_8), self.__salt).decode(UTF_8)
    
    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode(UTF_8), hashed_password.encode(UTF_8))