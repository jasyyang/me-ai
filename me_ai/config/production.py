from typing import Annotated

from pydantic import Field

from me_ai.config.base import ApplicationEnvType, ApplicationSettings


class ProductionApplicationSettings(ApplicationSettings):
    """ApplicationSettings for production environment."""

    app_env: Annotated[ApplicationEnvType, Field(alias="APP_ENV")] = ApplicationEnvType.PROD
    """The environment type of the application's runtime."""
