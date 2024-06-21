"""
Script to create niches database
"""
import os
import datetime
import psycopg2
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv()

db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST")
db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_port = os.getenv("DB_PORT")
initial_admin_hashed_password = os.getenv("INITIAL_ADMIN_HASHED_PASSWORD")

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
        CREATE TABLE IF NOT EXISTS tb_module(
            id serial PRIMARY KEY,
            name VARCHAR(10) NOT NULL UNIQUE,
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_row(
            id serial PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            module_id int REFERENCES tb_module(id),
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
            paternal_surname VARCHAR(50),
            maternal_surname VARCHAR(50),
            phone VARCHAR(20),
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_niche(
            id serial PRIMARY KEY,
            name VARCHAR(10) NOT NULL,
            is_busy BOOLEAN NOT NULL,
            is_paid_off BOOLEAN NOT NULL,
            is_donated BOOLEAN NOT NULL,
            holder_id int REFERENCES tb_holder(id),
            row_id int REFERENCES tb_row(id) NOT NULL,
            is_active BOOLEAN NOT NULL,
            created_at TIMESTAMP NOT NULL,
            updated_at TIMESTAMP NOT NULL)
        ''',
        '''
        CREATE TABLE IF NOT EXISTS tb_payment(
            id serial PRIMARY KEY,
            niche_id int REFERENCES tb_niche(id),
            quantity FLOAT NOT NULL,
            payment_date TIMESTAMP NOT NULL,
            comments TEXT,
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
        paternal_surname VARCHAR(50),
        maternal_surname VARCHAR(50),
        birth_date DATE,
        death_date DATE,
        remain_type_id int REFERENCES tb_remain_type(id) NOT NULL,
        niche_id int REFERENCES tb_niche(id) NOT NULL,
        book TEXT,
        sheet TEXT,
        image_route VARCHAR(300),
        is_active BOOLEAN NOT NULL,
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
                is_active,
                created_at,
                updated_at) 
            VALUES(
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name,
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

def __insert_holder(name, paternal_surname, maternal_surname, phone, is_active):
    command = '''
            INSERT INTO tb_holder(
                name,
                paternal_surname,
                maternal_surname,
                phone,
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
                %s)
        '''
    values = (name,
              paternal_surname,
              maternal_surname,
              phone,
              is_active,
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

def __insert_niche(name, is_busy, is_paid_off, is_donated, row_id, holder_id, is_active):
    command = '''
            INSERT INTO tb_niche(
                name,
                is_busy,
                is_paid_off,
                is_donated,
                row_id,
                holder_id,
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
              is_busy,
              is_paid_off,
              is_donated,
              row_id,
              holder_id,
              is_active,
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

def __insert_deceased(name, paternal_surname, maternal_surname, birth_date,
                      death_date, remain_type_id, niche_id, book, sheet,
                      is_active):
    command = '''
            INSERT INTO tb_deceased(
                name,
                paternal_surname,
                maternal_surname,
                birth_date,
                death_date,
                remain_type_id,
                niche_id,
                book,
                sheet,
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
                %s,
                %s,
                %s,
                %s)
        '''
    values = (name,
              paternal_surname,
              maternal_surname,
              birth_date,
              death_date,
              remain_type_id,
              niche_id,
              book,
              sheet,
              is_active,
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
    __insert_remain_type("desconocido", "dsc")

def __insert_admin_user():
    __insert_user("admin",
                  "admin",
                  "admin",
                  1,
                  "admin",
                  initial_admin_hashed_password)

def __insert_modules():
    excel_modules = pd.read_excel("enduring_chambers\scripts\enduring_chambers.xlsx",
                                  sheet_name="modules")
    for index, row in excel_modules.iterrows():
        __insert_module(row["nombre"])

def __insert_rows():
    excel_rows = pd.read_excel("enduring_chambers\scripts\enduring_chambers.xlsx",
                               sheet_name="filas")
    for index, row in excel_rows.iterrows():
        __insert_row(row["nombre"], int(row["id_module"]))

def __insert_holders():
    print("################################### Holders ####################################")
    excel_holders = pd.read_excel("enduring_chambers\scripts\enduring_chambers.xlsx",
                                  sheet_name="titulares", dtype=str)
    for index, row in excel_holders.iterrows():
        name:str = row["nombre"]
        if row["apellido_paterno"] is np.nan:
            paternal_surname:str = None
        else:
            paternal_surname:str = row["apellido_paterno"]
        if row["apellido_materno"] is np.nan:
            maternal_surname:str = None
        else:
            maternal_surname:str = row["apellido_materno"]
        if row["teléfono"] is np.nan:
            phone:str = None
        else:
            phone:str = row["teléfono"]
        if row["activo"] == "S":
            is_active:bool = True
        else:
            is_active:bool = False
        #print(name, paternal_surname, maternal_surname, phone, is_active)
        __insert_holder(name,
                        paternal_surname,
                        maternal_surname,
                        phone,
                        is_active)
    print("################################### Holders ####################################")

def __insert_niches():
    print("################################### Niches ####################################")
    excel_niches = pd.read_excel("enduring_chambers\scripts\enduring_chambers.xlsx",
                                  sheet_name="nichos", dtype=str)
    for index, row in excel_niches.iterrows():
        name:str = row["número"]
        if row["pagado"] == "S":
            is_paid:bool = True
        else:
            is_paid:bool = False
        if row["ocupado"] == "S":
            is_busy:bool = True
        else:
            is_busy:bool = False
        if row["donado"] == "S":
            is_donated:bool = True
        else:
            is_donated:bool = False
        if row["id_titular"] is np.nan:
            id_holder:int = None
        else:
            id_holder:int = row["id_titular"]
        if row["id_fila" ] is np.nan:
            id_row:int = None
        else:
            id_row:int = row["id_fila"]
        if row["activo"] == "S":
            is_active:bool = True
        else:
            is_active:bool = False
        #print(name, is_busy, is_paid, is_donated, id_row, id_holder, is_active)
        __insert_niche(name, is_busy, is_paid, is_donated, id_row, id_holder, is_active)
    print("################################### Niches ####################################")

def __insert_deceaseds():
    print("################################### Deceaseds ####################################")
    excel_deceased = pd.read_excel("enduring_chambers\scripts\enduring_chambers.xlsx",
                                   sheet_name="difuntos", dtype=str)
    for index, row in excel_deceased.iterrows():
        name:str = row["nombre"]
        if row["apellido_paterno"] is np.nan:
            paternal_surname:str = None
        else:
            paternal_surname:str = row["apellido_paterno"]
        if row["apellido_materno"] is np.nan:
            maternal_surname:str = None
        else:
            maternal_surname:str = row["apellido_materno"]
        if row["fecha_nacimiento"] is np.nan:
            birth_date:datetime = None
        else:
            birth_date:datetime = row["fecha_nacimiento"]
        if row["fecha_defunción"] is np.nan:
            death_date:datetime = None
        else:
            death_date:datetime = row["fecha_defunción"]
        if row["tipo_restos"] == "cenizas":
            remain_type:int = "1"
        if row["tipo_restos"] == "restos":
            remain_type:int = "2"
        if row["tipo_restos"] == "desconocido":
            remain_type:int = "3"
        id_nicho:int = row["id_nicho"]
        if row["libro"] is np.nan:
            book:str = None
        else:
            book:str = row["libro"]
        if row["foja"] is np.nan:
            sheet:str = None
        else:
            sheet:str = row["foja"]
        if row["activo"] == "S":
            is_active:bool = True
        else:
            is_active:bool = False
        #print(name, paternal_surname, maternal_surname, birth_date, death_date,
              ##remain_type, id_nicho, book, sheet, is_active)
        __insert_deceased(name, paternal_surname, maternal_surname, birth_date,
                          death_date, remain_type, id_nicho, book, sheet, is_active)
    print("#################################################################################################")

if __name__ == '__main__':
    __create_tables()
    __insert_user_types()
    __insert_remain_types()
    __insert_admin_user()
    __insert_modules()
    __insert_rows()
    __insert_holders()
    __insert_niches()
    __insert_deceaseds()
