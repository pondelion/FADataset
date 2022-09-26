from typing import Optional

import pandas as pd

from .s3 import BaseS3Repository
from ....datasets.company_financials import CompanyFinancialsYFinance
from ....utils.config import AWSConfig


class YFFinancialS3Repository(BaseS3Repository):

    def __init__(self, bucket_name: str = AWSConfig.S3_BUCKET_NAME):
        super().__init__(bucket_name)
        self._dataset = None

    def get(self, code: int) -> Optional[pd.DataFrame]:
        self._dataset = CompanyFinancialsYFinance(code=code)
        return self._dataset.df()
