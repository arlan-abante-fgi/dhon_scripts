import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pyautogui
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from move_campaign import main_move


def refresh_dwnld():
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Refresh')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')

def continue_after_yes():
    x = input("Waiting for credentials to be entered. Enter YES when done: ")
    if x == 'YES':
        pass

def on_product(driver):
    driver.get('https://brandportal.shopee.com/seller/mkt/my-ads-report/product')
    time.sleep(3)


    date_picker = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/div/div/div/div/div[2]""")
    date_picker.click()
    time.sleep(2)
    yesterday = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/ul/li[1]/span""")
    yesterday.click()

    time.sleep(2)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[2]""")
    btn_refresh.click()
    time.sleep(2)

    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[3]""")
    btn_dwnload.click()
    time.sleep(2)



def on_overall_perf(driver):
    #download_directory = "//dhon.bobis/Documents/Sprint 33/ecm-shoppee/downloads/"
    download_directory ="/home/dhon_bobis/Downloads/"

    driver.get('https://brandportal.shopee.com/seller/mkt/my-ads-report/overall')
    time.sleep(3)


    ##### SEARCH ADS KEYWORDS
    exclude_boost_select = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/div/div/div/div""")
    exclude_boost_select.click()

    
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Clear')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)

    #Clicks the button for Search_Ads_Keywords
    button_search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div/div[1]/span[3]/span")))
    button_search.click()

    time.sleep(2)

    date_picker = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/div/div/div/div/div[2]""")
    date_picker.click()
    
    time.sleep(2)
    yesterday = driver.find_element(By.XPATH, """/html/body/div[3]/div/div/div/div[2]/div/div/ul/li[1]""")
    yesterday.click()

    time.sleep(2)
    
    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[2]""")
    btn_refresh.click()
    time.sleep(2)

    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[3]""")
    btn_dwnload.click()

    time.sleep(2)

    main_move(download_directory, "Search_Ads_Keywords_")

    ### Search Ad Shop_Ads
    time.sleep(60)
    exclude_boost_select = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/div/div/div/div""")
    exclude_boost_select.click()

    
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Clear')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)

    button_search_keywords = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div/div[2]/span[3]/span")))
    button_search_keywords.click()

    time.sleep(2)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[2]""")
    btn_refresh.click()
    time.sleep(2)


    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[3]""")
    btn_dwnload.click()

    time.sleep(2)
    main_move(download_directory, "Search_Ads_Shop_")



    ### Discovery Ads
    time.sleep(60)
    exclude_boost_select = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/div/div/div/div""")
    exclude_boost_select.click()

    
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Clear')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)

    
    button_search_keywords = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div/div[3]/span[3]/span")))
    button_search_keywords.click()

    time.sleep(2)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[2]""")
    btn_refresh.click()
    time.sleep(2)


    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[3]""")
    btn_dwnload.click()

    time.sleep(2)
    main_move(download_directory, "Discovery_Ads_")

    ### Boost Ads
    time.sleep(60)
    exclude_boost_select = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[3]/div/div/div/div/div""")
    exclude_boost_select.click()

    
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'f')
    pyperclip.copy('Clear')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(3)

    
    button_search_keywords = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[3]/div/div/div/div[4]/span[3]/span")))
    button_search_keywords.click()

    time.sleep(2)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[2]""")
    btn_refresh.click()
    time.sleep(2)


    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[4]/div/button[3]""")
    btn_dwnload.click()

    time.sleep(2)
    main_move(download_directory, "Boost_Ads_")
    time.sleep(5)

def product_performance(driver):
    driver.get('https://brandportal.shopee.com/seller/mkt/traffic/product')
    time.sleep(3)

    date_picker = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/div/div/div/div/div[2]/span""")
    date_picker.click()
    time.sleep(3)

    
    yesterday = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/ul/li[1]""")
    yesterday.click()
    time.sleep(3)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[7]/div/button[2]""")
    btn_refresh.click()
    time.sleep(3)

    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[7]/div/button[3]""")
    btn_dwnload.click()
    time.sleep(8)


def overall_perf(driver):
    driver.get('https://brandportal.shopee.com/seller/mkt/traffic/overall')
    time.sleep(3)

    date_picker = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/form/div/div[2]/div/div/div/div/div/div""")
    date_picker.click()
    time.sleep(3)

    yesterday = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/ul/li[1]/span""")
    yesterday.click()
    time.sleep(3)

    btn_refresh = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/form/div/div[5]/div/button[2]""")
    btn_refresh.click()
    time.sleep(3)

    btn_dwnload = driver.find_element(By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div[2]/div/form/div/div[5]/div/button[3]""")
    btn_dwnload.click()
    time.sleep(8)

def marketing_campaign(driver):
    # Marketing Campaign
    driver.get('https://brandportal.shopee.com/seller/mkt/traffic/campaign')
    time.sleep(3)
     
    date_picker = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "src-components_v1-DatePicker---dateText--3nbzL")))
    date_picker.click()
    
    time.sleep(1)
    yesterday = driver.find_element(By.XPATH, """/html/body/div[2]/div/div/div/div[2]/div/div/ul/li[1]""")
    yesterday.click()
    time.sleep(3)

    refresh_dwnld()
    
    #Click the download button
    btn_dwnload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="app"]/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div[2]/div/form/div/div[7]/div/button[3]""")))
    btn_dwnload.click()
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(8)

def login(driver):
    driver.get('https://brandportal.shopee.com/seller/login')  
    
    # Perform manual login actions...
    time.sleep(2)
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")

    email.send_keys('joey.rodriguez@focusglobalinc.com')
    password.send_keys('Focus2021!')
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)

def change_principal(driver, principal_name):
    
    # Change principal
    driver.get('https://brandportal.shopee.com/seller/post-login')
    time.sleep(3)
    for i in range(0,5):
        pyautogui.hotkey('ctrl', '-')
        time.sleep(0.5)
    time.sleep(3)
    btn_expand = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopee-react-select__inner.line-clamp--1")))
    btn_expand.click()

    time.sleep(2)
    
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopee-react-input__input")))
    search_box.send_keys(principal_name)

    time.sleep(2)
    # continue_after_yes()
    results_box = driver.find_element(By.XPATH, """//*[@id="app"]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]""")
    # results_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopee-react-select-option shopee-react-select-option-selected")))
    results_box.click()
    time.sleep(1)

    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')

    time.sleep(10)

    on_overall_perf(driver)
    marketing_campaign(driver)
    overall_perf(driver)
    product_performance(driver)
    on_product(driver)

if __name__ == "__main__":
    
    #directory = '/ download_directory ="Users/dhon.bobis/Documents/Sprint 33/automate-browser-pyautogui/downloads'
    directory = '/home/dhon_bobis/Downloads/'
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an Excel file
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Remove the file
            os.remove(file_path)

    directory = '/home/dhon_bobis/Documents/ecm-web-scraper-shopee-main/downloads/'
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is an Excel file
        if filename.endswith('.xlsx') or filename.endswith('.xls'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Remove the file
            os.remove(file_path)

    driver = webdriver.Chrome()
   # options = Options()
   # options.add_experimental_option("prefs", {
   # "download.default_directory": r"/Users/dhon.bobis/Documents/Sprint 33/ecm-shoppee/downloads/"
   # })
   # driver = webdriver.Chrome(options=options)

    login(driver)
    
    brands = ["Focus Global",
    "Instant Pot",
    "KitchenAid",
    "Levoit",
    "Philips PH",
    "Tempur Philippines"
    ]
    
    for brand in brands:    
        change_principal(driver, brand)


    from move_files import move_files_main
    move_files_main()

    from transform_campaign import transform_data
    transform_data()

    from upload_to_google_cloud_storage import upload_shp_gcs
    upload_shp_gcs()


