#!/bin/bash

# Replace 'my_env' with the name of your virtual environment
ENV_NAME=".env"

# Activate the virtual environment
source /home/dhon_bobis/Documents/"$ENV_NAME"/bin/activate

# Optional: Display a message indicating that the environment has been activated
echo "Python virtual environment '$ENV_NAME' activated."

#google-chrome

#python /home/dhon_bobis/Documents/ecm-web-scraper-lazada-windows/main_lzd.py
#sleep 20
python /home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/main.py

