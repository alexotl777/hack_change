from sqlalchemy import select
from sqlalchemy.orm import selectinload

from db_settings import async_session_factory
from db_schemas.Bid import BidORM

async def get_bids_by_status(product: str, status: str):
    async with async_session_factory() as session:
        query = select(BidORM).options(
            selectinload(BidORM.participants)
        ).where(BidORM.status == status, BidORM.product == product)
        result = await session.execute(query)
        return result.scalars().all()