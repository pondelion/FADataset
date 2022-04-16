from datetime import date

from fin_app_dataset.repositories.dynamo.news import GoogleNewsRepository


repo = GoogleNewsRepository()

print(repo.get_by_date(date=date(2020, 3, 2)))

print(repo.get_by_date(date=date(2020, 3, 2), return_df=False)[:3])

print(repo.get_by_daterange(start_date=date(2020, 3, 2), end_date=date(2020, 3, 5)))

print(repo.get_by_daterange(start_date=date(2020, 3, 2), end_date=date(2020, 3, 5), return_df=False)[-3:])