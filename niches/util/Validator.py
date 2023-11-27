"""
Module util used to make validations
"""
from niches.constants.constants import UserField
from niches.constants.constants import THE_FIELD_LABEL
from niches.constants.constants import SHOULD_NOT_BE_EMPTY_LABEL
from niches.constants.constants import PASSWORDS_MUST_BE_EQUAL
from niches.constants.constants import PASSWORD_MINIMAL_CHARACTERS
from niches.constants.constants import PASSWORD_MUST_HAVE_CHARACTERS

def validate_is_not_empty(string:str, name:UserField):
    """
    Validates if a string is not empty
    Args:
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
    Args:
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
