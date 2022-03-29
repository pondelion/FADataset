from datetime import date
from typing import List, Optional

from sqlalchemy.sql import func

from ..base import BaseRDBRepository
from ...db.rdb import Session
from ...models.rdb.stock import CompanyModel
from ...schemas.stock import CompanyCreateSchema


class CompanyRepository(BaseRDBRepository[CompanyModel, CompanyCreateSchema, CompanyCreateSchema]):

    def __init__(self):
        super().__init__(CompanyModel)
