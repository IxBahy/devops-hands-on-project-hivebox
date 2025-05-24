from fastapi.testclient import TestClient


def test_read_root(client: TestClient):
    """
    Test the root endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to HiveBox API"}

    # Check response headers and content type
    assert response.headers["content-type"] == "application/json"


def test_health_check(client: TestClient):
    """
    Test the health check endpoint
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

    # Check response headers and content type
    assert response.headers["content-type"] == "application/json"
