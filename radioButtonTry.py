from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(2)

radios = driver.find_elements(By.CSS_SELECTOR, "input[class='radioButton']")

for radio in radios:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected()
        break




time.sleep(2)