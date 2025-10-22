from enum import Enum

from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter(prefix="/health")


class HealthStatus(str, Enum):
    """Health status of the application."""

    OK = "ok"
    ERROR = "error"


class GetHealthResponse(BaseModel):
    """Response model for healthcheck."""

    status: HealthStatus


@health_router.get("")
async def health() -> GetHealthResponse:
    """Healthcheck endpoint for the application."""
    return GetHealthResponse(status=HealthStatus.OK)
