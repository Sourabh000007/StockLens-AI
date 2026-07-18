from app.repositories.news_repository import NewsRepository


def test_get_news():

    repository = NewsRepository()

    articles = repository.get_news("TCS.NS")

    assert len(articles) > 0

    assert articles[0].title != ""

    assert articles[0].publisher != ""

    assert articles[0].link.startswith("http")