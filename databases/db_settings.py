from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from config import settings

class Base(DeclarativeBase):
    metadata = MetaData()


engine = create_async_engine(settings.DB_URL())

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)
