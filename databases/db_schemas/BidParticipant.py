from datetime import datetime
from typing import Annotated
from enum import Enum
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db_settings import Base
from db_schemas_types import *

class BidParticipantORM(Base):
    __tablename__ = 'bid_participants'

    id: Mapped[int]
    bid_id: Mapped[pkint] = mapped_column(ForeignKey('bids.id', ondelete='CASCADE'))
    role_in_bid: Mapped[Role]
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str]
    date_of_birth: Mapped[datetime.date]
    passport: Mapped[str] = mapped_column(unique=True)
    registration_place: Mapped[str]
    living_place: Mapped[str]
    family_status: Mapped[FamilyStatus]
    has_child: Mapped[false_bool]
    work_place: Mapped[str]
    work_position: Mapped[str]
    work_experience_year: Mapped[int]
    work_experience_month: Mapped[int]
    official_work_monthly_income: Mapped[float]
    official_income_proof: Mapped[false_bool]
    monthly_add_income: Mapped[float]
    add_income_proof: Mapped[false_bool]

    bids: Mapped[list["BidORM"]] = relationship("BidORM", backref="bid_participants")

