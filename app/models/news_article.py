from pydantic import BaseModel


class NewsArticle(BaseModel):
    """
    Represents a single news article.
    """

    title: str

    publisher: str

    published_at: str

    link: str

    summary: str