from datetime import datetime, timedelta
from typing import Annotated
import enum, re, sys
from fastapi import UploadFile, Form, APIRouter
from pydantic import BaseModel, Field, validator

from functions.archiver import is_file_in_archive

class City(enum.Enum):
    moscow = 'Москва'
    spb = 'Санкт-Петербург'

class FamilyStatus(enum.Enum):
    single = 'Холост'
    married = 'Женат/Замужем'
    devorced = 'В разводе'

class HasChild(enum.Enum):
    yes = 'Да'
    no = 'Нет'


class BidParticipantInfo(BaseModel):
    id: int
    status: str
    first_name: str
    last_name: str
    middle_name: str
    date_of_birth: datetime
    passport: str = Field(max_length=11, min_length=11, pattern=r"^(\d{4}) (\d{6})$")
    registration_place: City
    living_place: City
    family_status: FamilyStatus
    has_child: HasChild
    work_place: str
    work_position: str
    work_experience_year: int
    work_experience_month: int
    official_work_monthly_income: float
    official_income_proof: bool
    monthly_add_income: float
    add_income_proof: bool

    @validator('date_of_birth')
    @classmethod
    def validate_age(cls, value):
        age = (datetime.now() - value).days / 365
        if age < 18:
            raise ValueError("Возраст должен быть больше 18 лет")
        elif age > 130:
            raise ValueError("Возраст должен быть меньше 130 лет")
        return value

    @validator("passport")
    @classmethod
    def validate_passport(cls, value):
        if not bool(re.fullmatch(r"^(\d{4}) (\d{6})$", value)):
            raise ValueError("Неправильный формат паспорта")
        return value

    @validator("official_income_proof")
    @classmethod
    def validate_income_proof(cls, value=True):
        if not is_file_in_archive():
            value = False
        return value
