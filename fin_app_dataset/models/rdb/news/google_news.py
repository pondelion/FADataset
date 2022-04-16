from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, BigInteger, Text
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class GoogleNewsModel(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    published = Column(DateTime, nullable=False)
    title = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    topic = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=current_timestamp())
