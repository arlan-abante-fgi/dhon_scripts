import pyautogui, pyperclip, time


def login_laz(username:str, password:str):
    #pyautogui.hotkey('alt', 'tab')
    time.sleep(2)
    #Waiting time before the script starts / must move towards the chrome
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyperclip.copy('https://sellercenter.lazada.com.ph/apps/seller/login')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(3)


    #Enter the credentials
    # pyautogui.moveTo(937, 447)
    # pyautogui.click()  
    # time.sleep(2)   
    # pyautogui.moveTo(888, 841)
    for i in range(0,5):
        pyautogui.hotkey('ctrl', '-')
        time.sleep(0.5)
    time.sleep(1)
    for i in range(0,3):
        pyautogui.press('tab')
        time.sleep(0.5)
    
    pyperclip.copy(username)
    print(username)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyperclip.copy(password)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
