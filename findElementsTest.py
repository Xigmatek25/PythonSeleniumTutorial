from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


#driver.find_element(By.ID, "autosuggest").send_keys("ind") 
#time.sleep(2)

country_search = driver.find_element(By.ID, "autosuggest")
country_search.send_keys("lo")
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

for country in countries:
    if country.text == "Slovenia":
        country.click()
        break
 
#assert country_search.text == "Slovenia"
#print(f"PASSED! {counyt_search} is selected")

#raise Exception(f"Test failed: Expected 'Slovenia', got '{country_search.text}'")

print(country_search.text)
time.sleep(2)   
