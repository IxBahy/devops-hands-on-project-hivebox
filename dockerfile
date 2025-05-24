FROM python:3.13.3-slim

RUN pip install --no-cache-dir --upgrade pip==24.0

WORKDIR /app

# Generate a requirements.txt file from the lock file
COPY requirements.lock pyproject.toml ./

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN grep "^[a-zA-Z].*==" requirements.lock | sed 's/^//' > requirements.txt || echo "Failed to extract dependencies"

# Install dependencies with pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY src/ ./src/
COPY README.md .

EXPOSE 8000

ENTRYPOINT ["python", "src/main.py"]