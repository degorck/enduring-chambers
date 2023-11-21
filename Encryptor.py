import bcrypt
from dotenv import load_dotenv
import os

class Encryptor:
    def __init__(self):
        load_dotenv()
        self.__salt = os.getenv("SALT").encode('utf-8')

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.__salt).decode("utf-8")
    
    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)