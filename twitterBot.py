from Utilities.Webdriver import init_driver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Initialize Chrome WebDriver
driver = init_driver()

# Twitter login credentials
username = 'YourTwitterEmail'
password = 'YourTwitterPassword'

# URL of the Twitter login page
url = "https://twitter.com/login"
# Open Twitter login page
driver.get(url)
time.sleep(2)

username = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username.send_keys(username)
time.sleep(2)
username.send_keys(Keys.ENTER)

time.sleep(3)

password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password.send_keys(password)
time.sleep(2)
password.send_keys(Keys.ENTER)
time.sleep(3)
time.sleep(10)
