"""
Database connection configuration
"""
import os
import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import RealDictCursor

class DatabaseConnection:
    """
    Class with Database connection configuration
    """
    def __init__(self):
        load_dotenv()
        self.__db_name = os.getenv("DB_NAME")
        self.__db_host = os.getenv("DB_HOST")
        self.__db_password = os.getenv("DB_PASSWORD")
        self.__db_user = os.getenv("DB_USER")
        self.__db_port = os.getenv("DB_PORT")

    def start_connection(self):
        """
        Starts database connection
        """
        self.__connection = psycopg2.connect(database = self.__db_name,
                                             host = self.__db_host,
                                             user = self.__db_user,
                                             password = self.__db_password,
                                             port = self.__db_port)
        self.__cursor = self.__connection.cursor(cursor_factory=RealDictCursor)

    def end_connection(self):
        """
        Ends database connection
        """
        self.__cursor.close()
        self.__connection.commit()

    def get_cursor(self):
        """
        Get cursor for database connection
        """
        return self.__cursor

    def get_connection(self):
        """
        Gets database connection
        """
        return self.__connection
