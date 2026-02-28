from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, " .search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class = 'products']/div")

print(len(results))

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//img[@alt = 'Cart']").click()
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

#time.sleep(2)

driver.find_element(By.XPATH, "//input[@class = 'promoCode']").send_keys("rahulshetty")
driver.find_element(By.XPATH, "//button[@class = 'promoBtn']").click()

#Expicit Wait

wait = WebDriverWait(driver, 15)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

promoResult = driver.find_element(By.CLASS_NAME, "promoInfo").text

assert "applied" in promoResult


time.sleep(3)

