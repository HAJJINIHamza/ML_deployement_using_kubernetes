# --------------BASE-------------------
#1. base image 
FROM python:3.11-slim AS base
#2. set working directory
WORKDIR /app
#3. Install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# --------------Test-------------------
#Inherit from base image
FROM base AS test
#Install dev dependencies
COPY requirements-dev.txt . 
RUN pip install --no-cache-dir -r requirements-dev.txt
#Test application
COPY app/ ./app
COPY tests/ ./tests
CMD ["pytest", "-q", "-m", "not model"]

# --------------Production-------------
FROM base AS runtime
#Copy application and fastapi app
COPY app/ ./app
#Expose port 
EXPOSE 8000
#Run application 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]