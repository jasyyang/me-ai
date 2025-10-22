import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from me_ai.api.app import create_application


@pytest.fixture
def test_app() -> FastAPI:
    """Create a test FastAPI application."""
    return create_application()


@pytest.fixture
def test_client(test_app: FastAPI) -> TestClient:
    """Create a FastAPI TestClient."""
    return TestClient(test_app)
