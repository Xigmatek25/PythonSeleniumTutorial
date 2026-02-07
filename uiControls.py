
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

hideExample = driver.find_element(By.ID, "displayed-text")

driver.find_element(By.ID, "hide-textbox").click()

"""This should return error since field was hide on previous line/command"""
assert hideExample.is_displayed()






time.sleep(2)

