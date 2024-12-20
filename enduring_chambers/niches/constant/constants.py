"""
Constants required for enduring-chambers system
"""
import os
import logging
from enum import StrEnum
from decouple import config
from dotenv import load_dotenv
load_dotenv()
##############################################################################################
##                                                                                          ##
## Constants for enduring chambers system                                                   ##
##                                                                                          ##
##############################################################################################
VERSION = "1.0.2"
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

STARTS_LOGGING_CONSTANT = "STARTS"
ENDS_LOGGING_CONSTANT = "ENDS"

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

HASHED_BOOLEAN_CONVERTER_IS_DONATED = {
    "True" : "Si",
    "False": "No"
}

##############################################################################################
##                                                                                          ##
## Console log configuration                                                                ##
##                                                                                          ##
##############################################################################################
CONSOLE_LOG_ENABLED = config("CONSOLE_LOG_ENABLED", default=False, cast=bool)
LOG_FORMAT = ('[ %(asctime)s ][%(levelname)s][%(name)s] ' +
              '::::: %(message)s ::::: [%(module)s :: %(funcName)s]')
LOG_FOLDER = "." + os.getenv("LOG_FOLDER")
LOG_FILENAME = LOG_FOLDER + "enduring-chambers"
LOGGING_LEVEL_ENUM = {
    "INFO" : logging.INFO,
    "DEBUG" : logging.DEBUG,
    "WARNING" : logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAl": logging.CRITICAL
    }

LOGGING_LEVEL = LOGGING_LEVEL_ENUM[os.getenv("LOGGING_LEVEL")]
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

class FieldName(StrEnum):
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
    NICHE = "Nicho"
    QUANTITY = "Cantidad"
    MODULE = "Módulo"

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
