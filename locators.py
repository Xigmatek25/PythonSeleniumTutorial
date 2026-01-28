import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/") #use to get the website


# ID, Xpath, CSSSelector, Classname, name, linkText


"""send keys to email field"""
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com") #


"""send keys to password field"""
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password123")


"""tick checkbox field"""
driver.find_element(By.ID, "exampleCheck1").click()


"""select radio button"""
#driver.find_element(By.XPATH, "//label[@for='inlineRadio1']").click()

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[attribute = 'value']

#driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("Xigmatek")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
"""get and click submit button"""
driver.find_element(By.XPATH, "//input[@type='submit']").click()

"""use to get response message upon clicking subnmit"""
message = driver.find_element(By.CLASS_NAME, "alert-dismissible").text
print(message)

"""check if word success is in the message or alert message"""
assert "Success" in message

"""test how you can get specific field even if you are using tagname and attribute duplicates"""
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("test if working")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
#CSSSelector - "tagname[attribute = 'value']", #id, .className 

#Xpath - "//tagname[@attribute = 'value']"


time.sleep(2)

#XPATH - "//tagname[@attribute = 'value']"

# "//tagname[@attribute = '']"

# "tagname[attribute = 'value']"