import argparse
import pyautogui
import time
import pyperclip
import re
from datetime import datetime, timedelta
from utils.login import login_laz
from utils.sponsored_soln import sponsor_soln

from utils.sponsored_media import sponsor_media
from utils.new_product import npl
import json
from utils.external_traffic import external_traffic
from utils.sponsored_affiliate import sponsored_affiliate



def login(username:str, password:str, brand:str, start_date:str, end_date:str,
          sm_start_date:str, sm_end_date:str, sa_start_date:str, sa_end_date:str):

    
    #Login to Lazada
    login_laz(username, password)
    # Run the sponsored soln script
    download_directory = './downloads/'
    sponsor_soln(brand, start_date, end_date, download_directory)         
    time.sleep(2)
    #New Product Launcher
    npl(brand, start_date, end_date, sm_start_date, sm_end_date)
    time.sleep(2)
    # External Traffic
    external_traffic(brand, sa_start_date, sa_end_date)
    time.sleep(2)
    # if brand != 'Oster':
    #     # Sponsored Affiliate
    sponsored_affiliate(brand, sm_start_date, sm_end_date, start_date, end_date)
    time.sleep(2)
    #Run the sponsored media script
    sponsor_media(brand, sm_start_date, sm_end_date, start_date, end_date)    

    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'w')




########### Main Script ###########
if __name__ == "__main__":
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    pyautogui.hotkey('alt','tab')
    time.sleep(1)
    current_date = datetime.now()

    # Calculate the date of yesterday
    yesterday_date = current_date - timedelta(days=1)

    # Format the date as YYYY-MM-DD
    yesterday_date_formatted = yesterday_date.strftime("%Y-%m-%d")

    #pyautogui.hotkey('alt', 'tab')
    #time.sleep(5)

    from delete_folder_contents import delete_files
    delete_files()

    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    with open("/home/dhon_bobis/Documents/ecm-web-scraper-lazada-windows/login_creds.json", "r") as file:
        login_creds = json.load(file)


    for login_cred in login_creds:

        # Login to new lazada app
        start_date = yesterday_date_formatted
        end_date = yesterday_date_formatted

        #Sponsored Media
        sm_start_date = yesterday_date_formatted
        sm_end_date = yesterday_date_formatted

        #Sponsored Affiliate
        sa_start_date = yesterday_date_formatted.replace('-', '')
        sa_end_date = yesterday_date_formatted.replace('-', '')

        #Timing of the script
        start_time = time.time()
        login(login_cred['username'], login_cred['password'], login_cred['brand'], start_date, end_date, sm_start_date, sm_end_date, sa_start_date, sa_end_date)
        print(f"Finished processing {login_cred['brand']}")
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Script execution time: {execution_time} for {login_cred['brand']} in seconds")

    print(f"Starting Transformation")

    from transform_campaign import transform_data
    transform_data()
    
    from upload_to_gcs import upload_lzd_gcs
    upload_lzd_gcs()
