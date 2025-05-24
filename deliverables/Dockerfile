# Use the appropriate Python base image
FROM python:3.11  # Update this if your dependencies require a different version

# Set a non-root user for secure execution
USER appuser

# Set working directory inside the container
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies securely
RUN pip install --no-cache-dir -r requirements.txt

# Enforce strict permissions and least privilege
RUN chmod -R 755 /app

# Apply a health check to ensure Flask is running properly
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD curl -f http://localhost:5000 || exit 1

# Bind Flask service to localhost for security
CMD ["python", "-m", "flask", "run", "--host=127.0.0.1", "--port=5000"]
