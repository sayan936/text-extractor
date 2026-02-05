FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies (needed for pdfplumber)
RUN apt-get update && apt-get install -y \
    gcc \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI (module path corrected to match WORKDIR)
ENV PORT=8080
CMD uvicorn main:app --host 0.0.0.0 --port $PORT