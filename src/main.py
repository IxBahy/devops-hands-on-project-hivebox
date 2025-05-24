import uvicorn
from fastapi import FastAPI
from typing import Dict

app = FastAPI(
    title="HiveBox API",
    description="A FastAPI application for the HiveBox DevOps project",
    version="0.1.0",
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


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
