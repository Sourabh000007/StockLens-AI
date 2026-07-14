from app.builders.candlestick_chart_builder import (
    CandlestickChartBuilder,
)
from app.repositories.market_repository import MarketRepository
from app.transformers.market_transformer import MarketTransformer


def main():
    repository = MarketRepository()

    history = repository.get_price_history("TCS.NS")

    chart_data = MarketTransformer.to_chart_data(history)

    figure = CandlestickChartBuilder.build(chart_data)

    figure.show()


if __name__ == "__main__":
    main()