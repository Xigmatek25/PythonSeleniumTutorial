from selenium import webdriver
from selenium.webdriver.common.by import By

import time

#INITIALIZE

"""Chrome Driver"""
driver = webdriver.Chrome()

"""get URL of desired webpage to automate"""
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name = "Joshua"
#START

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()


#IMPORTANT IMPORTANT IMPORTANT IMPORTANT
"""Switch from driver to alert mode"""

alert = driver.switch_to.alert

"""grab text of alert"""
alertText = alert.text
print(alertText)

assert name in alertText

"""Click on OK button"""
alert.accept()

"""Click on Cancel button on alerts"""
#alert.dismiss()

time.sleep(3)