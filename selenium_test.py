from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
import time

os.environ['PATH'] += r"/Users/antikiller/Projects/Python_projects/selenium_drivers/chromedriver_mac_arm64"
driver = webdriver.Chrome()
driver.get("http://localhost:5000/")
driver.implicitly_wait(3)

title = driver.find_element(By.ID, "title_search_id")
author = driver.find_element(By.ID, "author_search_id")

# right click
action_chains = ActionChains(driver)
action_chains.context_click(author).perform()
time.sleep(3)

# paste the text into the search fields
title.send_keys('Paradise')
author.send_keys('John')


element = driver.find_element(By.ID, "nav_search_button_id")
element.click()
time.sleep(3)

card = driver.find_element(By.CSS_SELECTOR, 'div[class="col-xl-2 col-md-3 col-sm-6"]')
card.click()
time.sleep(3)

# login_form_text = driver.find_element(By.CLASS_NAME, "text-center")
# print(f"{login_form_text.text}")

