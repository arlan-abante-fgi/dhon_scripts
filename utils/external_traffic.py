import pyautogui, pyperclip, time
from utils.move_files import main_move
from datetime import datetime


def external_traffic(brand:str, sa_start_date:str, sa_end_date:str):

    time.sleep(2)
    # Go to Sponsored Services in New tab
    pyautogui.hotkey('ctrl', 't')

    date_range = f'https://sellercenter.lazada.com.ph/sponsor/solutions/traffic/campaign/report/export?beginDate={sa_start_date}&&endDate={sa_end_date}'
   
    time.sleep(5)
    pyperclip.copy(date_range)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
    
    scrape_type = 'external_traffic'
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    excel_name = sa_end_date.replace('/', '-') + '_' + brand + '_' + current_datetime + '_' + scrape_type + '.xlsx'

    s = main_move(excel_name)

    if s == True:
        pass
    else:
        print(f"Something went wrong {brand} in {scrape_type} External Traffic")
        exit()

    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')


    



