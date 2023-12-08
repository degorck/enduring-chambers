"""
Module util used to make validations
"""
import re
from niches.constants.constants import UserField
from niches.constants.constants import THE_FIELD_LABEL
from niches.constants.constants import SHOULD_NOT_BE_EMPTY_LABEL
from niches.constants.constants import PASSWORDS_MUST_BE_EQUAL
from niches.constants.constants import PASSWORD_MINIMAL_CHARACTERS
from niches.constants.constants import PASSWORD_MUST_HAVE_CHARACTERS

def validate_is_not_empty(string:str, name:UserField):
    """
    Validates if a string is not empty
    
    Arguments:
        string: str
            The string to validate
        name : UserField(Enum)
            Name of the field to manage the error
    Raises:
        ValueError:
            Raises ValueError if the field is empty
    """
    if len(string) != 0:
        pass
    else:
        raise ValueError(THE_FIELD_LABEL + name + SHOULD_NOT_BE_EMPTY_LABEL)

def validate_password(password:str, repeated_password:str):
    """
    Validates if the password is right
    
    Arguments:
        password: str
            Password to validate
        repeated_password: str
            Repeated password to validate
    Raises:
        ValueError:
            Raises a ValueError exception if the password and repeated password not match,
            or if not have the length required.
    """
    if password == repeated_password:
        pass
    else:
        raise ValueError(PASSWORDS_MUST_BE_EQUAL)

    if len(password) >= PASSWORD_MINIMAL_CHARACTERS:
        pass
    else:
        raise ValueError(PASSWORD_MUST_HAVE_CHARACTERS)

def validate_phone_number(phone_number):
    """
    Validates if the phone format
    
    Arguments:
        phone_number: str
            Number to validate

    Raises:
        ValueError:
            Raises a ValueError exception if the number does not have the right format
    """
    pattern = re.compile(r'^\d{3}-\d{4}$|^\+\d-\d{3}-\d{3}-\d{4}$|^1-\d{3}-\d{3}-\d{4}$|^\(\+\d{2}\)\s?\d{3}-\d{2}-\d{2}$|^\d{3}-\d{3}-\d{2}-\d{2}$')
    if bool(pattern.match(phone_number)):
        pass
    else:
        raise ValueError("""Formato de teléfono inválido.
Utiliza estos formatos:
México: 477-123-45-67, (+52) 477-123-45-67
US: 456-7890, 212-456-7890, +1-212-456-7890, 1-212-456-7890""")

def validate_not_none(item, name:str):
    """
    Validates if the item is not None
    
    Arguments:
        item:
            Item to validate
        name: str
            name of the item

    Raises:
        ValueError:
            Raises a ValueError exception if the number does not have the right format
    """
    if item is None:
        raise ValueError(name +" no debe estar vacío")
