"""
Script to create niches database
"""
import os
import datetime
import psycopg2
from dotenv import load_dotenv

load_dotenv()
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_port = os.getenv("DB_PORT")

def __create_tables():
    commands = (
        '''
        CREATE TABLE IF NOT EXISTS tb_user_type(
            id serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            key VARCHAR(10) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_user (
            id serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            paternal_surname VARCHAR(50) NOT NULL,
            maternal_surname VARCHAR(50),
            user_type_id int REFERENCES tb_user_type(id),
            user_name VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(150) NOT NULL,
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_holder(
            id serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            paternal_surname VARCHAR(50) NOT NULL,
            maternal_surname VARCHAR(50),
            phone VARCHAR(10),
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_niche(
            id serial PRIMARY KEY,
            module VARCHAR(50) NOT NULL,
            character VARCHAR(50) NOT NULL,
            number int NOT NULL,
            is_busy BOOLEAN NOT NULL,
            holder_id int REFERENCES tb_holder(id),
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_remain_type(
            id serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            key VARCHAR(10) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_deceased(
        id serial PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        paternal_surname VARCHAR(50) NOT NULL,
        maternal_surname VARCHAR(50),
        birth_date DATE NOT NULL,
        death_date DATE NOT NULL,
        remain_type_id int REFERENCES tb_remain_type(id) NOT NULL,
        niche_id int REFERENCES tb_niche(id) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL)
        ''')
    try:
        connection = psycopg2.connect(database = db_name,
                                      host = db_host,
                                      user = db_user,
                                      password = db_password,
                                      port = db_port)
        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

def __insert_user_type(name, key):
    command = '''
            INSERT INTO tb_user_type(
                name,
                key,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name, key, datetime.datetime.now(), datetime.datetime.now())
    try:
        connection = psycopg2.connect(database = db_name,
                                      host = db_host,
                                      user = db_user,
                                      password = db_password,
                                      port = db_port)
        cursor = connection.cursor()
        cursor.execute(command, values)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

def __insert_remain_type(name, key):
    command = '''
            INSERT INTO tb_remain_type(
                name,
                key,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name, key, datetime.datetime.now(), datetime.datetime.now())
    try:
        connection = psycopg2.connect(database = db_name,
                                      host = db_host,
                                      user = db_user,
                                      password = db_password,
                                      port = db_port)
        cursor = connection.cursor()
        cursor.execute(command, values)

        cursor.close()
        connection.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if connection is not None:
            connection.close()

def __insert_user_types():
    __insert_user_type("administrador", "dmn")
    __insert_user_type("capturista", "cpt")

def __insert_remain_types():
    __insert_remain_type("cenizas", "cnz")
    __insert_remain_type("restos", "rst")

if __name__ == '__main__':
    __create_tables()
    __insert_user_types()
    __insert_remain_types()
