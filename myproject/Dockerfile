# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev netcat gcc curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy Django project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run the Django app
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
