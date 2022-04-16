from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, BigInteger, Text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship

from ..base import Base


class CompanyModel(Base):
    code = Column(BigInteger, primary_key=True, index=True, autoincrement=False, nullable=False)
    name = Column(Text, nullable=False)
    sector_id = Column(BigInteger, ForeignKey("sector.id"), nullable=True)
    market = Column(Text, nullable=True)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )
    updated_at = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp()
    )
    sector = relationship("SectorModel", back_populates="company")
