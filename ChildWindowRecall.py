from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Click Here").click()

time.sleep(4)

windows = driver.window_handles

driver.switch_to.window(windows[1])

checkText = driver.find_element(By.TAG_NAME, "h3").text

assert checkText == "New Window"
print("✅PASSED checkText")

driver.switch_to.window(windows[0])

checkTextBack = driver.find_element(By.TAG_NAME, "h3").text

assert checkTextBack == "Opening a new window"
print("✅PASSED checkTextBack")

time.sleep(4)
