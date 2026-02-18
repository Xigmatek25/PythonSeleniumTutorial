from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(5)
# START #

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")

time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

time.sleep(2)
cartItems = driver.find_elements(By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")

cartList = []
for item in cartItems:
    cartList.append(item.find_element(By.XPATH, "div/p").text)

print(cartList)





