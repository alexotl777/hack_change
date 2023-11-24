from typing import List, Annotated
from fastapi import FastAPI, HTTPException, Request, Response, status, Depends, Query
from pydantic import BaseModel, Field, ValidationError, validator

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, ResponseValidationError
from fastapi.responses import JSONResponse

import models.models as models
from databases.database import engine, sessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, not_, null, or_


app = FastAPI(
    title="FastAPI App"
)
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class Application(BaseModel):
    pass