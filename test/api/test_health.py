from fastapi.testclient import TestClient

from me_ai.api.routers.health import GetHealthResponse, HealthStatus


def test_health(test_client: TestClient) -> None:
    """Test that the healthcheck endpoint returns a 200 OK."""
    response = test_client.get("/health")
    health_response = GetHealthResponse.model_validate(response.json())
    assert response.status_code == 200
    assert health_response.status == HealthStatus.OK
