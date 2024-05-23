#!/bin/bash
echo "Building db"
docker-compose build db

if [[ "$1" == "-rpi" ]]; then
    echo "Building for Raspberry Pi."
    docker-compose build django-rpi 
    docker-compose build notifier-rpi
else
    echo "Building for non-Raspberry Pi environment."
    docker-compose build django
    docker-compose build notifier
fi
