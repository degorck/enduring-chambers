import repackage
repackage.up(2)
from util.DbConnection import *
from model.entity.UserType import UserType
from mapper.UserTypeDaoMapper import UserTypeDaoMapper

class UserTypeDao:
    def __init__(self):
        db_connection.start_connection()
        db_connection.end_connection()

    def find_by_id(self, id:int):
        command = ('''
                   SELECT * 
                   FROM tb_user_type
                   WHERE
                   id = %s
                   ''')
        
        try:
            db_connection.start_connection()
            db_connection.get_cursor().execute(command % id)
            row = db_connection.get_cursor().fetchone()
            db_connection.end_connection()
            user_type = user_type_dao_mapper.real_dict_row_to_user(row)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            user_type = UserType()

        finally:
            if db_connection.get_connection() is not None:
                db_connection.get_connection().close()
        
        return user_type
    
    def find_all(self):
        command = ('''
                   SELECT * 
                   FROM tb_user_type
                   ''')
        
        try:
            db_connection.start_connection()
            db_connection.get_cursor().execute(command)
            list_user_type = []
            rows = db_connection.get_cursor().fetchall()
            for row in rows:
                user_type = user_type_dao_mapper.real_dict_row_to_user(row)
                list_user_type.append(user_type)
            db_connection.end_connection()
           
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            list_user_type = []

        finally:
            if db_connection.get_connection() is not None:
                db_connection.get_connection().close()
        
        return list_user_type

if __name__ == "__main__":
    db_connection = DbConnection()
    user_type_dao = UserTypeDao()
    user_type_dao_mapper = UserTypeDaoMapper()