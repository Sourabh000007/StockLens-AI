import streamlit as st

from app.models.market_snapshot import MarketSnapshot


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


def render_market_snapshot(snapshot: MarketSnapshot):
    """
    Render the latest market snapshot.
    """

    st.subheader("📊 Market Snapshot")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Current Price",
            f"{snapshot.currency} {snapshot.current_price:,.2f}",
        )

        st.metric(
            "Day High",
            f"{snapshot.currency} {snapshot.day_high:,.2f}",
        )

    with col2:

        st.metric(
            "Previous Close",
            f"{snapshot.currency} {snapshot.previous_close:,.2f}",
        )

        st.metric(
            "Day Low",
            f"{snapshot.currency} {snapshot.day_low:,.2f}",
        )

    with col3:

        st.metric(
            "Market Cap",
            _format_large_number(snapshot.market_cap),
        )

        st.metric(
            "Volume",
            f"{snapshot.volume:,}",
        )

    st.divider()