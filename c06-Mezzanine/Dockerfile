FROM python:3.11-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update &&  \
    apt-get upgrade -y &&  \
    apt-get install -y --no-install-recommends build-essential &&  \
    apt-get autoremove -y &&  \
    rm -rf /var/lib/apt/lists/*

# Create the mezzanine project
RUN python -m pip install --upgrade pip && \
    python -m pip install --upgrade wheel && \
    python -m pip install --upgrade mezzanine && \
    mezzanine-project myproject

WORKDIR /app/myproject

# Configure Django settings
RUN sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = ["*"]/' myproject/settings.py && \
    RUN python manage.py migrate && \
    echo "from django.contrib.auth.models import User; \
User.objects.create_superuser('admin', 'admin@example.com', 'P@ssw0rd!')" \
| python manage.py shell

# Expose port
EXPOSE 8000

# Default command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
