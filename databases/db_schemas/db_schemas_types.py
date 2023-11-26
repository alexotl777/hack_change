from datetime import datetime
from typing import Annotated
from enum import Enum
from sqlalchemy import func
from sqlalchemy.orm import mapped_column



pkint = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
false_bool = Annotated[bool, mapped_column(default=False)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=func.now())]

# Сделка
class BidStatus(Enum):
    new = 'Новая'
    at_work = 'В работе'
    requery = 'Дозапрос информации'
    to_review = 'На доработке'

class Product(Enum):
    mortgage = 'Ипотечный кредит'
    avtocredit = 'Автокредит'


# Участник сделки

class Role(Enum):
    borrower = 'Заемщик'
    co_borrower = 'Созаещик'
    guarantor = 'Поручитель'

class FamilyStatus(Enum):
    single = 'Холост'
    married = 'Женат/Замужем'
    devorced = 'В разводе'