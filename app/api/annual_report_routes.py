from fastapi import APIRouter, Depends

from app.dependencies import get_annual_report_chat_service
from app.models.rag import (
    ChatRequest,
    ChatResponse,
)
from app.services.annual_report_chat_service import (
    AnnualReportChatService,
)

router = APIRouter(
    prefix="/annual-report",
    tags=["Annual Report"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat_with_annual_report(
    request: ChatRequest,
    service: AnnualReportChatService = Depends(
        get_annual_report_chat_service,
    ),
) -> ChatResponse:
    """
    Answer questions using an indexed annual report.
    """

    result = service.ask(
        company=request.company,
        report_year=request.report_year,
        question=request.question,
    )

    return ChatResponse(
        answer=result.answer,
        sources=result.sources,
    )