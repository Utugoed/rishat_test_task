python manage.py migrate

export DJANGO_SUPERUSER_EMAIL=test@test.com
export DJANGO_SUPERUSER_USERNAME=rishat
export DJANGO_SUPERUSER_PASSWORD=V3rySt0ngP4ss

python manage.py createsuperuser --no-input
python manage.py runserver 0.0.0.0:8000