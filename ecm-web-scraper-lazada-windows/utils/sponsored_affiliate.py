import pyautogui, pyperclip, time
from utils.move_files import main_move
from datetime import datetime
import wget

def sponsored_affiliate(brand:str, sm_start_date:str, sm_end_date:str, start_date:str, end_date:str):

    sponsored_affiliate = f'https://sellercenter.lazada.com.ph/sponsor/solutions/affiliate/report/metric/export.json?&startDateStr={start_date}&endDateStr={end_date}'
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyperclip.copy(sponsored_affiliate)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)

    ## Move and rename the excel file to the folder
    scrape_type = 'sponsored_affiliate'
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





    


