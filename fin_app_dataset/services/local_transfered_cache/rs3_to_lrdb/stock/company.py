from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
import pandas as pd

from .sector import SectorService
from ..base import Base
from .....models.rdb.stock import CompanyModel
from .....repositories.rdb.stock import CompanyRepository
from .....repositories.storage.s3.company import CompanyS3Repository
from .....schemas.stock import CompanyCreateSchema
from .....utils.logger import Logger


class CompanyService(Base):

    def __init__(self):
        super().__init__(
            CompanyRepository(),
            CompanyS3Repository(),
        )
        self._sector_svc = SectorService()

    def get_all(self) -> Optional[List[CompanyModel]]:
        records = self._local_rdb_repo.get_all(self._local_db)
        if records:
            Logger.i('CompanyService.get_all', f'Company list found in local db, using the data in db as cache.')
            return records
        else:
            Logger.i('CompanyService.get_all', f'Company list not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get()
            self._import_df_to_local_db(df)
            records = self._local_rdb_repo.get_all(self._local_db)
            return records

    def _import_df_to_local_db(self, df: pd.DataFrame) -> None:
        df_renamed = df.rename(columns={
            '銘柄コード': 'code',
            '銘柄名': 'name',
            '市場名': 'market',
            '業種分類': 'sector',
        })
        dict_list = df_renamed.apply(lambda x: {col: x[col] for col in df_renamed.columns}, axis=1).tolist()
        sectors = self._sector_svc.get_all()
        name_id_mappings = {s.name: s.id for s in sectors}
        [d.update({'sector_id': name_id_mappings.get(d['sector'], None)}) for d in dict_list]
        schemas = [CompanyCreateSchema.parse_obj(d) for d in dict_list]
        self._local_rdb_repo.create_all(self._local_db, data_list=schemas)
