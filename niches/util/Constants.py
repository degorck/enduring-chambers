import logging
from enum import StrEnum
SHOULD_NOT_BE_EMPTY_LABEL = " no debe estar vacío"
THE_FIELD_LABEL = "El campo "
UTF_8 = 'utf-8'
PASSWORDS_MUST_BE_EQUAL = "Las contraseñas deben ser iguales"
PASSWORD_MINIMAL_CHARACTERS = 10
PASSWORD_MUST_HAVE_CHARACTERS = "Las contraseñas deben tener " + str(PASSWORD_MINIMAL_CHARACTERS) + " caracteres."
LOGIN_ERROR = "Error en login. Verifica tu usuario y contraseña"
USER_NOT_EXIST = "El usuario no existe o está inactivo"
'''
Logging configuration:
    INFO - info message
    WARNING - warn message
    ERROR - error message
    CRITICAL - critical message
'''
CONSOLE_LOG_ENABLED = True
LOG_FORMAT = '[ %(asctime)s ][%(levelname)s][%(name)s] ::::: %(message)s ::::: [%(module)s :: %(funcName)s]'
LOG_FILENAME = "enduring-chambers.log"
LOGING_LEVEL = logging.INFO

class UserField(StrEnum):
    NAME = "Nombre"
    PATERNAL_SURNAME = "Apellido Paterno"
    MATERNAL_SURNAME = "Apellido Materno"
    USER_TYPE = "Tipo de usuario"
    USER_NAME = "Nombre de usuario"
    PASSWORD = "Contraseña"

class UserTypeKey(StrEnum):
    ADMINISTRATOR = "dmn"
    CAPTURIST = "cpt"
    GUEST = "gst"
    NOT_LOGGED = "ntl"
