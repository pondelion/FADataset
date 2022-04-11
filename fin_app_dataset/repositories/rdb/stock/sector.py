from datetime import date
from typing import List, Optional

from sqlalchemy.sql import func
from sqlalchemy.orm import Session

from ..base import BaseRDBRepository
from ....models.rdb.stock import SectorModel
from ....schemas.stock import SectorCreateSchema


class SectorRepository(BaseRDBRepository[SectorModel, SectorCreateSchema, SectorCreateSchema]):

    def __init__(self):
        super().__init__(SectorModel)

    def get_by_name(self, db: Session, *, name: str) -> Optional[SectorModel]:
        return db.query(self._model).filter(self._model.name == name).all()
