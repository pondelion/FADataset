from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class SectorSchema(BaseModel):
    name: str


class SectorInDBSchema(SectorSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class SectorCreateSchema(SectorSchema):
    pass
