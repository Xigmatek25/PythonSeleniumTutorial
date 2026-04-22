from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.implicitly_wait(3)

action = ActionChains(driver)

mouseHoverBtn = driver.find_element(By.ID, "mousehover")

action.move_to_element(mouseHoverBtn).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()

wait = WebDriverWait(driver, 5)

element = wait.until(EC.visibility_of_element_located((By.ID, "checkBoxOption1")))

action.double_click(element).perform()

time.sleep(3)
#ACTION CHAIN
    #action.context_click() -> right click
    #action.click_and_hold -> click and hold
    #action.double_click -> used for double clicking
    #action.move_to_element -> used to just go to a specific element (example: hovering)