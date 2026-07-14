import streamlit as st

from app.models.company import Company


def render_company_card(company: Company):
    """
    Render the company information section.
    """

    st.subheader("🏢 Company Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Company**")
        st.write(company.company_name)

        st.write("**Symbol**")
        st.write(company.symbol)

        st.write("**Exchange**")
        st.write(company.exchange)

        st.write("**Sector**")
        st.write(company.sector)

    with col2:
        st.write("**Industry**")
        st.write(company.industry)

        st.write("**Country**")
        st.write(company.country)

        st.write("**City**")
        st.write(company.city)

        st.write("**Website**")
        st.write(company.website)

    if company.full_time_employees:
        st.write("**Full-Time Employees**")
        st.write(f"{company.full_time_employees:,}")

    if company.business_summary:
        with st.expander("📖 Business Summary"):
            st.write(company.business_summary)

    st.divider()