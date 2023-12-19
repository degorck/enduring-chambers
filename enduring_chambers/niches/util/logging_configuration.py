"""
Module configuration for logging
"""
import logging
import datetime
from niches.constant.constants import LOG_FILENAME, LOGGING_LEVEL, LOG_FOLDER
from niches.constant.constants import UTF_8, LOG_FORMAT, CONSOLE_LOG_ENABLED
from niches.util.folder_creation_util import create_folder

create_folder(LOG_FOLDER)

logging.basicConfig(filename = LOG_FILENAME + "-"+ str(datetime.date.today()) + ".log",
                    encoding = UTF_8,
                    level = LOGGING_LEVEL,
                    format = LOG_FORMAT.replace("\n", ""))
if CONSOLE_LOG_ENABLED:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=LOG_FORMAT.replace("\n", ""))
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)

def get_loging():
    """
    Returns:
        configured logging
    """
    return logging
