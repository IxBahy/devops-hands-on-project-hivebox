import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the FastAPI app
from src.main import app
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    """
    Create a test client for FastAPI application
    """
    return TestClient(app)
