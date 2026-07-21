import streamlit as st

from app.models.company_statistics import CompanyStatistics


def _format_large_number(value: float | None) -> str:
    """
    Format large financial values.
    """

    if value is None:
        return "N/A"

    if value >= 1_000_000_000_000:
        return f"₹{value / 1_000_000_000_000:.2f}T"

    if value >= 1_000_000_000:
        return f"₹{value / 1_000_000_000:.2f}B"

    if value >= 1_000_000:
        return f"₹{value / 1_000_000:.2f}M"

    return f"₹{value:,.0f}"


def _format_percentage(value: float | None) -> str:
    if value is None:
        return "N/A"

    return f"{value * 100:.2f}%"


def render_company_statistics_card(stats: CompanyStatistics):
    
    st.subheader("📊 Key Statistics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Market Cap",
            _format_large_number(stats.market_cap),
        )

        st.metric(
            "Enterprise Value",
            _format_large_number(stats.enterprise_value),
        )

        st.metric(
            "Trailing PE",
            f"{stats.trailing_pe:.2f}" if stats.trailing_pe else "N/A",
        )

        st.metric(
            "Forward PE",
            f"{stats.forward_pe:.2f}" if stats.forward_pe else "N/A",
        )

    with col2:
        st.metric(
            "Dividend Yield",
            _format_percentage(stats.dividend_yield),
        )

        st.metric(
            "Beta",
            f"{stats.beta:.2f}" if stats.beta else "N/A",
        )

        st.metric(
            "52 Week High",
            f"₹{stats.fifty_two_week_high:,.2f}"
            if stats.fifty_two_week_high
            else "N/A",
        )

        st.metric(
            "52 Week Low",
            f"₹{stats.fifty_two_week_low:,.2f}"
            if stats.fifty_two_week_low
            else "N/A",
        )