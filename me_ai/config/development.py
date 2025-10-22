from me_ai.config import ApplicationEnvType
from me_ai.config.base import ApplicationSettings


class DevelopmentApplicationSettings(ApplicationSettings):
    """ApplicationSettings for development environment."""

    def app_env(self) -> ApplicationEnvType:
        return ApplicationEnvType.DEV
