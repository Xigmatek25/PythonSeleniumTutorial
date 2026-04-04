from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(2)



driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(2)

#expected values for search keyword "ber"
expected = ["Strawberry - 1/4 Kg", "Cucumber - 1 Kg", "Raspberry - 1/4 Kg"]
actual = []

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    actual.append(result.find_element(By.XPATH, "h4").text)

print(actual)

assert sorted(actual) == sorted(expected)


time.sleep(5)