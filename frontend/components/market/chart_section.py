import streamlit as st


def render_chart(figure):
    st.subheader("📈 Price History")

    st.plotly_chart(
        figure,
        width="stretch",
    )