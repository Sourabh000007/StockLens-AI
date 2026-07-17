class PromptBuilder:
    """
    Responsible for constructing prompts
    sent to the language model.
    """

    @staticmethod
    def build_company_summary_prompt(
        company_name: str,
        business_summary: str) -> str:

        return f"""

    You are a professional equity research analyst.

    Company:
    {company_name}

    Business Description:
    {business_summary}

    Write a concise summary in simple language.

    Keep it under 120 words.
    """
    
    @staticmethod
    def build_financial_health_prompt(
        company_name: str,
        revenue: list,
        operating_income: list,
        net_income: list,
        operating_cash_flow: list) -> str:
        """
        Build a prompt for financial health analysis.
        """

        return f"""
    You are an experienced equity research analyst.

    Analyze the following financial information for {company_name}.

    Revenue:
    {revenue}

    Operating Income:
    {operating_income}

    Net Income:
    {net_income}

    Operating Cash Flow:
    {operating_cash_flow}

    Write a concise financial health assessment.

    Mention:
    - Revenue trend
    - Profitability
    - Cash generation
    - Overall financial health

    Keep it under 180 words.
    """