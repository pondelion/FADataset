from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel


class YFFinancialSchema(BaseModel):
    date: date
    company_code: int
    research_development: Optional[float] = None
    effect_of_accounting_charges: Optional[float] = None
    income_before_tax: Optional[float] = None
    minority_interest: Optional[float] = None
    net_income: Optional[float] = None
    selling_general_administrative: Optional[float] = None
    gross_profit: Optional[float] = None
    ebit: Optional[float] = None
    operationg_income: Optional[float] = None
    other_operating_expenses: Optional[float] = None
    interest_expense: Optional[float] = None
    extraordinary_items: Optional[float] = None
    non_recurring: Optional[float] = None
    other_items: Optional[float] = None
    income_tax_expense: Optional[float] = None
    total_revenue: Optional[float] = None
    total_operating_expense: Optional[float] = None
    cost_of_revenue: Optional[float] = None
    total_other_income_expense_net: Optional[float] = None
    discontinued_operations: Optional[float] = None
    net_income_from_continuing_ops: Optional[float] = None
    net_income_applicable_to_common_shares: Optional[float] = None


class YFFinancialInDBSchema(YFFinancialSchema):
    id: int
    created_at: datetime


class YFFinancialCreateSchema(YFFinancialSchema):
    pass
