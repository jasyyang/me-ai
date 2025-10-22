from pathlib import Path
from typing import Final

APPLICATION_PATH: Final[Path] = Path(__file__).parent.parent
"""The path to the application's root directory."""

REPO_PATH: Final[Path] = APPLICATION_PATH.parent
"""The path to the repository's root directory."""

REPO_ENV_PATH: Final[Path] = REPO_PATH / ".env"
"""The path to the repository's environment file."""

OPENAPI_SPEC_PATH: Final[Path] = APPLICATION_PATH / "openapi.json"
"""The path to the application's OpenAPI specification file."""
