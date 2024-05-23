#!/bin/bash

if [[ "$1" == "-rpi" ]]; then
    echo "Running for Raspberry Pi environment."
    docker-compose up db django-rpi
else
    echo "Running for non-Raspberry Pi environment."
    docker-compose up db django
fi
