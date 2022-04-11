from datetime import date

from fin_app_dataset.services.local_transfered_cache.rs3_to_lrdb.stock import (
    StqStockpriceService
)


stockprice_svc = StqStockpriceService()
# stockprice = [d.__dict__ for d in stockprice_svc.get_by_code(code=1301)]
stockprice = stockprice_svc.get_by_code(code=1301)
print(len(stockprice))
print(stockprice[:10])


# stockprice = [d.__dict__ for d in stockprice_svc.get_by_y(code=1301, year=2019)]
stockprice = stockprice_svc.get_by_y(code=1301, year=2019)
print(len(stockprice))
print(stockprice[:10])


# stockprice = [d.__dict__ for d in stockprice_svc.get_by_ym(code=1301, year=2019, month=6)]
stockprice = stockprice_svc.get_by_ym(code=1301, year=2019, month=6)
print(len(stockprice))
print(stockprice[:10])


# stockprice = [d.__dict__ for d in stockprice_svc.get_by_ymd(code=1301, year=2019, month=6, day=3)]
stockprice = stockprice_svc.get_by_ymd(code=1301, year=2019, month=6, day=3)
print(len(stockprice))
print(stockprice[:10])


# stockprice = [d.__dict__ for d in stockprice_svc.get_by_date(code=1301, date=date(2019, 6, 3))]
stockprice = stockprice_svc.get_by_date(code=1301, date=date(2019, 6, 3))
print(len(stockprice))
print(stockprice[:10])
