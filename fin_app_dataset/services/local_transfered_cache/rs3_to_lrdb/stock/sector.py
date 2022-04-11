from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
import pandas as pd

from ..base import Base
from .....models.rdb.stock import SectorModel
from .....repositories.rdb.stock import SectorRepository
from .....repositories.storage.s3.company import CompanyS3Repository
from .....schemas.stock import SectorCreateSchema
from .....utils.logger import Logger


class SectorService(Base):

    def __init__(self):
        super().__init__(
            SectorRepository(),
            CompanyS3Repository(),
        )

    def get_all(self) -> Optional[List[SectorModel]]:
        records = self._local_rdb_repo.get_all(self._local_db)
        if records:
            Logger.i('SectorService.get', f'Sector list found in local db, using the data in db as cache.')
            return records
        else:
            Logger.i('SectorService.get', f'Sector list not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get()
            self._import_df_to_local_db(df=df)
            records = self._local_rdb_repo.get_all(self._local_db)
            return records

    def _import_df_to_local_db(self, df: pd.DataFrame) -> None:
        uniq_sector_names = df['業種分類'].unique()
        dict_list = [{'name': name} for name in uniq_sector_names]
        schemas = [SectorCreateSchema.parse_obj(d) for d in dict_list]
        self._local_rdb_repo.create_all(self._local_db, data_list=schemas)
