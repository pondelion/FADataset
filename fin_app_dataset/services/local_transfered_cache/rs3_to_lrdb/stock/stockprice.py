from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session
import pandas as pd

from ..base import Base
from .....models.rdb.stock import StqDailyStockpriceModel
from .....repositories.rdb.stock import StqDailyStockpriceRepository
from .....repositories.storage.s3.stockprice import StqStockpriceS3Repository
from .....schemas.stock import DailyStockpriceCreateSchema
from .....utils.logger import Logger


class StqStockpriceService(Base):

    def __init__(self):
        super().__init__(
            StqDailyStockpriceRepository(),
            StqStockpriceS3Repository(),
        )

    def get_by_code(self, code: int, convert_to_df: bool = True) -> Optional[List[StqDailyStockpriceModel]]:
        records = self._local_rdb_repo.get_by_code(self._local_db, code=code)
        if records:
            Logger.i('StqStockpriceService.get_by_code', f'Stockprice data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_code', f'Stock data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_code(self._local_db, code=code)
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_y(self, code: int, year: int, convert_to_df: bool = True) -> Optional[List[StqDailyStockpriceModel]]:
        records = self._local_rdb_repo.get_by_y(self._local_db, code=code, year=year)
        if records:
            Logger.i('StqStockpriceService.get_by_y', f'Stockprice data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_y', f'Stock data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_y(self._local_db, code=code, year=year)
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_ym(
        self,
        code: int,
        year: int,
        month: int,
        convert_to_df: bool = True,
    ) -> Optional[List[StqDailyStockpriceModel]]:
        records = self._local_rdb_repo.get_by_ym(self._local_db, code=code, year=year, month=month)
        if records:
            Logger.i('StqStockpriceService.get_by_ym', f'Stockprice data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_ym', f'Stock data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_ym(self._local_db, code=code, year=year, month=month)
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_ymd(
        self,
        code: int,
        year: int,
        month: int,
        day: int,
        convert_to_df: bool = True,
    ) -> Optional[List[StqDailyStockpriceModel]]:
        records = self._local_rdb_repo.get_by_ymd(
            self._local_db, code=code, year=year, month=month, day=day,
        )
        if records:
            Logger.i('StqStockpriceService.get_by_ymd', f'Stockprice data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_ymd', f'Stock data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_ymd(
                self._local_db, code=code, year=year, month=month, day=day,
            )
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_date(self, code: int, date: date, convert_to_df: bool = True) -> Optional[List[StqDailyStockpriceModel]]:
        records = self._local_rdb_repo.get_by_date(
            self._local_db,
            code=code,
            date=date,
        )
        if records:
            Logger.i('StqStockpriceService.get_by_date', f'Stockprice data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_date', f'Stock data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_date(
                self._local_db,
                code=code,
                date=date,
            )
        return self._convert_to_df(records) if convert_to_df else records

    def _import_df_to_local_db(self, code: int, df: pd.DataFrame) -> None:
        df_renamed = df.rename(columns={
            'Date': 'date',
            'Open':'open',
            'High': 'high',
            'Low': 'low',
            'Close': 'close',
            'Volume': 'volume',
        })
        df_renamed['date'] = df_renamed.index
        dict_list = df_renamed.apply(lambda x: {col: x[col] for col in df_renamed.columns}, axis=1).tolist()
        [d.update({'company_code': code}) for d in dict_list]
        print(dict_list[0])
        schemas = [DailyStockpriceCreateSchema.parse_obj(d) for d in dict_list]
        Logger.i('StqStockpriceService', f"Start importing {code}'s stockprice data to local db")
        self._local_rdb_repo.create_all(self._local_db, data_list=schemas)
        Logger.i('StqStockpriceService', 'Done import')
