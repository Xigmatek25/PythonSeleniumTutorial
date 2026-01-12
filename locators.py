import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("password123")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.XPATH, "//label[@for='inlineRadio1']").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute = 'value']

driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Xigmatek")
driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(message)

assert "Success" in message

#CSSSelector - "tagname[attribute = 'value']"

#Xpath - "//tagname[@attribute = 'value']"



time.sleep(2)
