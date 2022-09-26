from datetime import date
from typing import List, Optional

from sqlalchemy import extract
from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from ..base import BaseRDBRepository
from ....models.rdb.financial import YFFinancialModel
from ....schemas.financial import YFFinancialCreateSchema


class YFFinancialRepository(BaseRDBRepository[YFFinancialModel, YFFinancialCreateSchema, YFFinancialCreateSchema]):

    def __init__(self):
        super().__init__(YFFinancialModel)

    def get_by_code(self, db: Session, *, code: int) -> Optional[List[YFFinancialModel]]:
        return db.query(self._model).filter(self._model.company_code == code).all()

    def get_by_y(self, db: Session, *, code: int, year: int) -> Optional[List[YFFinancialModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            extract('year', self._model.date) == year,
        ).all()

    def get_by_ym(self, db: Session, *, code: int, year: int, month: int) -> Optional[List[YFFinancialModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            extract('year', self._model.date) == year,
            extract('month', self._model.date) == month,
        ).all()

    def get_by_ymd(self, db: Session, *, code: int, year: int, month: int, day: int) -> Optional[List[YFFinancialModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            self._model.date == date(year, month, day)
        ).all()

    def get_by_date(self, db: Session, *, code: int, date: date) -> Optional[List[YFFinancialModel]]:
        return db.query(self._model).filter(
            self._model.company_code == code,
            self._model.date == date,
        ).all()
