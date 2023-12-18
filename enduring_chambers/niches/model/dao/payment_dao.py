"""
PaymentDao Module. Includes all the functions to load and read data
from database. 
"""
import datetime
import logging
import psycopg2
from niches.util.database_connection import DatabaseConnection
from niches.model.entity.payment import Payment
from niches.model.mapper.dao.payment_dao_mapper import real_dict_row_to_payment

class PaymentDao:
    """
    Class with the functionality of PamentDao
    """
    def __init__(self):
        self.__db_connection = DatabaseConnection()

    def create_payment(self, payment:Payment):
        """
        Saves the payment on database

        Arguments:
            payment: Payment
                Payment entity to be created
        Returns:
            Payment : Payment
                Created payment entity 
        """
        command = '''
                INSERT INTO tb_payment(
                    niche_id,
                    quantity,
                    payment_date,
                    comments,
                    created_at,
                    updated_at)
                VALUES (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s)
                '''
        values = (
            payment.get_niche().get_id(),
            payment.get_quantity(),
            payment.get_payment_date(),
            payment.get_comments(),
            datetime.datetime.now(),
            datetime.datetime.now()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.get_cursor().execute('SELECT LASTVAL()')
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            logging.debug("Se creó el pago")
            return self.find_by_id(int(row["lastval"]))
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def find_by_id(self, payment_id:int):
        """
        Find payment by its payment_id
        
        Arguments:
            payment_id: int
                payment_id of the deceased to find
        Returns:
            payment: Payment
                Payment found
        """
        command = '''
                SELECT tb_payment.id,
                tb_payment.quantity,
                tb_payment.payment_date,
                tb_payment.comments,
                tb_payment.created_at,
                tb_payment.updated_at,
                tb_niche.id as niche_id,
                tb_niche.number as niche_number,
                tb_niche.is_busy as niche_is_busy,
                tb_niche.is_paid_off as niche_is_paid_off,
                tb_niche.is_active as niche_is_active,
                tb_niche.created_at as niche_created_at,
                tb_niche.updated_at as niche_updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname as holder_paternal_surname,
                tb_holder.maternal_surname as holder_maternal_surname,
                tb_holder.phone as holder_phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_payment
                INNER JOIN tb_niche ON tb_payment.niche_id = tb_niche.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE tb_payment.id = %s
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % payment_id)
            row = self.__db_connection.get_cursor().fetchone()
            self.__db_connection.end_connection()
            payment:Payment = real_dict_row_to_payment(row)
            logging.debug("Se buscó el pago por su id")
            return payment

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def search_all_payments_by_niche_id(self, niche_id:int):
        """
        Search all payments by niche_id
        
        Arguments:
            niche_id: int
                niche_id to match with the payment search
        Returns:
            payment_list = list<Payment>
        """

        payment_list = []
        command = '''
                SELECT tb_payment.id,
                tb_payment.quantity,
                tb_payment.payment_date,
                tb_payment.comments,
                tb_payment.created_at,
                tb_payment.updated_at,
                tb_niche.id as niche_id,
                tb_niche.number as niche_number,
                tb_niche.is_busy as niche_is_busy,
                tb_niche.is_paid_off as niche_is_paid_off,
                tb_niche.is_active as niche_is_active,
                tb_niche.created_at as niche_created_at,
                tb_niche.updated_at as niche_updated_at,
                tb_module.id as module_id,
                tb_module.name as module_name,
                tb_module.is_active as module_is_active,
                tb_module.created_at as module_created_at,
                tb_module.updated_at as module_updated_at,
                tb_row.id as row_id,
                tb_row.name as row_name,
                tb_row.created_at as row_created_at,
                tb_row.updated_at as row_updated_at,
                tb_holder.id as holder_id,
                tb_holder.name as holder_name,
                tb_holder.paternal_surname as holder_paternal_surname,
                tb_holder.maternal_surname as holder_maternal_surname,
                tb_holder.phone as holder_phone,
                tb_holder.is_active as holder_is_active,
                tb_holder.created_at as holder_created_at,
                tb_holder.updated_at as holder_updated_at
                FROM tb_payment
                INNER JOIN tb_niche ON tb_payment.niche_id = tb_niche.id
                INNER JOIN tb_row ON tb_niche.row_id = tb_row.id
                FULL OUTER JOIN tb_holder ON tb_niche.holder_id = tb_holder.id
                INNER JOIN tb_module ON tb_row.module_id = tb_module.id
                WHERE
                tb_payment.niche_id = %s
                ORDER BY id
                '''

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command % niche_id)
            rows = self.__db_connection.get_cursor().fetchall()
            for row in rows:
                payment = real_dict_row_to_payment(row)
                payment_list.append(payment)
            self.__db_connection.end_connection()
            logging.debug("Se buscaron todos los pagos por su nicho")
            return payment_list

        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()

    def modify_payment(self, payment:Payment):
        """
        Modifies the payment on database
        
        Arguments:
            payment: Payment
                Payment entity to be modified
        """
        command = '''
                UPDATE tb_payment
                SET
                niche_id = %s,
                quantity = %s,
                payment_date = %s,
                comments = %s,
                updated_at = %s
                WHERE id = %s
                '''
        values = (
            payment.get_niche().get_id(),
            payment.get_quantity(),
            payment.get_payment_date(),
            payment.get_comments(),
            datetime.datetime.now(),
            payment.get_id()
            )

        try:
            self.__db_connection.start_connection()
            self.__db_connection.get_cursor().execute(command, values)
            self.__db_connection.end_connection()
            logging.debug("Se modificó el pago")
        except (Exception, psycopg2.DatabaseError) as error:
            logging.exception(error)
            raise error

        finally:
            if self.__db_connection.get_connection() is not None:
                self.__db_connection.get_connection().close()
