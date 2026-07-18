from app.ai.groq_client import GroqClient
from app.ai.prompt_builder import PromptBuilder

from app.models.company import Company
from app.models.ai.company_report import AICompanyReport


class AIInsightService:
    """
    Business logic for AI-generated insights.
    """

    def __init__(self):

        self.client = GroqClient()

    
    def generate_company_report(self,company,income_statement,balance_sheet,cash_flow) -> AICompanyReport:
        """
        Generate a complete AI company report.
        """

        prompt = PromptBuilder.build_company_report_prompt(
            company=company,
            income_statement=income_statement,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )

        response = self.client.generate_json(prompt)

        return AICompanyReport.model_validate(response)
    
    def get_company_report(
        self,
        company,
        income_statement,
        balance_sheet,
        cash_flow,
    ) -> AICompanyReport:
        """
        Generate the complete AI company report.
        """

        return self.ai_service.generate_company_report(
            company=company,
            income_statement=income_statement,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )