web: gunicorn api_app.articles_api.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate