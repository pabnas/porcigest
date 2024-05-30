#!/bin/bash

# Set default values for flags
RPI=false
NOTIFIER=true

# Function to print usage instructions
print_usage() {
    echo "Usage: $0 [-rpi] [-notify_off]"
    echo "  -rpi          Run for Raspberry Pi environment with notifier"
    echo "  -notify_off   Run for Raspberry Pi environment without notifier"
}

# Parse command line options
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -rpi)
            RPI=true
            shift
            ;;
        -notify_off)
            NOTIFIER=false
            shift
            ;;
        -h|--help)
            print_usage
            exit 0
            ;;
        *)
            echo "Error: Invalid option $1"
            print_usage
            exit 1
            ;;
    esac
done

# Determine which containers to run
containers="db django "
if [[ $NOTIFIER == false ]]; then
    containers=${containers// notifier/}
else
    containers+="notifier "
fi

if [[ $RPI == true ]]; then
    for word in $containers; do
        if [ "$word" != "db" ]; then
            word="$word-rpi"
        fi
        new_containers="$new_containers $word"
    done
    containers=$new_containers
fi

# Run docker-compose with specified containers
echo "Running containers: $containers"
docker-compose up $containers
