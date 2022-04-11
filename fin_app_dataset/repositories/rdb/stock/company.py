from datetime import date
from typing import List, Optional

from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from ..base import BaseRDBRepository
from ....models.rdb.stock import CompanyModel
from ....schemas.stock import CompanyCreateSchema


class CompanyRepository(BaseRDBRepository[CompanyModel, CompanyCreateSchema, CompanyCreateSchema]):

    def __init__(self):
        super().__init__(CompanyModel)

    def get_by_name(self, db: Session, *, name: str) -> Optional[CompanyModel]:
        return db.query(self._model).filter(self._model.name == name).all()

    def get_by_code(self, db: Session, *, code: int) -> Optional[CompanyModel]:
        return db.query(self._model).filter(self._model.code == code).all()

    def get_by_code(self, db: Session, *, sector_id: int) -> Optional[List[CompanyModel]]:
        return db.query(self._model).filter(self._model.sector_id == sector_id).all()
