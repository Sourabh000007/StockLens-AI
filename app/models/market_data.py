from datetime import date

from pydantic import BaseModel


class PriceData(BaseModel):
    date: date
    open: float
    high: float
    low: float
    close: float
    volume: int