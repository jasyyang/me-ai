from typing import Annotated

from pydantic import Field

from me_ai.config.base import ApplicationEnvType, ApplicationSettings


class DevelopmentApplicationSettings(ApplicationSettings):
    """ApplicationSettings for development environment."""

    app_env: Annotated[ApplicationEnvType, Field(alias="APP_ENV")] = ApplicationEnvType.DEV
    """The environment type of the application's runtime."""
