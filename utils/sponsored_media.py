import pyautogui, pyperclip, time
from utils.move_files import main_move
from datetime import datetime


def sponsor_media(brand:str, sm_start_date:str, sm_end_date:str, start_date:str, end_date:str):

    time.sleep(2)
    # Go to Sponsored Services in New tab
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy('https://sellercenter.lazada.com.ph/sponsor/solutions/ads/report/?spm=a2a3k.asa_myaccount_home.0.dsponsor_report.729748b15vvv9t')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(8)


    #Find Sponsored Media
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.5)
    pyperclip.copy('Sponsored Media')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('esc')



    #Click Sponsored Media
    pyautogui.press('left')
    time.sleep(4)

    #Find Duration
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Duration')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('esc')


    #Select Date range
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyperclip.copy(sm_start_date)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    pyautogui.press('tab')
    time.sleep(1)
    pyperclip.copy(sm_end_date)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')

    #Find Download Button
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Download')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    scrape_type = 'sponsored_media'
    current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    excel_name = end_date.replace('/', '-') + '_' + brand + '_' + current_datetime + '_' + scrape_type + '.xlsx'

    s = main_move(excel_name)

    if s == True:
        pass
    else:
        print(f"Something went wrong {brand} in {scrape_type} SM")
        exit()

    time.sleep(2)
    pyautogui.hotkey('ctrl', 'w')


    



