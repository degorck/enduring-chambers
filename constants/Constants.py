from enum import StrEnum
SHOULD_NOT_BE_EMPTY_LABEL = " no debe estar vacío"
THE_FIELD_LABEL = "El campo "
class UserField(StrEnum):
    NAME = "Nombre"
    PATERNAL_SURNAME = "Apellido Paterno"
    MATERNAL_SURNAME = "Apellido Materno"
    USER_TYPE = "Tipo de usuario"
    USER_NAME = "Nombre de usuario"
    PASSWORD = "Contraseña"
