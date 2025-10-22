from typing import Annotated

from pydantic import Field

from me_ai.config.base import ApplicationEnvType, ApplicationSettings


class TestApplicationSettings(ApplicationSettings):
    """ApplicationSettings for test environment."""

    app_env: Annotated[ApplicationEnvType, Field(alias="APP_ENV")] = ApplicationEnvType.TEST
    """The environment type of the application's runtime."""
