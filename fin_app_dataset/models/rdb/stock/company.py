from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, BigInteger
from sqlalchemy.dialects.mysql import DATETIME, TEXT
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class CompanyModel(Base):
    code = Column(BigInteger, primary_key=True, index=True, autoincrement=False, nullable=False)
    name = Column(TEXT, nullable=False)
    sector_id = Column(BigInteger, ForeignKey("sector.id"), nullable=True)
    market = Column(TEXT, nullable=True)
    created_at = Column(
        DATETIME(fsp=6),
        server_default=current_timestamp(6)
    )
    updated_at = Column(
        DATETIME(fsp=6),
        server_default=current_timestamp(6),
        onupdate=current_timestamp(6)
    )
