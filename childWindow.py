from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.LINK_TEXT, "Click Here").click()

openedWindows = driver.window_handles

driver.switch_to.window(openedWindows[1])

textNew = driver.find_element(By.TAG_NAME, "h3").text

try:
    assert textNew == "New Window"
    print("✅ Text in new window is correct")
except Exception as e:
    print(f"❌ Text in new windows is incorrect {e}")

driver.close()

driver.switch_to.window(openedWindows[0])

textCheck = driver.find_element(By.TAG_NAME, "h3").text

try:
    assert textCheck == "Opening a new window"
    print("✅ switched back to old window")
except Exception as e:
    print(f"❌ Did not switched back to old window {e}")

time.sleep(5)



###NOTES

#driver.window_handles -> will put all windows in session in a list
#driver.switch_to.window() -> used to switch windows; usually comes with the variable for the list of windows






