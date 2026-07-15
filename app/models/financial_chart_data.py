from pydantic import BaseModel


class FinancialChartData(BaseModel):
    """
    Generic financial chart data.
    """

    x: list[str]
    y: list[float]
    title: str
    y_axis_title: str