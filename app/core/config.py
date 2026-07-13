from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "StockLens AI"
    app_version: str = "1.0.0"

    groq_api_key: str

    embedding_model: str
    vector_db_path: Path
    report_path: Path
    cache_path: Path

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()