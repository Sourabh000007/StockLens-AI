import streamlit as st


def render_ai_news_summary(news_summary: str,):
    
    """
    Render the AI-generated news summary.
    """

    st.markdown("### Recent News Analysis")

    st.info(news_summary)

    st.divider()