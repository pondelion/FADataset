from fin_app_dataset.services.local_transfered_cache.rs3_to_lrdb.stock import (
    CompanyService
)


company_svc = CompanyService()
models = company_svc.get_all()
companies = [d.__dict__ for d in models]
print(len(companies))
print(companies[:3])
print(models[0].sector.__dict__)
