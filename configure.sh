#!/bin/bash

# Script to run configuration with a bash terminal

# Build the Docker image and start the container
docker-compose --env-file ./.env up --build
