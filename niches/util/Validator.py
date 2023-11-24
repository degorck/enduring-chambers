from niches.util.Constants import *

class Validator():
    def __init__(self):
        pass

    def validate_is_not_empty(self, string:str, name:UserField):
        if len(string) != 0:
            pass
        else:
            raise ValueError(THE_FIELD_LABEL + name + SHOULD_NOT_BE_EMPTY_LABEL)
        
    def validate_password(self, password, repeated_password):
        if password == repeated_password:
            pass
        else:
            raise ValueError(PASSWORDS_MUST_BE_EQUAL)
        
        if len(password) >= PASSWORD_MINIMAL_CHARACTERS:
            pass
        else:
            raise ValueError(PASSWORD_MUST_HAVE_CHARACTERS)