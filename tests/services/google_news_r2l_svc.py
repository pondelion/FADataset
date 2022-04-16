from datetime import date

from fin_app_dataset.services.local_transfered_cache.rdynamo_to_lrdb.news import (
    GoogleNewsService
)


google_news_svc = GoogleNewsService()
models = google_news_svc.get_by_date(date=date(2020, 3, 2))
news = [d.__dict__ for d in models]
print(len(news))
print(news[:3])

