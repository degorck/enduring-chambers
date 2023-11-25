import psycopg2
from dotenv import load_dotenv
import os
from psycopg2.extras import RealDictCursor
import logging

class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.__db_name = os.getenv("DB_NAME")
        self.__db_host = os.getenv("DB_HOST")
        self.__db_password = os.getenv("DB_PASSWORD")
        self.__db_user = os.getenv("DB_USER")
        self.__db_port = os.getenv("DB_PORT")
    
    def start_connection(self):
        self.__connection = psycopg2.connect(database = self.__db_name,
                                             host = self.__db_host,
                                             user = self.__db_user,
                                             password = self.__db_password,
                                             port = self.__db_port)
        self.__cursor = self.__connection.cursor(cursor_factory=RealDictCursor)
        logging.debug("Database connection started")

    def end_connection(self):
        self.__cursor.close()
        self.__connection.commit()
        logging.debug("Database connection finished")

    def get_cursor(self):
        return self.__cursor
    
    def get_connection(self):
        return self.__connection