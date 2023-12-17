"""
DeceasedMapper Module
"""
from niches.model.dto.payment_dto import PaymentDto
from niches.model.entity.payment import Payment
from niches.model.mapper.niche_mapper import niche_dto_to_niche, niche_to_niche_dto
from niches.model.mapper.remain_type_mapper import remain_type_dto_to_remain_type
from niches.model.mapper.remain_type_mapper import remain_type_to_remain_type_dto

def payment_to_payment_dto(payment:Payment):
    """
    Maps PaymentDto from a Payment

    Arguments:
        payment : Payment
            Payment to be mapped
    Returns:
        payment_dto : PaymentDto
            PaymentDto mapped from Payment 
    """
    if payment is None:
        return None

    payment_dto = PaymentDto()
    payment_dto.existing_payment(
        payment.get_id(),
        niche_to_niche_dto(payment.get_niche()) if (
            payment.get_niche() is not None) else None,
        payment.get_quantity(),
        payment.get_payment_date() if (payment.get_payment_date() is not None) else None,
        payment.get_comments(),
        payment.get_created_at() if (payment.get_created_at() is not None) else None,
        payment.get_updated_at() if (payment.get_updated_at() is not None) else None
    )

    return payment_dto

def payment_dto_to_payment(payment_dto:PaymentDto):
    """
    Maps Payment from a PaymentDto

    Arguments:
        payment_dto: PaymentDto
            PaymentDto to be mapped
    Returns:
        payment : Payment
            Payment mapped from PaymentDto 
    """
    if payment_dto is None:
        return None
    payment = Payment()
    payment.existing_payment(
        payment_dto.get_id(),
        niche_dto_to_niche(payment_dto.get_niche()) if (
            payment_dto.get_niche() is not None) else None,
        payment_dto.get_quantity(),
        payment_dto.get_payment_date() if (payment_dto.get_payment_date() is not None) else None,
        payment_dto.get_comments(),
        payment_dto.get_created_at() if (payment_dto.get_created_at() is not None) else None,
        payment_dto.get_updated_at() if (payment_dto.get_updated_at() is not None) else None
    )

    return payment
