from datetime import date
from typing import List, Optional

from sqlalchemy import extract
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from ..base import BaseRDBRepository
from ....models.rdb.stock import StqDailyStockpriceModel
from ....schemas.stock import DailyStockpriceSchema, DailyStockpriceCreateSchema


class StqDailyStockpriceRepository(BaseRDBRepository[StqDailyStockpriceModel, DailyStockpriceCreateSchema, DailyStockpriceCreateSchema]):

    def __init__(self):
        super().__init__(StqDailyStockpriceModel)

    def get_by_code(self, db: Session, *, code: int) -> Optional[List[StqDailyStockpriceModel]]:
        return db.query(self._model).filter(self._model.company_code == code).all()

    def get_by_y(self, db: Session, *, code: int, year: int) -> Optional[List[StqDailyStockpriceModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            extract('year', self._model.date) == year,
        ).all()

    def get_by_ym(self, db: Session, *, code: int, year: int, month: int) -> Optional[List[StqDailyStockpriceModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            extract('year', self._model.date) == year,
            extract('month', self._model.date) == month,
        ).all()

    def get_by_ymd(self, db: Session, *, code: int, year: int, month: int, day: int) -> Optional[List[StqDailyStockpriceModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            extract('year', self._model.date) == year,
            extract('month', self._model.date) == month,
            extract('day', self._model.date) == day,
        ).all()

    def get_by_date(self, db: Session, *, code: int, date: date) -> Optional[List[StqDailyStockpriceModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            self._model.date == date,
        ).all()
