from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(2)
# START #

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber") 

time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0

for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()


'''cartItems = driver.find_elements(By.XPATH, "//div[@class='cart-preview active']/div/div/ul/li")

cartList = []
for item in cartItems:
    cartList.append(item.find_element(By.XPATH, "div/p").text)

print(cartList)'''

time.sleep(2)
driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

promoText = driver.find_element(By.CLASS_NAME, "promoInfo").text
#assert "Code applied" in promoText

print(promoText)






