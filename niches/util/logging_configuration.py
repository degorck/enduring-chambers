import logging
import datetime
from niches.constants.constants import LOG_FILENAME, LOGING_LEVEL, UTF_8, LOG_FORMAT, CONSOLE_LOG_ENABLED

logging.basicConfig(filename = LOG_FILENAME + "-"+ str(datetime.date.today()) + ".log",
                    encoding = UTF_8,
                    level = LOGING_LEVEL,
                    format = LOG_FORMAT.replace("\n", ""))
if CONSOLE_LOG_ENABLED:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=LOG_FORMAT.replace("\n", ""))
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)

def get_loging():
    return logging