from enum import Enum
from typing import Annotated

from pydantic import Field
from pydantic_settings import BaseSettings


class ApplicationEnvType(Enum):
    TEST = "test"
    DEV = "dev"
    PROD = "prod"


class ApplicationSettings(BaseSettings):
    """
    Pydantic settings for main application.

    Use `get_application_settings()` to get the environment-specific settings.
    """

    app_name: Annotated[str, Field(alias="APP_NAME")] = "me-ai"
    """The name of the application."""

    app_env: Annotated[ApplicationEnvType, Field(alias="APP_ENV")] = ApplicationEnvType.DEV
    """The environment type of the application's runtime."""

    log_level: Annotated[str, Field(alias="LOG_LEVEL")] = "INFO"
    """The level of logging to use."""

    api_host: Annotated[str, Field(alias="API_HOST")] = "0.0.0.0"
    """The host to bind the API to."""

    api_port: Annotated[int, Field(alias="API_PORT")] = 8000
    """The port to bind the API to."""
