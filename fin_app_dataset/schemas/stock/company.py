from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class CompanySchema(BaseModel):
    code: int
    name: str
    market: Optional[str]


class CompanyInDBSchema(CompanySchema):
    id: int
    sector_id: Optional[int]
    created_at: datetime
    updated_at: datetime


class CompanyCreateSchema(CompanySchema):
    sector_id: Optional[int]
