from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, BigInteger
from sqlalchemy.dialects.mysql import DATETIME, TEXT
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class DailyStockpriceModel(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    date = Column(DateTime, nullable=False)
    open = Column(Integer, nullable=False)
    close = Column(Integer, nullable=False)
    high = Column(Integer, nullable=False)
    low = Column(Integer, nullable=True)
    company_code = Column(BigInteger, ForeignKey("company.code"), nullable=False)
    created_at = Column(
        DATETIME(fsp=6),
        server_default=current_timestamp(6)
    )
    # updated_at = Csolumn(
    #     DATETIME(fsp=6),
    #     server_default=current_timestamp(6),
    #     onupdate=current_timestamp(6)
    # )
