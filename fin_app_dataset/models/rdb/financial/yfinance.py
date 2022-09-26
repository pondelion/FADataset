from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, UniqueConstraint
from sqlalchemy.sql.functions import current_timestamp

from ..base import Base


class YFFinancialModel(Base):
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True, nullable=False)
    date = Column(Date)
    company_code = Column(BigInteger, ForeignKey("company.code"), nullable=False)
    research_development = Column(Float, nullable=True)  # 研究開発費
    effect_of_accounting_charges = Column(Float, nullable=True)  # ?
    income_before_tax = Column(Float, nullable=True)  # 税引前利益
    minority_interest = Column(Float, nullable=True)  # 少数株主持分
    net_income = Column(Float, nullable=True)  # 当期純利益
    selling_general_administrative = Column(Float, nullable=True)  # 販売費及び一般管理費(?)
    gross_profit = Column(Float, nullable=True)  # 売上総利益
    ebit = Column(Float, nullable=True)  # 利払前・税引前利益
    operationg_income = Column(Float, nullable=True)  # 営業利益
    other_operating_expenses = Column(Float, nullable=True)  # その他の営業費用
    interest_expense = Column(Float, nullable=True)  # 支払利息
    extraordinary_items = Column(Float, nullable=True)
    non_recurring = Column(Float, nullable=True)  # 一時的収益(?)費用(?)
    other_items = Column(Float, nullable=True)
    income_tax_expense = Column(Float, nullable=True)  # 法人所得税
    total_revenue = Column(Float, nullable=True)  # 総利益
    total_operating_expense = Column(Float, nullable=True)  # 営業費用合計
    cost_of_revenue = Column(Float, nullable=True)  # 収益費用(?)
    total_other_income_expense_net = Column(Float, nullable=True)  # その他の収益費用合計(?)
    discontinued_operations = Column(Float, nullable=True)
    net_income_from_continuing_ops = Column(Float, nullable=True)
    net_income_applicable_to_common_shares = Column(Float, nullable=True)
    created_at = Column(
        DateTime,
        server_default=current_timestamp()
    )
    __table_args__ = (UniqueConstraint('date', 'company_code', name='unique_date_company_code'),)
