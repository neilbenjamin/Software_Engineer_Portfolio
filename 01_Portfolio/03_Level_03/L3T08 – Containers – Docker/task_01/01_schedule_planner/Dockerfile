# Build solution courtesy of Google.
# Please note it's not possible to test run an image built on an ARM64 
# computer on Dockerlabs. It needs to be rub on a machine with docker 
# installed i.e docker desktop.
# Use a Python base image. It's good practice to be specific with version.
# python:3.11-slim-buster is a good choice for production as it's small.
FROM python:3.11-slim-bookworm

# Set the initial directory where all run and copy commands will take place 
# relative the WORKDIR, unless a new WORKDIT is specified

WORKDIR /app

# Installs all the sytem necessary dependencies. 
# Build essential is necessarry for all C type extensions.
# libpq is important to link to PostgreSQL databases with python through
# psycopg2, 
# rm -rf /var/lib/apt/lists/* cleans the cache to reduce size
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy your requirements.txt. Docker will use the same file if no changes are
# made, eliminatingy uncessarily copying it again with the same result. 
COPY requirements.txt /app/

# Install Python dependencies without saving the donwload cache
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project source code into the container's /app directory
# The .dockerignore file will ensure unnecessary files are not copied
COPY . /app/

# Change the working directory to the *inner* schedule_planner directory
# where manage.py and your settings.py are located so that those files can be 
# accessed and run.
WORKDIR /app/schedule_planner

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=schedule_planner.settings

# Run Django migrations
RUN python manage.py migrate --noinput

# Collect static files
RUN python manage.py collectstatic --noinput

# Create port that Gunicorn (or Django's runserver) will listen on
EXPOSE 8000

# Command to run your Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "schedule_planner.wsgi:application"]