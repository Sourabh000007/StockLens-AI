import yfinance as yf

from app.core.logger import logger
from app.models.news_article import NewsArticle


class NewsRepository:
    """
    Repository responsible for fetching company news.
    """

    def _get_ticker(self,symbol: str,) -> yf.Ticker:

        """
        Create and return a Yahoo Finance ticker.
        """

        return yf.Ticker(symbol)
    
    def _map_article(self,article: dict,) -> NewsArticle:

        """
        Convert a Yahoo Finance article into a NewsArticle.
        """

        content = article["content"]

        return NewsArticle(
            title=content["title"],
            publisher=content["provider"]["displayName"],
            published_at=content["pubDate"],
            link=content["clickThroughUrl"]["url"],
            summary=content["summary"],
        )
    
    def get_news(self,symbol: str,) -> list[NewsArticle]:

        """
        Retrieve the latest company news.
        """

        logger.info("Fetching news for {}",symbol)

        try:

            ticker = self._get_ticker(symbol)

            articles = ticker.news

            if not articles:
                return []

            return [
                self._map_article(article)
                for article in articles
            ]

        except Exception:
            logger.exception(
                "Failed to fetch news for {}",
                symbol,
            )
            raise