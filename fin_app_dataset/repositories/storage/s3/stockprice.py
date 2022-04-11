from typing import Optional
import os

import pandas as pd

from .s3 import BaseS3Repository
from ....datasets.stockprice import StqStockPrice
from ....utils.config import AWSConfig, DataLocationConfig


class StqStockpriceS3Repository(BaseS3Repository):

    def __init__(self, bucket_name: str = AWSConfig.S3_BUCKET_NAME):
        super().__init__(bucket_name)
        self._S3_FILEPATH_FMT = os.path.join(
            DataLocationConfig.STOCKPRICE_STOOQ_CONCAT_BASEDIR,
            '{CODE}.csv'
        )
        self._dataset = None

    def get(self, code: int) -> Optional[pd.DataFrame]:
        self._dataset = StqStockPrice(code=code)
        return self._dataset.df()
