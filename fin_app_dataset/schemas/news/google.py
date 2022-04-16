from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class GoogleNewsSchema(BaseModel):
    published: datetime
    title: str
    summary: str
    topic: str


class GoogleNewsInDBSchema(GoogleNewsSchema):
    id: int
    created_at: datetime


class GoogleNewsCreateSchema(GoogleNewsSchema):
    pass
