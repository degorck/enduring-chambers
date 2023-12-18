"""
Module encryptor used to hash data
"""
import os
import bcrypt
from dotenv import load_dotenv
from niches.constant.constants import UTF_8

class Encryptor:
    """
    Class with encryptor configuration
    """
    def __init__(self):
        load_dotenv()
        self.__salt = os.getenv("SALT").encode(UTF_8)

    def hash_password(self, password:str):
        """
        Method used to hash password

        Arguments:
            password: str
                Password to encrypt

        Returns:
            password: str
                Encrypted password
        """
        return bcrypt.hashpw(password.encode(UTF_8), self.__salt).decode(UTF_8)

    def check_password(self, password, hashed_password):
        """
        Method used to validate hassed password

        Arguments:
            password: str
                Password to validate
            hashed_password: str
                Hashed password to check

        Returns:
            is_valid: bool
        """
        return bcrypt.checkpw(password.encode(UTF_8), hashed_password.encode(UTF_8))
