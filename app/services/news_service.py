from app.models.news_article import NewsArticle
from app.repositories.news_repository import NewsRepository


class NewsService:
    """
    Business logic for company news.
    """

    def __init__(self,repository: NewsRepository):

        self.repository = repository

    def get_news(self,symbol: str) -> list[NewsArticle]:
        
        """
        Retrieve the latest company news.
        """

        return self.repository.get_news(symbol)