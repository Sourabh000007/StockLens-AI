from datetime import date

from pydantic import BaseModel


class ChartData(BaseModel):
    dates: list[date]
    opens: list[float]
    highs: list[float]
    lows: list[float]
    closes: list[float]
    volumes: list[int]