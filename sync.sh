#!/bin/bash

echo "syncing..."
cd ..
rsync -avh --exclude='data' porcigest/ rpi:/home/pi/porcigest
