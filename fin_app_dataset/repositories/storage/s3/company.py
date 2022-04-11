from typing import Optional

import pandas as pd

from .s3 import BaseS3Repository
from ....datasets.stocklist import StockList
from ....utils.config import AWSConfig


class CompanyS3Repository(BaseS3Repository):

    def __init__(self, bucket_name: str = AWSConfig.S3_BUCKET_NAME):
        super().__init__(bucket_name)
        self._dataset = None

    def get(self) -> Optional[pd.DataFrame]:
        self._dataset = StockList()
        return self._dataset.df()
