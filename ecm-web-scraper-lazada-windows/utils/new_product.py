import pyautogui, pyperclip, time
from datetime import datetime
from utils.move_files import main_move


def npl(brand:str, sm_start_date:str, sm_end_date:str, start_date:str, end_date:str):
    
    new_product_launcher = f'https://sellercenter.lazada.com.ph/sponsor/solutions/performance/report/product/export.json?&useRtTable=0&startDate={sm_start_date}&endDate={sm_end_date}&pageNo=1&pageSize=100000&adgroupName=&campaignName=&sceneId=10020'
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyperclip.copy(new_product_launcher)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(3)

        ## Move and rename the excel file to the folder
    scrape_type = 'new_product_launcher'
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
    
    










    

    
