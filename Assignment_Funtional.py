from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(2)


# ---------START -------------#


#TYPE "BER" IN SEARCH BAR
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)


#SCENARIO: GET LIST OF ITEMS
expected = ["Strawberry - 1/4 Kg", "Cucumber - 1 Kg", "Raspberry - 1/4 Kg"]
actual = []
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for result in results:
    actual.append(result.find_element(By.XPATH, "h4").text)
    result.find_element(By.XPATH, "div/button").click()

print(actual)

assert sorted(actual) == sorted(expected)
print("✅ CHECKLIST IS CORRECT")

#END SCENARIO 1


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[text() = 'PROCEED TO CHECKOUT']").click()

#SCENARIO: SUM VALIDATION

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)


totalAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)

assert sum == totalAmount
print("✅ total amount is equal to sum of prices in cart")

#END SCENARIO 2


driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))

promoText = driver.find_element(By.CLASS_NAME, "promoInfo").text

#SCENARIO: CHECK PROMO IS APPLIED
assert "Code applied" in promoText
print("✅ code is applied")
#END

totalAfterDisc = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)

#SCENARIO: DISCOUNT IS LESS THAN TOTAL AMOUNT
assert totalAmount > totalAfterDisc
print("✅ Discount is less than total amount")
#end







