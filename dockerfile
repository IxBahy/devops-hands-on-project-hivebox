FROM python:3.13.3-slim

# Update pip version
RUN pip install --upgrade pip

WORKDIR /app

# Generate a requirements.txt file from the lock file
COPY requirements.lock pyproject.toml ./

# Try to extract the dependencies from the requirements.lock file
RUN grep "^[a-zA-Z].*==" requirements.lock | sed 's/^//' > requirements.txt || echo "Failed to extract dependencies"

# Install dependencies with pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY src/ ./src/
COPY README.md .

EXPOSE 8000

ENTRYPOINT ["python", "src/main.py"]