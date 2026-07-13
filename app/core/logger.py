import sys

from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "{message}",
    level="INFO",
)

logger.add(
    "stocklens.log",
    rotation="5 MB",
    retention="7 days",
    level="DEBUG",
)

__all__ = ["logger"]