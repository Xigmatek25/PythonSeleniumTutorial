from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.implicitly_wait(3)

actions = ActionChains(driver)

mouseHvrBtn = driver.find_element(By.ID, "mousehover")

actions.move_to_element(mouseHvrBtn).perform()
actions.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

wait = WebDriverWait(driver,5)

element = wait.until(EC.visibility_of_element_located((By.ID, "checkBoxOption1")))
assert element.is_displayed(), print(f"❌ element not found")
print("✅ PASSED, element is found")

actions.double_click(element).perform()

time.sleep(5)
