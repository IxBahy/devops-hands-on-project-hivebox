from fastapi.testclient import TestClient


def test_openapi_docs(client: TestClient):
    """
    Test that the OpenAPI documentation endpoint is accessible
    """
    response = client.get("/docs")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

    # Check that the response contains the title of our API
    assert "HiveBox API" in response.text


def test_openapi_json(client: TestClient):
    """
    Test that the OpenAPI JSON schema is accessible
    """
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"

    # Validate that the schema contains our endpoints
    schema = response.json()
    assert schema["info"]["title"] == "HiveBox API"
    assert schema["info"]["version"] == "0.0.1"

    # Check that our endpoints are defined in the schema
    assert "/health" in schema["paths"]
    assert "/" in schema["paths"]
