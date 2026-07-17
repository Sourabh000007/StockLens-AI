from app.models.company import Company
from app.services.ai_insight_service import AIInsightService


class AIDashboardService:
    """
    Frontend service responsible for AI features.
    """

    def __init__(self):
        self.ai_service = AIInsightService()
    
    def get_company_summary(self,company: Company,) -> str:
        
        """
        Generate an AI company summary.
        """

        return self.ai_service.generate_company_summary(
            company,
        )
    
    def get_financial_health(self,company,income_statement,cash_flow,) -> str:
        """
        Generate AI financial health analysis.
        """

        return self.ai_service.generate_financial_health(
            company,
            income_statement,
            cash_flow,
        )