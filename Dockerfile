# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy application files
COPY app.py requirements.txt ./

# Install dependencies (none for now)
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["python", "app.py"]
