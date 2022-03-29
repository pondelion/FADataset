from datetime import date
from typing import List, Optional

from sqlalchemy.sql import func

from ..base import BaseRDBRepository
from ...db.rdb import Session
from ...models.rdb.stock import SectorModel
from ...schemas.stock import SectorCreateSchema


class SectorRepository(BaseRDBRepository[SectorModel, SectorCreateSchema, SectorCreateSchema]):

    def __init__(self):
        super().__init__(SectorModel)
