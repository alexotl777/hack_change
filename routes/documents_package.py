import datetime
import io, os, requests
from typing import Annotated
import zipfile
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from pydantic_models.document_package import BidParticipantInfo
from pydantic_models.bid_info import Bid
from pydantic_models.document_package import BidParticipantInfo, City, HasChild, FamilyStatus
from functions.archiver import archivate_documents
from databases.db_endpoints import get_bids_by_status


router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
    responses={404: {"description": "Not found"}},
)
# Предполагаю, что данные формы каким-то образом окажутся в хранилище. В базе данных лежат запрашиваемые условия.
# Где-то в хранилище, на облаке или просто на сервере лежат паспортные данные. Для разработки файлы pdf будут лежать в папке 'тестовые файлы'

@router.get('/deque_bids/{product}/{status}')
async def get_dequeue(product: str, status: str):
    """
    Возвращает JSON с данными по заявкам по определенному статусу и продукту. Данные краткие - Номер сделки, сумма, срок, ставка
    """
    result = await get_bids_by_status(product, status)
    return {
        'bids': result
    }




@router.get('/docs_package')
async def get_docs_package():
    """
    Возвращает архив с документами пользователя
    """
    archivate_documents()

    return FileResponse('Документы пользователей/тестовые файлы.zip', filename='Документы пользователя.zip', media_type='application/zip')


@router.get('/bid_info')
async def get_bid_info(id: int):
    """
    Принимает id сделки, возвращает давнные по ней
    """
    return {'id': Bid}

@router.get('/participant_info/{id}')
async def get_participant_info(id: int):
    """
    Принимает на вход id участника и возвращает информацию о нем
    """
    return {
        'id': BidParticipantInfo
    }