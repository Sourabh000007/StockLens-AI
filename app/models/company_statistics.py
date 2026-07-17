from pydantic import BaseModel


class CompanyStatistics(BaseModel):
    market_cap: float | None = None
    enterprise_value: float | None = None

    trailing_pe: float | None = None
    forward_pe: float | None = None

    dividend_yield: float | None = None

    beta: float | None = None

    fifty_two_week_high: float | None = None
    fifty_two_week_low: float | None = None