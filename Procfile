# This is the WSGI setting for Gunicorn. Make sure 'opmconsultdb.wgsi' is the path to your wsgi.py in dot form, i.e. '/' replaced by '.'
web: gunicorn opmconsultdb.wsgi:application

# This runs commands during deploy: make migrations, migrate db
release: python manage.py makemigrations; python manage.py migrate --noinput; python manage.py loaddata practiceareas.json; python manage.py loaddata specializations.json; python manage.py loaddata skills.json; 