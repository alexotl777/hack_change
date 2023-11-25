from typing import Annotated
from fastapi import UploadFile, Form, APIRouter

from pydantic import BaseModel



class PrimaryDocs(BaseModel):

    passport: Annotated[bytes, UploadFile]
    # employment_doc: Annotated[UploadFile, Form()]
    # revenue_doc: Annotated[UploadFile, Form()]
    # other_docs: Annotated[UploadFile, Form()] | None = None

