"""
Constants required for enduring-chambers system
"""
import logging
from enum import StrEnum
##############################################################################################
##                                                                                          ##
## Constants for enduring chambers system                                                   ##
##                                                                                          ##
##############################################################################################
SHOULD_NOT_BE_EMPTY_LABEL = " no debe estar vacío"
THE_FIELD_LABEL = "El campo "
UTF_8 = 'utf-8'
PASSWORDS_MUST_BE_EQUAL = "Las contraseñas deben ser iguales"
PASSWORD_MINIMAL_CHARACTERS = 10
PASSWORD_MUST_HAVE_CHARACTERS = ("Las contraseñas deben tener " +
                                 str(PASSWORD_MINIMAL_CHARACTERS) + " caracteres.")
LOGIN_ERROR = "Error en login. Verifica tu usuario y contraseña"
USER_NOT_EXIST = "El usuario no existe o está inactivo"
NOT_VALID_IMAGE = "El archivo no es una imagen. \n Utiliza archivos *.png, *.jpg o *.jpeg"

HASHED_BOOLEAN_CONVERTER_IS_ACTIVE = {
    "True" : "Activo",
    "False": "Inactivo"
}

HASHED_BOOLEAN_CONVERTER_IS_BUSY = {
    "True" : "Ocupado",
    "False": "Desocupado"
}

HASHED_BOOLEAN_CONVERTER_IS_PAID_OFF = {
    "True" : "Pagado",
    "False": "Sin liquidar"
}

##############################################################################################
##                                                                                          ##
## Console log configuration                                                                ##
##                                                                                          ##
##############################################################################################
CONSOLE_LOG_ENABLED = True
LOG_FORMAT = ('[ %(asctime)s ][%(levelname)s][%(name)s] ' +
              '::::: %(message)s ::::: [%(module)s :: %(funcName)s]')
LOG_ROUTE = "./log/"
LOG_FILENAME = LOG_ROUTE + "enduring-chambers"
LOGING_LEVEL = logging.DEBUG
'''
Logging levels:
    - INFO - info message
    - DEBUG - debug message
    - WARNING - warn message
    - ERROR - error message
    - CRITICAL - critical message
'''

##############################################################################################
##                                                                                          ##
## Enums for enduring chambers system                                                       ##
##                                                                                          ##
##############################################################################################

class UserField(StrEnum):
    """
    Enum that includes the field names of an user
    """
    NAME = "Nombre"
    PATERNAL_SURNAME = "Apellido Paterno"
    MATERNAL_SURNAME = "Apellido Materno"
    USER_TYPE = "Tipo de usuario"
    USER_NAME = "Nombre de usuario"
    PASSWORD = "Contraseña"
    PHONE = "Teléfono"

class UserTypeKey(StrEnum):
    """
    Enum that includes the type of user of the system
    """
    ADMINISTRATOR = "dmn"
    CAPTURIST = "cpt"
    GUEST = "gst"
    NOT_LOGGED = "ntl"

class ValidImageExtension(StrEnum):
    """
    Enum that includes valid image extensions
    """
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"
