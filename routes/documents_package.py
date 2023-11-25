import datetime
import io, os, requests
from typing import Annotated
import zipfile
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse

from pydantic_models.document_package import BidParticipantInfo, City, HasChild, FamilyStatus
from functions.archiver import archivate_documents

from databases.db_settings import engine, async_session_factory
from sqlalchemy.orm import Session
from pydantic_models.document_package import BidParticipantInfo

def get_db():
    db = async_session_factory()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
    responses={404: {"description": "Not found"}},
)
# Предполагаю, что данные формы каким-то образом окажутся в хранилище. В базе данных лежат запрашиваемые условия.
# Где-то в хранилище, на облаке или просто на сервере лежат паспортные данные. Для разработки файлы pdf будут лежать в папке 'тестовые файлы'



@router.get('/docs_package')
async def get_docs_package():
    """
    Рассматривать продукт будем один. Далее буду использовать продукт "Ипотечный кредит" - mortgage
    Возвращает список заявок из очереди для продукта c необходимым статусом
    (1. Новая - new
    2. В работе - at_work
    3. Дозапрос информации - requery
    4. На доработке - to_review
    )
    """
    archivate_documents()

    return FileResponse('Документы пользователей/тестовые файлы.zip', filename='Документы пользователя.zip', media_type='application/zip')


@router.get('/bid_info')
async def get_bid_info(
        id: int = Query(None, description="ID"),
        # status: str = Query(None, description="Начальный вес рулона"),
        # first_name: str = Query(None, description="Имя"),
        # last_name: str = Query(None, description="Фамилия"),
        # middle_name: str = Query(None, description="Отчество"),
        # date_of_birth: datetime.date = Query(None, description="Дата рождения"),
        # registration_place: City = Query(None, description="Адрес регистрации"),
        # living_place: City = Query(None, description="Адрес проживания"),
        # family_status: FamilyStatus = Query(None, description="Семейное положение"),
        # has_child: HasChild = Query(None, description="Наличие детей"),
        # work_place: str = Query(None, description="Место работы"),
        # work_position: str = Query(None, description="Должность"),
        # official_work_monthly_income: float = Query(None, description="Доход официальный"),
        # add_income_proof: bool = Query(None, description="Доп. доход подтвержден"),
        # monthly_add_income: float = Query(None, description="Доход дополнительный"),
):
    application = db_dependency.query(BidParticipantInfo).filter(BidParticipantInfo.id == id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Item not found")
    print(application)
    if not(application.status and application.first_name and application.last_name and application.middle_name and application.date_of_birth and
           application.registration_place and application.living_place and application.family_status and application.has_child != None and
           application.work_place and application.work_position and application.official_work_monthly_income and
           application.work_experience_year and application.work_experience_month and application.add_income_proof != None and 
           application.monthly_add_income):
        application.status = status = "Дозапрос информации"
        return {'status': status}
    else:
        status = "В работе"
    return {'id': id}