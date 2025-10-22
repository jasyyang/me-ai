import logging

import uvicorn

from me_ai.api.app import fastapi_app
from me_ai.config import get_application_settings
from me_ai.config.base import ApplicationEnvType

logger = logging.getLogger(__name__)


def main() -> None:
    """Main entry point for me-ai application."""
    settings = get_application_settings()

    # Enable reload for development
    should_reload = settings.app_env == ApplicationEnvType.DEV

    logger.info(f"Starting me-ai application in {settings.app_env} environment")
    uvicorn.run(
        fastapi_app,
        host=settings.api_host,
        port=settings.api_port,
        reload=should_reload,
        log_level=settings.log_level.lower(),
    )


if __name__ == "__main__":
    main()
