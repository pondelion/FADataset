from typing import List, TypeVar

from sqlalchemy.orm import Session
import pandas as pd

from ....repositories.rdb.base import BaseRDBRepository
from ....repositories.storage.s3 import BaseS3Repository
from ....db.rdb import local_db
from ....models.rdb.base import Base


ModelType = TypeVar('ModelType', bound=Base)


class Base:

    def __init__(
        self,
        local_rdb_repo: BaseRDBRepository,
        remote_s3_repo: BaseS3Repository,
        local_db: Session = local_db,
    ):
        self._local_db = local_db
        self._local_rdb_repo = local_rdb_repo
        self._remote_s3_repo = remote_s3_repo

    def _convert_to_df(self, data_list: List[ModelType]) -> pd.DataFrame:
        return pd.DataFrame([d.__dict__ for d in data_list])
