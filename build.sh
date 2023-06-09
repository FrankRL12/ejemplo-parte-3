#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt


python manage.py collectstatic --no-input
python manage.py migrate

# Variables de entorno para el superusuario
SUPERUSER_USERNAME="admin3"
SUPERUSER_EMAIL="Adolfo95lopez95@gmail.com"
SUPERUSER_PASSWORD="1234567"

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$SUPERUSER_USERNAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD')" | python manage.py shell