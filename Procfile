web: gunicorn CRUD-ARTICLE-API-main.wsgi --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate