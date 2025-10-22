from me_ai.config import ApplicationEnvType
from me_ai.config.base import ApplicationSettings


class ProductionApplicationSettings(ApplicationSettings):
    """ApplicationSettings for production environment."""

    def app_env(self) -> ApplicationEnvType:
        return ApplicationEnvType.PROD
