from datetime import date
from typing import List, Optional, Union

import pandas as pd

from ..base import BaseDynamoRepository
from ....datasets.google_news import GoogleNews as GoogleNewsDatasets
from ....schemas.news import GoogleNewsSchema
from ....utils.config import AWSConfig


class GoogleNewsDynamoRepository(BaseDynamoRepository):

    def __init__(self, table_name: str = AWSConfig.DYNAMODB_GOOGLE_RSS_NEWS_TABLE_NAME):
        super().__init__(table_name=table_name)

    def get_by_date(
        self, date: date, return_df: bool = True
    ) -> Optional[Union[pd.DataFrame, List[GoogleNewsSchema]]]:
        dataset = GoogleNewsDatasets(publised_date=date)
        df_news = dataset.df()
        if return_df:
            return df_news
        if len(df_news) == 0:
            return []
        dict_datalist = df_news.apply(lambda row: {col: row[col] for col in df_news.columns}, axis=1).tolist()
        return [GoogleNewsSchema.parse_obj(dict_data) for dict_data in dict_datalist]

    def get_by_daterange(
        self, start_date: date, end_date: date, return_df: bool = True
    ) -> Optional[Union[pd.DataFrame, List[GoogleNewsSchema]]]:
        news_list = [self.get_by_date(date, return_df=return_df) for date in pd.date_range(start_date, end_date, freq='D')]
        if return_df:
            return pd.concat(news_list)
        else:
            return sum(news_list, [])
