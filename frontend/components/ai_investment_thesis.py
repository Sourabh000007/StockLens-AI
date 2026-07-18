import streamlit as st


def render_ai_investment_thesis(
    thesis: str,
):
    """
    Render the AI investment thesis.
    """

    st.subheader("💡 Investment Thesis")

    st.info(thesis)