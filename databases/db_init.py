from logger import loger
from databases.db_settings import engine, Base
from sqlalchemy import select


async def init_db():
    loger.info(Base)
    async with engine.connect() as conn:

        loger.debug(f'{conn=}')
        loger.debug(f'{Base.metadata=}')
        await conn.run_sync(Base.metadata.drop_all)
        loger.debug('Дропнул базу данных')
        await conn.run_sync(Base.metadata.create_all)
        loger.debug('Создал базу данных')