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
    def build_company_report_prompt(company,income_statement,balance_sheet,cash_flow,) -> str:
        """
        Build a prompt that requests a complete AI report.
        """

        schema = PromptBuilder.get_output_schema()

        return f"""
    You are an experienced equity research analyst.

    Analyze the company below.

    Company Name:
    {company.company_name}

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
    
    Return ONLY valid JSON.

    The JSON MUST follow this schema:

    {schema}

    Do not include markdown.

    Do not wrap the JSON in triple backticks.

    Do not add explanations.
    """