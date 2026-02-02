
from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)
options = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(options))

for option in options:
    if option.get_attribute("value") == "option2":
        option.click()
        break

time.sleep(2)

