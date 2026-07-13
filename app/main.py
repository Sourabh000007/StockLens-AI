from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.company_routes import router as company_router
from app.core.config import settings
from app.core.logger import logger

from app.api.financial_routes import router as financial_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("StockLens AI started successfully.")

    yield

    logger.info("StockLens AI shutting down...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "application": settings.app_name,
        "version": settings.app_version,
        "status": "Running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
    }


app.include_router(company_router)
app.include_router(financial_router)