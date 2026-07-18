from app.repositories.news_repository import NewsRepository
from app.services.news_service import NewsService


def test_get_news():

    repository = NewsRepository()

    service = NewsService(repository)

    articles = service.get_news("TCS.NS")

    assert len(articles) > 0

    assert articles[0].title != ""