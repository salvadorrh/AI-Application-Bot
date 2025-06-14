from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# Chrome the most popular. Install driver from: https://sites.google.com/chromium.org/driver/

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Running Selenium, testing with Google
driver.get('https://www.google.com')

input_element = driver.find_element(By.CLASS_NAME, 'gLFyf')
# input_element.send_keys("Tech with tim" + Keys.ENTER)

for char in "Tech with tim":
    val = random.uniform(0.2, 0.5)
    input_element.send_keys(char)
    time.sleep(val)

input_element.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()