import streamlit as st


PERIOD_OPTIONS = {
    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y",
    "5 Years": "5y",
}


def render_search_bar():
    """
    Render the search controls.
    """

    col1, col2, col3 = st.columns([3, 2, 1])

    with col1:
        symbol = st.text_input(
            "Stock Symbol",
            value="TCS.NS",
        )

    with col2:
        period_label = st.selectbox(
            "Time Period",
            list(PERIOD_OPTIONS.keys()),
            index=3,   # 1 Year default
        )

    with col3:
        st.write("")
        st.write("")
        load_clicked = st.button(
            "Load",
            width="stretch",
        )

    return (
        symbol.strip().upper(),
        PERIOD_OPTIONS[period_label],
        load_clicked,
    )