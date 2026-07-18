import streamlit as st

from app.models.news_article import NewsArticle


def render_news_card(articles: list[NewsArticle]):
    
    """
    Render the latest company news.
    """

    st.subheader("📰 Latest Company News")

    if not articles:
        st.info("No recent news available.")
        return

    for article in articles:

        with st.container():

            st.markdown(
                f"### {article.title}"
            )

            st.caption(
                f"{article.publisher} • {article.published_at}"
            )

            if article.summary:
                st.write(article.summary)

            st.link_button(
                "Read Full Article",
                article.link,
            )

            st.divider()