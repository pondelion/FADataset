from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, BigInteger
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class YFDailyStockpriceModel(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    date = Column(Date, nullable=False)
    open = Column(Integer, nullable=False)
    close = Column(Integer, nullable=False)
    high = Column(Integer, nullable=False)
    low = Column(Integer, nullable=True)
    company_code = Column(BigInteger, ForeignKey("company.code"), nullable=False)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )


class StqDailyStockpriceModel(Base):
    date = Column(Date, nullable=False, primary_key=True, index=True)
    open = Column(Integer, nullable=False)
    close = Column(Integer, nullable=False)
    high = Column(Integer, nullable=False)
    low = Column(Integer, nullable=False)
    volume = Column(Integer, nullable=False)
    company_code = Column(BigInteger, ForeignKey("company.code"), nullable=False, primary_key=True, index=True)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )
