import streamlit as st

from app.models.company import Company


def render_business_summary(company: Company):
    """
    Render the company's business overview.
    """

    # st.subheader("📝 Business Overview")

    preview = company.business_summary[:450]

    if len(company.business_summary) > 450:
        preview += "..."

    st.subheader("📝 Business Overview")

    st.write(preview)

    with st.expander("Read full overview"):

        st.write(company.business_summary)