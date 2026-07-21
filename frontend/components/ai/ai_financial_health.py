import streamlit as st


def render_ai_financial_health(analysis: str,):
    """
    Render AI financial health analysis.
    """

    st.markdown("### Financial Health")

    st.success(analysis)

    st.divider()