import streamlit as st


def render_search_bar():
    """
    Render the stock search section.
    """

    col1, col2 = st.columns([5, 1])

    with col1:
        symbol = st.text_input(
            "Company Symbol",
            value="TCS.NS",
            help="Example: TCS.NS, INFY.NS, RELIANCE.NS",
        )

    with col2:
        st.write("")
        st.write("")
        load_clicked = st.button(
            "Load",
            width="stretch",
        )

    return symbol.strip().upper(), load_clicked