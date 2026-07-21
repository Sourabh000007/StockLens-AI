import streamlit as st

from app.models.news_article import NewsArticle
from frontend.utils.datetime_formatter import format_relative_date


def render_news_card(articles: list[NewsArticle]):
    
    """
    Render the latest company news.
    """

    st.subheader("📰 Latest Company News")

    if not articles:
        st.info("No recent news available.")
        return

    for article in articles:

        with st.container(border=True):

            st.markdown(f"### {article.title}")

            col1, col2 = st.columns([2, 1])

            with col1:
                st.caption(f"🏢 {article.publisher}")

            with col2:
                st.caption(
                    f"🕒 {format_relative_date(article.published_at)}"
                )

            st.write(article.summary)

            st.link_button(
                "Read Full Article →",
                article.link,
            )