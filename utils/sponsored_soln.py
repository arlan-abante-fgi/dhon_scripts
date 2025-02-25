import pyautogui, pyperclip, time
from datetime import datetime, timedelta
import wget
import time
from utils.move_files import main_move

def sponsor_soln(brand:str, start_date:str, end_date:str, download_directory:str):

    sponsored_solutions = f'https://sellercenter.lazada.com.ph/sponsor/solutions/performance/report/campaign/export.json?sort=&order=&useRtTable=0&startDate={start_date}&endDate={end_date}&pageNo=1&pageSize=100000&productType=&campaignType=&campaignName=&clickToConversion=30'
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyperclip.copy(sponsored_solutions)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)

    ## Move and rename the excel file to the folder
    scrape_type = 'sponsored_solutions'
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    excel_name = end_date.replace('/', '-') + '_' + brand + '_' + current_datetime + '_' + scrape_type + '.xlsx'
    
    s = main_move(excel_name)
    if s == True:
        pass
    else:
        print(f"Something went wrong {brand} in {scrape_type}")
        exit()

    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(3)





    


