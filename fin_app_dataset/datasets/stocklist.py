import os
from datetime import datetime, date

from overrides import overrides
import pandas as pd

from .base.s3_csv_cached_data import S3CSVCachedData
from ..utils.config import DataLocationConfig


class StockListLegacy(S3CSVCachedData):

    @overrides
    def _local_cache_path(self) -> str:
        local_cache_path = os.path.join(
            DataLocationConfig.LOCAL_CACHE_DIR,
            'stocklist',
            'stocklist.csv'
        )
        return local_cache_path

    @overrides
    def _source_path(self) -> str:
        source_path = DataLocationConfig.STOCKLIST_FILE
        return source_path


class StockList(S3CSVCachedData):

    @overrides
    def _local_cache_path(self) -> str:
        local_cache_path = os.path.join(
            DataLocationConfig.LOCAL_CACHE_DIR,
            'stocklist',
            'stocklist.csv'
        )
        return local_cache_path

    @overrides
    def _source_path(self) -> str:
        source_path = DataLocationConfig.STOCKLIST_FILE_LATEST
        return source_path

    @overrides
    def df(self, force_update: bool = False) -> pd.DataFrame:
        df = super().df(force_update)
        # 古いバージョンにカラム名を合わせる
        new_cols = {
            'コード': '銘柄コード',
            '銘柄名': '銘柄名',
            '市場・商品区分': '市場名',
            '33業種区分': '業種分類',  # or '17業種区分'
        }
        return df.rename(columns=new_cols)
