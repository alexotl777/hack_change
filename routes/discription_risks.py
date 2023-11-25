from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import FileResponse

from pydantic_models.document_package import BidParticipantInfo, City, HasChild, FamilyStatus

from databases.db_settings import engine, async_session_factory
from sqlalchemy.orm import Session
from pydantic_models.document_package import BidParticipantInfo

from scripts.pdn import calculate_pdn
from scripts.level_risk import check_risk
from scripts.risks_of_trade import enforcement_proceedings, bankruptcy, mvd

def get_db():
    db = async_session_factory()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

router = APIRouter(
    prefix="/risks",
    tags=["Documents"],
    responses={404: {"description": "Not found"}},
)

# 3 - 5 пункты
@router.get('/risk_assessment')
async def get_bid_info(
        id: int = Query(None, description="ID")):
    
    application = db_dependency.query(BidParticipantInfo).filter(BidParticipantInfo.id == id).first()
    risk, pdn = calculate_pdn(application.official_work_monthly_income)
    has_bill = True
    level = check_risk(application, pdn, has_bill)
    enforcement_proceedings_info = enforcement_proceedings(application)
    check_bankruptcy = bankruptcy(application)
    mvd_info = mvd(application)

    return {'id': id,
            'pdn': pdn,
            'level': level,
            'enforcement_proceedings': enforcement_proceedings_info,
            'bankruptcy': check_bankruptcy,
            'mvd_info': mvd_info}

#Нужен ли пост запрос для андеррайтера, так как он вручную инфу еще заполняет на 4ом пункте