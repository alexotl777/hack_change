import sys, os
import logging
import uvicorn
from fastapi import FastAPI, Depends, APIRouter
from asyncio import get_event_loop
sys.path.insert(1, os.path.join(sys.path[0], 'hack_change'))

from databases.db_init import init_db
from routes import documents_package


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


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=80)





