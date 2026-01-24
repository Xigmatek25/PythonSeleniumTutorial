import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME, "name").send_keys("Joshua")

driver.find_element(By.NAME, "email").send_keys("sample@email.com")

driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")

driver.find_element(By.ID, "exampleCheck1").click()

driver.find_element(By.CSS_SELECTOR, "input[type = 'submit']").click()

submit_button_name = driver.find_element(By.CLASS_NAME, "btn")
label = submit_button_name.get_attribute("value")
print(label)
try:
    assert label == "Done"
    print("PASSED")
except AssertionError:
    print("FAILED: Expected 'Done' but got " + str(label))

response = driver.find_element(By.CLASS_NAME, "alert-success").text
print("Submit message: " + str(response))

assert "Success!" in response
#driver.find_element(By.)

# Xpath = //tagname[@attribute = 'value']
# CSS = tagname[attribute = 'value']


time.sleep(3)