from datetime import date
from typing import List, Optional

import pandas as pd

from ..base import Base
from .....models.rdb.news.google_news import GoogleNewsModel
from .....repositories.rdb.news import GoogleNewsRDBRepository
from .....repositories.dynamo.news import GoogleNewsDynamoRepository
from .....schemas.news.google import GoogleNewsSchema
from .....utils.logger import Logger


class GoogleNewsService(Base):

    def __init__(self):
        super().__init__(
            GoogleNewsRDBRepository(),
            GoogleNewsDynamoRepository(),
        )

    def get_by_date(self, date: date) -> Optional[List[GoogleNewsModel]]:
        records = self._local_rdb_repo.get_by_date(self._local_db, date=date)
        if records:
            Logger.i('SectorService.get', f'Google news data at {date} found in local db, using the data in db as cache.')
            return records
        else:
            Logger.i('SectorService.get', f'Google news data at {date} not found in local db, downloading from DynamoDB.')
            news_list = self._remote_dynamo_repo.get_by_date(date=date, return_df=False)
            self._import_news_to_local_db(news=news_list, date=date)
            records = self._local_rdb_repo.get_all(self._local_db)
            return records

    def get_by_daterange(self, start_date: date, end_date: date) -> Optional[List[GoogleNewsModel]]:
        records_list = [self.get_by_date(date) for date in pd.date_range(start_date, end_date, freq='D')]
        return sum(records_list, [])

    def _import_news_to_local_db(self, news: List[GoogleNewsSchema], date: date) -> None:
        Logger.i('GoogleNewsService', f"Start importing {date}'s news data to local db")
        self._local_rdb_repo.create_all(self._local_db, data_list=news)
        Logger.i('GoogleNewsService', 'Done import')
