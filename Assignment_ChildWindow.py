from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

#driver.maximize_window()

driver.implicitly_wait(3)


wait = WebDriverWait(driver, 4)

link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material")))
link.click()


time.sleep(3)

openWindows = driver.window_handles

#switch to new window
driver.switch_to.window(openWindows[1])


wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.im-para.red")))

text = driver.find_element(By.CSS_SELECTOR, "p.red").text
email = text.split("at")[1].split(" ")[1]


print(email)


#switch back to old window
driver.switch_to.window(openWindows[0])

driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys("1234567")

driver.find_element(By.CSS_SELECTOR, "input.btn.btn-info.btn-md").click()

message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger.col-md-12"))).text

print(message)
time.sleep(5)


