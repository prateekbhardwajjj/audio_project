# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
# (Make sure to add 'fastapi' and 'uvicorn' to your requirements.txt files)
COPY ./qwen_service/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# We will copy the actual code in via docker-compose later for easier development
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]