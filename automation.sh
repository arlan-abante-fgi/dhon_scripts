#!/bin/bash

# Replace 'my_env' with the name of your virtual environment
ENV_NAME=".env"
export DISPLAY=:20.0

# Activate the virtual environment
source /home/dhon_bobis/Documents/.env/bin/activate

# Optional: Display a message indicating that the environment has been activated
echo "Python virtual environment '$ENV_NAME' activated."

google-chrome &
sleep 20
python /home/dhon_bobis/Documents/ecm-web-scraper-lazada-windows/main_lzd.py
sleep 20
python /home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/main.py

