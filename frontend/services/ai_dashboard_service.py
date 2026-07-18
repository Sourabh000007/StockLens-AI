from app.models.company import Company
from app.services.ai_insight_service import AIInsightService
from app.models.ai.company_report import AICompanyReport

class AIDashboardService:
    """
    Frontend service responsible for AI features.
    """

    def __init__(self):
        self.ai_service = AIInsightService()
    
    
    def get_company_report(self,company,income_statement,balance_sheet,cash_flow) -> AICompanyReport:
        """
        Generate the complete AI company report.
        """

        return self.ai_service.generate_company_report(
            company=company,
            income_statement=income_statement,
            balance_sheet=balance_sheet,
            cash_flow=cash_flow,
        )