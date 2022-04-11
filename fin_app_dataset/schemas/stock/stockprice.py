from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class DailyStockpriceSchema(BaseModel):
    date: date
    open: int
    close: int
    high: int
    low: int
    volume: Optional[int]


class DailyStockpriceInDBSchema(DailyStockpriceSchema):
    id: int
    company_code: int
    created_at: datetime


class DailyStockpriceCreateSchema(DailyStockpriceSchema):
    company_code: int
