from fastapi import FastAPI, Depends, APIRouter
from asyncio import get_event_loop

from databases.db_init import init_db
from routes import documents_package
from routes import discription_risks

app = FastAPI(
    title="FastAPI App",
)

app.include_router(documents_package.router)
app.include_router(discription_risks.router)

loop = get_event_loop()
loop.create_task(init_db())






