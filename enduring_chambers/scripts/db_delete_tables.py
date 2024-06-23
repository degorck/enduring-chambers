"""
Script to delete niches tables
"""
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_port = os.getenv("DB_PORT")
initial_admin_hashed_password = os.getenv("INITIAL_ADMIN_HASHED_PASSWORD")

def __delete_tables():
    command = '''
            DROP TABLE tb_deceased CASCADE;
            DROP TABLE tb_niche CASCADE;
            DROP TABLE tb_holder CASCADE;
            DROP TABLE tb_module CASCADE;
            DROP TABLE tb_user_type CASCADE;
            DROP TABLE tb_remain_type CASCADE;
            DROP TABLE tb_row CASCADE;
            DROP TABLE tb_user CASCADE;
            DROP TABLE tb_payment CASCADE;
            '''
    try:
        connection = psycopg2.connect(database = db_name,
                                      host = db_host,
                                      user = db_user,
                                      password = db_password,
                                      port = db_port)
        cursor = connection.cursor()
        cursor.execute(command)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

if __name__ == '__main__':
    __delete_tables()
