from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class DailyStockpriceSchema(BaseModel):
    date: date
    open: int
    close: int
    high: str
    low: int


class DailyStockpriceInDBSchema(DailyStockpriceSchema):
    id: int
    company_code: int
    created_at: datetime


class DailyStockpriceCreateSchema(DailyStockpriceSchema):
    company_code: int
