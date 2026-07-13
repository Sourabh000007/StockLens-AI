from pydantic import BaseModel


class Company(BaseModel):
    symbol: str
    company_name: str
    exchange: str
    sector: str
    industry: str