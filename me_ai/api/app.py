import logging

from fastapi import FastAPI

from me_ai.api.routers import routers
from me_ai.config import get_app_settings

logger = logging.getLogger(__name__)


def _setup_fastapi_app() -> FastAPI:
    """
    Setup and return FastAPI application with routers and middleware.
    """
    app = FastAPI(title=get_app_settings().app_name)
    for router in routers:
        app.include_router(router)
    return app


def create_application() -> FastAPI:
    """
    Create and return the API service application.
    """
    try:
        app = _setup_fastapi_app()
    except Exception:
        logger.exception("Uncaught FastAPI exception while setting", extra={"alert": True})
        raise RuntimeError("Error starting application") from None
    return app


fastapi_app: FastAPI = create_application()
