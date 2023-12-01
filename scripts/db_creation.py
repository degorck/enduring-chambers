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
            id_user_type serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            key VARCHAR(10) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_module(
            id_module serial PRIMARY KEY,
            name VARCHAR(10) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_row(
            id_row serial PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            module_id int REFERENCES tb_module(id_module),
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_user (
            id_user serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            paternal_surname VARCHAR(50) NOT NULL,
            maternal_surname VARCHAR(50),
            user_type_id int REFERENCES tb_user_type(id_user_type),
            user_name VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(150) NOT NULL,
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_holder(
            id_holder serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            paternal_surname VARCHAR(50) NOT NULL,
            maternal_surname VARCHAR(50),
            phone VARCHAR(20),
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_niche(
            id_niche serial PRIMARY KEY,
            row_id int REFERENCES tb_row(id_row) NOT NULL,
            number int NOT NULL,
            is_busy BOOLEAN NOT NULL,
            is_paid_off BOOLEAN NOT NULL,
            holder_id int REFERENCES tb_holder(id_holder),
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_payment(
            id_payment serial PRIMARY KEY,
            niche_id int REFERENCES tb_niche(id_niche),
            quantity FLOAT NOT NULL,
            payment_date TIMESTAMP NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_remain_type(
            id_remain_type serial PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            key VARCHAR(10) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_deceased(
        id_deceased serial PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        paternal_surname VARCHAR(50) NOT NULL,
        maternal_surname VARCHAR(50),
        birth_date DATE NOT NULL,
        death_date DATE NOT NULL,
        remain_type_id int REFERENCES tb_remain_type(id_remain_type) NOT NULL,
        niche_id int REFERENCES tb_niche(id_niche) NOT NULL,
        book TEXT,
        sheet TEXT,
        image_route VARCHAR(300),
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

def __insert_user(name,
                  paternal_surname,
                  maternal_surname,
                  user_type_id,
                  user_name,
                  password):
    command = '''
            INSERT INTO tb_user(
                name,
                paternal_surname,
                maternal_surname,
                user_type_id,
                user_name,
                password,
                is_active,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name,
              paternal_surname,
              maternal_surname,
              user_type_id,
              user_name,
              password,
              True,
              datetime.datetime.now(),
              datetime.datetime.now())
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

def __insert_module(name):
    command = '''
            INSERT INTO tb_module(
                name,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s)
        '''
    values = (name,
              datetime.datetime.now(),
              datetime.datetime.now())
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

def __insert_row(name, module_id):
    command = '''
            INSERT INTO tb_row(
                name,
                module_id,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name,
              module_id,
              datetime.datetime.now(),
              datetime.datetime.now())
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

def __insert_admin_user():
    __insert_user("admin",
                  "admin",
                  "admin",
                  1,
                  "admin",
                  "$2b$12$X5XasxumBmNNZK8OpLUoNufmghMYMa8E6ZYpC0VXiScNdnoF0VI4.")

def __insert_modules():
    module_list =[
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M"
    ]
    for module in module_list:
        __insert_module(module)

def __insert_rows():
    row_list = [
        ["1", "A"],
        ["1", "B"],
        ["1", "C"],
        ["2", "A"],
        ["2", "B"],
        ["2", "C"],
        ["3", "A"],
        ["3", "B"],
        ["3", "C"]
        ]

    for row in row_list:
        __insert_row(str(row[1]), int(row[0]))

if __name__ == '__main__':
    __create_tables()
    __insert_user_types()
    __insert_remain_types()
    __insert_admin_user()
    __insert_modules()
    __insert_rows()
