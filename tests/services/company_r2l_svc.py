from fin_app_dataset.services.local_transfered_cache.rs3_to_lrdb.stock import (
    CompanyService
)


company_svc = CompanyService()
companies = [d.__dict__ for d in company_svc.get_all()]
print(len(companies))
print(companies[:3])