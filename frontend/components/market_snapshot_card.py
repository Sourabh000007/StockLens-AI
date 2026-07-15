import streamlit as st

from app.models.market_snapshot import MarketSnapshot


def render_market_snapshot(snapshot: MarketSnapshot):
    """
    Render the latest market snapshot.
    """

    st.subheader("📊 Market Snapshot")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Current Price",
            value=f"{snapshot.currency} {snapshot.current_price:,.2f}",
        )

        st.metric(
            label="Day High",
            value=f"{snapshot.currency} {snapshot.day_high:,.2f}",
        )

    with col2:
        st.metric(
            label="Previous Close",
            value=f"{snapshot.currency} {snapshot.previous_close:,.2f}",
        )

        st.metric(
            label="Day Low",
            value=f"{snapshot.currency} {snapshot.day_low:,.2f}",
        )

    with col3:
        st.metric(
            label="Market Cap",
            value=f"{snapshot.market_cap:,.0f}",
        )

        st.metric(
            label="Volume",
            value=f"{snapshot.volume:,}",
        )

    st.divider()