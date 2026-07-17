import streamlit as st

from app.models.company import Company


def render_business_summary(company: Company):
    """
    Render the company's business overview.
    """

    st.subheader("📝 Business Overview")

    st.write(company.business_summary)