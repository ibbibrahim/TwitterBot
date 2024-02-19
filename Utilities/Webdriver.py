import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def init_driver() -> webdriver:
    current_directory = os.getcwd()
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_argument('--disable- notifications')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument(f'--user-data-dir={current_directory}\\Chrome Profile\\')
    chrome_options.add_experimental_option("prefs", prefs)
    # chrome_options.add_argument("--headless")
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.maximize_window()
        return driver
    except WebDriverException:
        print('Chrome already running!')
        print('Please close the previous chrome window and restart!')
        exit(1)
    return None