"""
Delete old log files util
"""
import os
import logging
import time
from dotenv import load_dotenv
load_dotenv()

LOG_FOLDER = "." + os.getenv("LOG_FOLDER")
DAY_LIMIT = int(os.getenv("DAY_LIMIT"))
DAY_SECONDS = 86400

def delete_old_logs():
    """
    Deletes old log files, day limit configured on .env file
    """
    os.chdir(os.path.join(os.getcwd(), LOG_FOLDER))

    file_list = os.listdir()
    current_time = time.time()
    logging.debug("files in log folder %s", file_list)

    for file in file_list:
        file_location = os.path.join(os.getcwd(), file)
        file_time = os.stat(file_location).st_mtime

        if (file_time < current_time - DAY_SECONDS*DAY_LIMIT) and (not file == "log.md"):
            logging.info(" Deleted file \"%s\", has more than %s days old", file, DAY_LIMIT)
            os.remove(file_location)
