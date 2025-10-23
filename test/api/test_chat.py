import pytest
from fastapi.testclient import TestClient


@pytest.mark.skip(reason="TODO")
def test_start_chat(test_client: TestClient) -> None:
    raise NotImplementedError


@pytest.mark.skip(reason="TODO")
def test_open_chat_stream(test_client: TestClient) -> None:
    raise NotImplementedError
