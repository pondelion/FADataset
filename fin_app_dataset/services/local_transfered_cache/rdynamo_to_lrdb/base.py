from typing import List, TypeVar

from sqlalchemy.orm import Session
import pandas as pd



from ....repositories.rdb.base import BaseRDBRepository
from ....repositories.dynamo.base import BaseDynamoRepository
from ....db.rdb import local_db
from ....models.rdb.base import Base


ModelType = TypeVar('ModelType', bound=Base)


class Base:

    def __init__(
        self,
        local_rdb_repo: BaseRDBRepository,
        remote_dynamo_repo: BaseDynamoRepository,
        local_db: Session = local_db,
    ):
        self._local_db = local_db
        self._local_rdb_repo = local_rdb_repo
        self._remote_dynamo_repo = remote_dynamo_repo

    def _convert_to_df(self, data_list: List[ModelType]) -> pd.DataFrame:
        return pd.DataFrame([d.__dict__ for d in data_list])
