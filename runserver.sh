#!/bin/bash

# Script to execute the command `python manage.py runserver 0.0.0.0:8000`

# Run the Django server
# docker-compose exec web python manage.py runserver 0.0.0.0:8000

docker-compose exec web bash

