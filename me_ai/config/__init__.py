import os
from collections.abc import Callable
from functools import lru_cache

from dotenv import load_dotenv

from me_ai.config.base import ApplicationEnvType, ApplicationSettings
from me_ai.config.development import DevelopmentApplicationSettings
from me_ai.config.paths import REPO_ENV_PATH
from me_ai.config.production import ProductionApplicationSettings

_ENVIRONMENTS: dict[ApplicationEnvType, type[ApplicationSettings]] = {
    ApplicationEnvType.DEV: DevelopmentApplicationSettings,
    ApplicationEnvType.PROD: ProductionApplicationSettings,
}


class UnspecifiedApplicationEnvironmentError(Exception):
    """Exception raised when the `APP_ENV` is unspecified."""

    def __init__(self) -> None:
        super().__init__("The `APP_ENV` environment variable is unspecified.")


class InvalidApplicationEnvironmentError(Exception):
    """Exception raised when the `APP_ENV` is not a valid environment."""

    def __init__(self, app_env: str) -> None:
        super().__init__(f"{app_env} is not a valid environment.")


def load_dotenv_file(
    dotenv_path: str | os.PathLike[str] | None,
    encoding: str | None = "utf-8",
) -> bool:
    """Load a .env file into the environment variables, returning boolean indicating success."""
    path = dotenv_path or REPO_ENV_PATH
    if path.exists():
        load_dotenv(path, override=False)
        return True
    return False


def _get_env_type() -> ApplicationEnvType:
    """Return the current application's environment type."""
    if not (app_env := os.getenv("APP_ENV", "").lower()):
        raise UnspecifiedApplicationEnvironmentError
    try:
        return ApplicationEnvType(app_env)
    except ValueError:
        raise InvalidApplicationEnvironmentError(app_env) from None


def make_get_application_settings[T: ApplicationSettings](
    environments: dict[ApplicationEnvType, type[T]],
    dotenv_path: str | os.PathLike[str] | None = None,
) -> Callable[[], T]:
    def get_application_settings() -> T:
        """Return the ApplicationSettings for the environment type."""
        if dotenv_path:
            load_dotenv_file(dotenv_path)

        app_env = _get_env_type()

        return environments[app_env]()

    return get_application_settings


@lru_cache
def get_application_settings() -> ApplicationSettings:
    return make_get_application_settings(_ENVIRONMENTS, REPO_ENV_PATH)()
