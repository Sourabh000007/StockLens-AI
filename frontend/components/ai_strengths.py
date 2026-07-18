import streamlit as st


def render_ai_strengths(
    strengths: list[str],
):
    """
    Render AI-identified company strengths.
    """

    st.subheader("💪 Key Strengths")

    for strength in strengths:
        st.success(f"✓ {strength}")