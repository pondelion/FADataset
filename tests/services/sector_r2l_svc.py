from fin_app_dataset.services.local_transfered_cache.rs3_to_lrdb.stock import (
    SectorService
)


sector_svc = SectorService()
print([d.__dict__ for d in sector_svc.get_all()])