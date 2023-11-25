from fastapi import FastAPI, Depends, APIRouter
from asyncio import get_event_loop

from hack_change.databases.db_init import init_db
from hack_change.routes import documents_package

app = FastAPI(
    title="FastAPI App",
)

app.include_router(documents_package.router)

loop = get_event_loop()
loop.create_task(init_db())






