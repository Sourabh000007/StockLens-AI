import streamlit as st


def render_ai_company_summary(summary: str,):
    
    """
    Render the AI-generated company summary.
    """

    st.subheader("🤖 AI Company Summary")

    st.info(summary)