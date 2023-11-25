from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from hack_change.config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(settings.DB_URL)
async_session_factory = async_sessionmaker(engine, expire_on_commit=False)


