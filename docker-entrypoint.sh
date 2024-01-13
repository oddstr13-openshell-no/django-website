#!/bin/bash
WEBSITE_CONFIG=/website/website/settings

if [ ! -d "${WEBSITE_CONFIG}" ]; then
  echo "The path ${WEBSITE_CONFIG} must exist and be a directory!" > /dev/stderr
  exit 1
fi

if [ ! -f "${WEBSITE_CONFIG}/__init__.py" ]; then
  echo "from .settings import *" > "${WEBSITE_CONFIG}/__init__.py"
fi

if [ ! -f "${WEBSITE_CONFIG}/settings.py" ]; then
  cp website/settings.example.py "${WEBSITE_CONFIG}/settings.py"
fi

# Clear stale (missing) thumbnail files
python ./manage.py thumbnail cleanup
python ./manage.py migrate --noinput --no-initial-data
python manage.py collectstatic --noinput

python ./manage.py validate
echo "Starting Django..."
# TODO: replace with proper reverse proxy
python ./manage.py runserver --verbosity=3 --traceback --insecure 0.0.0.0:8000