"""
Payment Service Module for Enduring Chambers
"""
import logging
from niches.model.dto.payment_dto import PaymentDto
from niches.model.dao.payment_dao import PaymentDao
from niches.model.mapper.payment_mapper import payment_dto_to_payment, payment_to_payment_dto
from niches.controller.error_controller import ErrorController

class PaymentService:
    """
    Class with the functionality of PaymentService
    """
    def __init__(self):
        self.__error_controller = ErrorController()
        self.__payment_dao = PaymentDao()

    def create_payment(self, payment_dto:PaymentDto):
        """
        Saves the payment on database.

        Arguments:
            payment_dto: PaymentDto
                Data transfer object of the payment to be saved
        Returns:
            payment_dto: PaymentDto
                Payment created
        """
        try:
            output = payment_to_payment_dto(
                self.__payment_dao.create_payment(payment_dto_to_payment(payment_dto)))

            logging.debug("Pago creado")
            return output

        except ValueError as ve:
            self.__error_controller.handle_value_error(ve)
            self.__error_controller.show()
            return None

        except Exception as e:
            self.__error_controller.handle_exception_error(e)
            self.__error_controller.show()
            return None

    def search_all_payments_by_niche_id(self, niche_id:int):
        """
        Search payments by niche_id on database.

        Arguments:
            niche_id: int
                module_id to filter the list
        Returns:
            list_payment_dto : list<PaymentDto> 
                Payment list found
        """
        list_payment_dto = []
        list_payment = []
        list_payment = self.__payment_dao.search_all_payments_by_niche_id(niche_id)
        for payment in list_payment:
            payment_dto = PaymentDto()
            payment_dto = payment_to_payment_dto(payment)
            list_payment_dto.append(payment_dto)
        return list_payment_dto

    def find_by_id(self, payment_id:int):
        """
        Find payment by its id

        Arguments:
            payment_id : int
                id of the Payment
        Returns:
            payment_dto : PaymentDto
                Found PaymentDto.
        """
        payment_dto = PaymentDto()
        payment_dto = payment_to_payment_dto(
            self.__payment_dao.find_by_id(payment_id))
        logging.debug("Se encontró el pago por su id")
        return payment_dto

    def modify_payment(self, payment_dto:PaymentDto):
        """
        Modify payment

        Arguments:
            payment_dto: PaymentDto
                PaymentDto to be modified
        """
        self.__payment_dao.modify_payment(payment_dto_to_payment(payment_dto))
