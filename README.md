# porcigest

# create models from existing db
python3 manage.py inspectdb > models.py
## create initial migration for db
python3 manage.py migrate
## create superuser
python3 manage.py createsuperuser
