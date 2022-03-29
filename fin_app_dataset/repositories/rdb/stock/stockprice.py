from datetime import date
from typing import List, Optional

from sqlalchemy.sql import func

from ..base import BaseRDBRepository
from ...db.rdb import Session
from ...models.rdb.stock import DailyStockpriceModel
from ...schemas.stock import DailyStockpriceSchema, DailyStockpriceCreateSchema


class DailyStockpriceRepository(BaseRDBRepository[DailyStockpriceModel, DailyStockpriceCreateSchema, DailyStockpriceCreateSchema]):

    def __init__(self):
        super().__init__(DailyStockpriceModel)

    def get_by_code(self, db: Session, *, code: int) -> Optional[List[DailyStockpriceModel]]:
        return db.query(self._model).filter(self._model.coder == code).all()

    def get_by_y(self, db: Session, *, code: int, year: int) -> Optional[List[StockpriceModel]]:
        return db.query(self._model).filter(
            self._model.coder == code,
            self._model.date.year == year,
        ).all()

    def get_by_ym(self, db: Session, *, code: int, year: int, month: int) -> Optional[List[StockpriceModel]]:
        return db.query(self._model).filter(
            self._model.coder == code,
            self._model.date.year == year,
            self._model.date.month == month,
        ).all()

    def get_by_ymd(self, db: Session, *, code: int, year: int, month: int, day: int) -> Optional[List[StockpriceModel]]:
        return db.query(self._model).filter(
            self._model.coder == code,
            self._model.date.year == year,
            self._model.date.month == month,
            self._model.date.month == month,
        ).all()

    def get_by_date(self, db: Session, *, code: int, date: date) -> Optional[List[StockpriceModel]]:
        return db.query(self._model).filter(
            self._model.coder == code,
            self._model.date.year == year,
            self._model.date == date,
        ).all()
