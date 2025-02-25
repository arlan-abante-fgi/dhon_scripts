import shutil
import os
import time
from datetime import datetime, timedelta


def move_and_rename(source_folder, destination_folder, excel_name:str):
    # Get list of all files and directories in source folder
    contents = os.listdir(source_folder)
    
    # Iterate over each item in the source folder
    for item in contents:
        # Create full path for the item
        source_path = os.path.join(source_folder, item)

        # If the item is a file, move it to the destination folder and rename
        if os.path.isfile(source_path):
            # Example renaming: appending "_moved" to the original filename
            # new_filename = excel_name
            destination_path = os.path.join(destination_folder, excel_name)
            shutil.move(source_path, destination_path)
    
        



def main_move(excel_name:str):
    source_folder = '/home/dhon_bobis/Downloads/'
    current_date = datetime.now()

    # Calculate the date of yesterday
    yesterday_date = current_date - timedelta(days=1)

    # Format the date as YYYY-MM-DD
    yesterday_date_formatted = yesterday_date.strftime("%Y-%m-%d")

    destination_folder = f'/home/dhon_bobis/Documents/ecm-web-scraper-lazada-windows/downloads/{yesterday_date_formatted}/'
    # Check if the folder exists
    if not os.path.exists(destination_folder):
        # If it doesn't exist, create it
        os.makedirs(destination_folder)
        print("Folder created successfully")


    move_and_rename(source_folder, destination_folder, excel_name)
    return True
#main()
