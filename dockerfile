#1. base image 
FROM python:3.11-slim

#2. set working directory
WORKDIR /app

#3. Install dependencies
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

#4. Copy application and fastapi app
COPY app/ ./app

#5. Expose port 
EXPOSE 8000

#6. Run application 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]