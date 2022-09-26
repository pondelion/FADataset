from datetime import date
from typing import List, Optional

import pandas as pd
import jpholiday

from ..base import Base
from .....models.rdb.financial import YFFinancialModel
from .....repositories.rdb.financial import YFFinancialRepository
from .....repositories.storage.s3.financial import YFFinancialS3Repository
from .....schemas.financial import YFFinancialCreateSchema
from .....utils.logger import Logger


class YFFinancialService(Base):

    def __init__(self):
        super().__init__(
            YFFinancialRepository(),
            YFFinancialS3Repository(),
        )

    def get_by_code(self, code: int, convert_to_df: bool = True) -> Optional[List[YFFinancialModel]]:
        records = self._local_rdb_repo.get_by_code(self._local_db, code=code)
        if records:
            Logger.i('YFFinancialService.get_by_code', f'YFFinancial data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('YFFinancialService.get_by_code', f'YFFinancial data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_code(self._local_db, code=code)
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_y(self, code: int, year: int, convert_to_df: bool = True) -> Optional[List[YFFinancialModel]]:
        records = self._local_rdb_repo.get_by_y(self._local_db, code=code, year=year)
        if records:
            Logger.i('YFFinancialService.get_by_y', f'YFFinancial data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('YFFinancialService.get_by_y', f'YFFinancial data for {code} not found in local db, downloading from S3.')
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
    ) -> Optional[List[YFFinancialModel]]:
        records = self._local_rdb_repo.get_by_ym(self._local_db, code=code, year=year, month=month)
        if records:
            Logger.i('YFFinancialService.get_by_ym', f'YFFinancial data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('YFFinancialService.get_by_ym', f'YFFinancial data for {code} not found in local db, downloading from S3.')
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
    ) -> Optional[List[YFFinancialModel]]:
        dt = date(year, month, day)
        if dt.weekday() >= 5 or jpholiday.is_holiday(dt):
            Logger.w('YFFinancialService.get_by_ymd', f'specified day {dt} is holyday')
            return pd.DataFrame([]) if convert_to_df else []
        records = self._local_rdb_repo.get_by_ymd(
            self._local_db, code=code, year=year, month=month, day=day,
        )
        if records:
            Logger.i('YFFinancialService.get_by_ymd', f'YFFinancial data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('StqStockpriceService.get_by_ymd', f'YFFinancial data for {code} not found in local db, downloading from S3.')
            df = self._remote_s3_repo.get(code=code)
            self._import_df_to_local_db(code=code, df=df)
            records = self._local_rdb_repo.get_by_ymd(
                self._local_db, code=code, year=year, month=month, day=day,
            )
        return self._convert_to_df(records) if convert_to_df else records

    def get_by_date(self, code: int, date: date, convert_to_df: bool = True) -> Optional[List[YFFinancialModel]]:
        records = self._local_rdb_repo.get_by_date(
            self._local_db,
            code=code,
            date=date,
        )
        if records:
            Logger.i('YFFinancialService.get_by_date', f'YFFinancial data for {code} found in local db, using the data in db as cache.')
        else:
            Logger.i('YFFinancialService.get_by_date', f'YFFinancial data for {code} not found in local db, downloading from S3.')
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
            'Research Development': 'research_development',
            'Effect Of Accounting Charges': 'effect_of_accounting_charges',
            'Income Before Tax': 'income_before_tax',
            'Minority Interest': 'minority_interest',
            'Net Income': 'net_income',
            'Selling General Administrative': 'selling_general_administrative',
            'Gross Profit': 'gross_profit',
            'Ebit': 'ebit',
            'Operating Income': 'operationg_income',
            'Other Operating Expenses': 'other_operating_expenses',
            'Interest Expense': 'interest_expense',
            'Extraordinary Items': 'extraordinary_items',
            'Non Recurring': 'non_recurring',
            'Other Items': 'other_items',
            'Income Tax Expense': 'income_tax_expense',
            'Total Revenue': 'total_revenue',
            'Total Operating Expenses': 'total_operating_expense',
            'Cost Of Revenue': 'cost_of_revenue',
            'Total Other Income Expense Net': 'total_other_income_expense_net',
            'Discontinued Operations': 'discontinued_operations',
            'Net Income From Continuing Ops': 'net_income_from_continuing_ops',
            'Net Income Applicable To Common Shares': 'net_income_applicable_to_common_shares',
        })
        dict_list = df_renamed.apply(lambda x: {col: x[col] if not pd.isna(x[col]) else None for col in df_renamed.columns}, axis=1).tolist()
        [d.update({'company_code': code}) for d in dict_list]
        objs = [YFFinancialCreateSchema.parse_obj(d) for d in dict_list]
        Logger.i('YFFinancialService', f"Start importing {code}'s YFFinancial data to local db")
        self._local_rdb_repo.create_all(self._local_db, data_list=objs)
        Logger.i('YFFinancialService', 'Done import')
