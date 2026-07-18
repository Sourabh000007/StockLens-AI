from app.repositories.news_repository import NewsRepository
from app.services.news_service import NewsService


class NewsDashboardService:
    """
    Dashboard service for company news.
    """

    def __init__(self):

        repository = NewsRepository()

        self.news_service = NewsService(repository)

    def get_news(self,symbol: str):

        """
        Retrieve company news.
        """

        return self.news_service.get_news(symbol)