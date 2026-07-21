import streamlit as st

from app.models.market_snapshot import MarketSnapshot
from frontend.utils.formatters import format_large_number


def render_market_snapshot(snapshot: MarketSnapshot):
    """
    Render the latest market snapshot.
    """

    st.subheader("📊 Market Snapshot")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Current Price",
            f"₹{snapshot.current_price:,.2f}",
        )

        st.metric(
            "Day High",
            f"₹{snapshot.day_high:,.2f}",
        )

        st.metric(
            "Market Cap",
            format_large_number(snapshot.market_cap),
        )

    with col2:

        st.metric(
            "Previous Close",
            f"₹{snapshot.previous_close:,.2f}",
        )

        st.metric(
            "Day Low",
            f"₹{snapshot.day_low:,.2f}",
        )

        st.metric(
            "Volume",
            format_large_number(snapshot.volume),
        )