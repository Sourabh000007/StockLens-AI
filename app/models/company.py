from pydantic import BaseModel


class Company(BaseModel):
    """
    Represents the static profile of a company.

    This model intentionally contains only identity/profile
    information. Dynamic market data (price, market cap, volume,
    etc.) belongs in separate models.
    """

    symbol: str

    company_name: str
    short_name: str

    exchange: str

    sector: str
    industry: str

    country: str
    city: str

    website: str

    business_summary: str

    investor_relations_website: str | None = None

    full_time_employees: int | None = None

