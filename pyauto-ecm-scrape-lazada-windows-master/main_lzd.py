import argparse
import pyautogui
import time
import pyperclip
import re
from utils.move_file import move_rename
import datetime
from utils.login import login_laz
from utils.sponsored_soln import sponsor_soln

from utils.sponsored_media import sponsor_media
from utils.new_product import npl
import json
from utils.external_traffic import external_traffic
from utils.sponsored_affiliate import sponsored_affiliate

from utils.move_to_data import move_to_data


def login(username:str, password:str, brand:str, start_date:str, end_date:str,
          sm_start_date:str, sm_end_date:str, sa_start_date:str, sa_end_date:str):

    
    #Login to Lazada
    login_laz(username, password)
    # Run the sponsored soln script

    sponsor_soln(brand, start_date, end_date)         

    #New Product Launcher
    npl(brand, start_date, end_date, sm_start_date, sm_end_date)

    # External Traffic
    external_traffic(brand, sa_start_date, sa_end_date)

    # if brand != 'Oster':
    #     # Sponsored Affiliate
    sponsored_affiliate(brand, sm_start_date, sm_end_date, start_date, end_date)

    #Run the sponsored media script
    sponsor_media(brand, sm_start_date, sm_end_date, start_date, end_date)    

    time.sleep(1.5)
    pyautogui.hotkey('ctrl', 'w', interval=0.25)




########### Main Script ###########
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Lazada Web Scraping')
    parser.add_argument('--start_date', type=str, help='Start date considered (yyyy-mm-dd)')
    parser.add_argument('--end_date', type=str, help='End date considered (yyyy-mm-dd)')

    args = parser.parse_args()

    time.sleep(3)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    with open("login_creds.json", "r") as file:
    #with open("test.json", "r") as file:
        login_creds = json.load(file)


    for login_cred in login_creds:

        # Login to new lazada app

        start_date = args.start_date
        end_date = args.end_date

        #Sponsored Media
        sm_start_date = args.start_date
        sm_end_date = args.end_date

        #Sponsored Affiliate
        sa_start_date = args.start_date.replace('-', '')
        sa_end_date = args.end_date.replace('-', '')
        # sa_start_date = '20231109'
        # sa_end_date = '20231116'

        #Timing of the script
        start_time = time.time()

        login(login_cred['username'], login_cred['password'], login_cred['brand'], start_date, end_date, sm_start_date, sm_end_date, sa_start_date, sa_end_date)
        print(f"Finished processing {login_cred['brand']}")
        
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Script execution time: {execution_time} for {login_cred['brand']} in seconds")
        time.sleep(30)
    

    ## Upload to GCS
    from upload_to_google_cloud_storage import upload_folder_to_gcs
    local_folder_path = "downloads"
    bucket_name = "fgi-ecm-web-scraping"
    destination_folder = "LAZ"

    upload_folder_to_gcs(local_folder_path, bucket_name, destination_folder)
    #main_gcs()
