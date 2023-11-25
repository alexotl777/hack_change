import io, os, requests
import zipfile
from fastapi import APIRouter
from fastapi.responses import FileResponse

from hack_change.pydantic_models.document_package import BidParticipantInfo
from hack_change.functions.archiver import archivate_documents

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

async def get_bid_info():
    pass