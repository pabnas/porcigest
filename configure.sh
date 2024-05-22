#!/bin/bash
echo "Building db"
docker-compose build db

if [[ "$1" == "-rpi" ]]; then
    echo "Building for Raspberry Pi."
    docker-compose build django-rpi
    echo "Running for Raspberry Pi environment."
    docker-compose up db django-rpi
else
    echo "Building for non-Raspberry Pi environment."
    docker-compose build django
    echo "Running for non-Raspberry Pi environment."
    docker-compose up db django
fi
