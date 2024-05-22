# porcigest

# create models from existing db
python3 manage.py inspectdb > models.py
## create initial migration for db
python3 manage.py migrate
## create superuser
python3 manage.py createsuperuser

## create veterinario and administrador permissions
python3 manage.py create_veterinario
python3 manage.py create_administrador
