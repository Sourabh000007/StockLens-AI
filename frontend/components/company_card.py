import streamlit as st

from app.models.company import Company


def render_company_card(company: Company):

    st.subheader("🏢 Company Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Company:** {company.company_name}")
        st.write(f"**Short Name:** {company.short_name}")
        st.write(f"**Symbol:** {company.symbol}")
        st.write(f"**Exchange:** {company.exchange}")
        st.write(f"**Sector:** {company.sector}")
        st.write(f"**Industry:** {company.industry}")

    with col2:
        st.write(f"**Country:** {company.country}")
        st.write(f"**City:** {company.city}")

        if company.full_time_employees:
            st.write(
                f"**Employees:** {company.full_time_employees:,}"
            )

        st.write(f"**Website:** {company.website}")

        if company.investor_relations_website:
            st.write(
                f"**Investor Relations:** {company.investor_relations_website}"
            )