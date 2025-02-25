import shutil
import os
import time
from datetime import datetime, timedelta


def move_and_rename(source_folder, destination_folder, rename_file):
    # Get list of all files and directories in source folder
    contents = os.listdir(source_folder)
    
    # Iterate over each item in the source folder
    for item in contents:
        # Create full path for the item
        source_path = os.path.join(source_folder, item)
        # print(source_folder)
        # If the item is a file, move it to the destination folder and rename
        if os.path.isfile(source_path):
            # Example renaming: appending "_moved" to the original filename
            new_filename =  rename_file + os.path.splitext(item)[0]  + os.path.splitext(item)[1]
            destination_path = os.path.join(destination_folder, new_filename)
            shutil.move(source_path, destination_path)
        



def main_move(download_folder, rename_file):
    # source_folder = '/home/dhon_bobis/Downloads/'
    source_folder = download_folder
    current_date = datetime.now()

    # Calculate the date of yesterday
    yesterday_date = current_date - timedelta(days=1)

    # Format the date as YYYY-MM-DD
    yesterday_date_formatted = yesterday_date.strftime("%Y-%m-%d")
    destination_folder = f'/home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/downloads/{yesterday_date_formatted}'
    #destination_folder = f'{source_folder}{yesterday_date_formatted}'
    # Check if the folder exists
    if not os.path.exists(destination_folder):
        # If it doesn't exist, create it
        os.makedirs(destination_folder)
        print("Folder created successfully")


    move_and_rename(source_folder, destination_folder, rename_file)

# main_move('/Users/dhon.bobis/Documents/Sprint 33/ecm-shoppee/downloads/', 'Search_Ads_Keywords_')

