import streamlit as st


def render_ai_risks(
    risks: list[str],
):
    """
    Render AI-identified company risks.
    """

    st.markdown("### Key Risks")

    for risk in risks:
        st.warning(f"• {risk}")

    st.divider()