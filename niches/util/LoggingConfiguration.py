import logging
from niches.util.Constants import LOG_FILENAME, LOGING_LEVEL, UTF_8, LOG_FORMAT, CONSOLE_LOG_ENABLED

logging.basicConfig(filename = LOG_FILENAME,
                    encoding = UTF_8,
                    level = LOGING_LEVEL,
                    format = LOG_FORMAT)
if CONSOLE_LOG_ENABLED:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt=LOG_FORMAT)
    handler.setFormatter(formatter)
    logging.getLogger().addHandler(handler)

def get_loging():
    return logging