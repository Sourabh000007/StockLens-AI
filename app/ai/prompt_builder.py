from app.models.ai.company_report import AICompanyReport
import json


class PromptBuilder:
    """
    Responsible for constructing prompts
    sent to the language model.
    """

    @staticmethod
    def get_output_schema() -> str:
        """
        Return the JSON schema expected from the AI.
        """

        return json.dumps(
            AICompanyReport.model_json_schema(),
            indent=2,
        )

    @staticmethod
    def format_metric(metrics) -> str:
        """
        Format a financial metric list into readable text.
        """

        if not metrics:
            return "Not Available"

        lines = []

        for metric in metrics:

            value = metric.value

            if abs(value) >= 1_000_000_000_000:
                formatted = f"{value / 1_000_000_000_000:.2f} Trillion"

            elif abs(value) >= 1_000_000_000:
                formatted = f"{value / 1_000_000_000:.2f} Billion"

            elif abs(value) >= 1_000_000:
                formatted = f"{value / 1_000_000:.2f} Million"

            else:
                formatted = f"{value:,.0f}"

            lines.append(
                f"{metric.year}: {formatted}"
            )

        return "\n".join(lines)

    @staticmethod
    def build_company_report_prompt(
        company,
        income_statement,
        balance_sheet,
        cash_flow,
        news_articles,
    ) -> str:
        """
        Build a prompt that requests a complete AI report.
        """

        schema = PromptBuilder.get_output_schema()

        return f"""
You are an experienced equity research analyst.

Analyze the company below.

Company Name:
{company.company_name}

Recent News:
{PromptBuilder.format_news(news_articles)}

Business Summary:
{company.business_summary}

Revenue:
{PromptBuilder.format_metric(income_statement.revenue)}

Operating Income:
{PromptBuilder.format_metric(income_statement.operating_income)}

Net Income:
{PromptBuilder.format_metric(income_statement.net_income)}

Total Assets:
{PromptBuilder.format_metric(balance_sheet.total_assets)}

Total Liabilities:
{PromptBuilder.format_metric(balance_sheet.total_liabilities)}

Total Equity:
{PromptBuilder.format_metric(balance_sheet.total_equity)}

Operating Cash Flow:
{PromptBuilder.format_metric(cash_flow.operating_cash_flow)}

Investing Cash Flow:
{PromptBuilder.format_metric(cash_flow.investing_cash_flow)}

Financing Cash Flow:
{PromptBuilder.format_metric(cash_flow.financing_cash_flow)}

In addition to the required report sections, provide an overall Company Health Assessment.

Company Health Score Guidelines:

- health_score must be a decimal number between 1.0 and 10.0.
- health_rating must be exactly one of:
  - Excellent
  - Strong
  - Average
  - Weak
  - Poor

The health assessment should consider:

- Business quality
- Financial strength
- Revenue and profitability trends
- Balance sheet quality
- Cash flow strength
- Growth prospects
- Competitive position
- Recent news sentiment
- Overall investment outlook

Return ONLY valid JSON.

The JSON MUST follow this schema:

{schema}

Do not include markdown.

Do not wrap the JSON in triple backticks.

Do not add explanations.
"""

    @staticmethod
    def format_news(articles) -> str:
        """
        Format news articles for the AI prompt.
        """

        if not articles:
            return "No recent news."

        lines = []

        for article in articles:

            lines.append(
                f"""
Title: {article.title}

Publisher: {article.publisher}

Summary: {article.summary}
"""
            )

        return "\n\n".join(lines)