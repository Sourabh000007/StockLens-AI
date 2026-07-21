import streamlit as st

from app.models.ai.company_report import AICompanyReport

def render_company_health_score(
    report: AICompanyReport,
):
    st.subheader("⭐ Company Health Score")

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown(
            f"""
            <div style="text-align:center;">
                <h1 style="margin-bottom:0;">
                    {report.health_score:.1f}/10
                </h1>
                <p style="color:gray;">
                    Company Health Score
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.progress(report.health_score / 10)

    rating = report.health_rating

    if rating == "Excellent":
        emoji = "🟢"

    elif rating == "Strong":
        emoji = "🟢"

    elif rating == "Average":
        emoji = "🟡"

    elif rating == "Weak":
        emoji = "🟠"

    else:
        emoji = "🔴"

    with right:

        st.markdown("### Overall Rating")

        st.markdown(
            f"## {emoji} {rating}"
        )

        st.caption(
            "Based on company fundamentals, "
            "financial statements, "
            "recent news and AI analysis."
        )

    if report.health_score >= 8:

        st.success(
            "Strong overall business fundamentals with healthy financials."
        )

    elif report.health_score >= 6:

        st.warning(
            "Company fundamentals are stable with some areas to monitor."
        )

    else:

        st.error(
            "Business shows elevated risk and requires careful analysis."
        )