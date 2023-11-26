from datetime import datetime
from pydantic import BaseModel
from enum import Enum

class BidStatus(Enum):
    new = 'Новая'
    at_work = 'В работе'
    requery = 'Дозапрос информации'
    to_review = 'На доработке'

class Product(Enum):
    mortgage = 'Ипотечный кредит'
    avtocredit = 'Автокредит'



class Bid(BaseModel):

    id: int
    status: BidStatus
    created_at: datetime
    status_updated_at: datetime
    product: Product
    max_summ: float
    requested_summ: float
    max_term_in_months: int
    requested_term_in_months: int
    product_rate: float # ставка по продукту в процентах
    requested_rate: float # запрашиваемая ставка в процентах
    monthly_payment: float
    other_info: str | None