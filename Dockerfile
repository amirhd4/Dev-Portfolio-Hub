FROM python:3.11-slim

WORKDIR /app

# Install system dependencies that might be needed by some Python packages
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    build-essential \
#    libpq-dev \
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    || true && apt-get install -f && \
    rm -rf /var/lib/apt/lists/*


# Copy and install Python requirements
COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the Django application
COPY . .

# Expose the port Gunicorn will run on
EXPOSE 8000

# (Note: For a real production app, you'd run collectstatic here)
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio_project.wsgi"]
# For development, we can run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]