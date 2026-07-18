import streamlit as st

from app.models.company import Company


def render_company_hero(
    company: Company,
):
    """
    Render the company hero section.
    """

    st.title(company.company_name)

    st.caption(
        f"{company.exchange} • {company.symbol}"
    )

    st.write(
        f"**{company.sector} • {company.industry}**"
    )

    col1, col2, col3, col4 = st.columns([1, 1.2, 0.8, 1])

    with col1:

        st.write(f"🌍 {company.country}")

    with col2:

        if company.full_time_employees:

            st.write(
                f"👥 {company.full_time_employees:,} Employees"
            )

    with col3:

        if company.website:

            st.link_button(
                "🌐 Visit Website",
                company.website,
                use_container_width=True,
            )

    st.divider()