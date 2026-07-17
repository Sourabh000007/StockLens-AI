from app.ai.groq_client import GroqClient
from app.ai.prompt_builder import PromptBuilder

from app.models.company import Company


class AIInsightService:
    """
    Business logic for AI-generated insights.
    """

    def __init__(self):

        self.client = GroqClient()

    def generate_company_summary(self,company: Company,) -> str:
        
        """
        Generate an AI-written company summary.
        """

        prompt = PromptBuilder.build_company_summary_prompt(
            company_name=company.company_name,
            business_summary=company.business_summary,
        )

        return self.client.generate(prompt)
    
    def generate_financial_health(self,company,income_statement,cash_flow,) -> str:
        """
        Generate AI financial health analysis.
        """

        prompt = PromptBuilder.build_financial_health_prompt(
            company_name=company.company_name,
            revenue=income_statement.revenue,
            operating_income=income_statement.operating_income,
            net_income=income_statement.net_income,
            operating_cash_flow=cash_flow.operating_cash_flow,
        )

        return self.client.generate(prompt)