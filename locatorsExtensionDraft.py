import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/#/auth/login")

driver.find_element(By.CLASS_NAME, "forgot-password-link").click()


time.sleep(10)
