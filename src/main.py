import uvicorn
from fastapi import FastAPI
from typing import Dict
from contextlib import asynccontextmanager
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="HiveBox API",
    description="A FastAPI application for the HiveBox DevOps project",
    version="0.0.1",
)


@app.get("/")
def read_root() -> Dict[str, str]:
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to HiveBox API"}


@app.get("/health")
def health_check() -> Dict[str, str]:
    """
    Health check endpoint.
    """
    return {"status": "healthy"}


instrumentator = Instrumentator().instrument(app)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handle application startup and shutdown events.
    Start the metrics collection on application startup.
    """
    # Expose metrics endpoint on startup
    instrumentator.expose(app, endpoint="/metrics")
    yield
    # Cleanup could go here if needed


# Set lifespan handler
app.router.lifespan_context = lifespan


if __name__ == "__main__":
    # Run with the app directly
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
