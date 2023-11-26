from datetime import datetime
from typing import Annotated
from enum import Enum
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from databases.db_settings import Base
from db_schemas_types import *


class BidORM(Base):
    __tablename__ = 'bids'

    id: Mapped[int]
    status: Mapped[BidStatus]
    created_at: Mapped[created_at]
    status_updated_at: Mapped[updated_at]
    product: Mapped[Product]
    max_summ: Mapped[float]
    requested_summ: Mapped[float]
    max_term_in_months: Mapped[int]
    requested_term_in_months: Mapped[int]
    product_rate: Mapped[float] # ставка по продукту в процентах
    requested_rate: Mapped[float] # запрашиваемая ставка в процентах
    monthly_payment: Mapped[float]
    other_info: Mapped[str | None] = mapped_column(nullable=True)

    participants: Mapped[list["BidParticipantORM"]] = relationship("BidParticipantORM", backref="bid")


