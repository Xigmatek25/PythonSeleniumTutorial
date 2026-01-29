from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class forgotPasswordTest:

    def __init__(self):
        self.driver = None
        self.testURL = "https://rahulshettyacademy.com/client/#/auth/login"

    def setUpDriver(self):
        self.driver = webdriver.Chrome()
        print("✅ Web Driver initialized")

    def closeDriver(self):

        if self.driver:
            time.sleep(10)
            self.driver.quit()
            print("✅ Web Driver successfully quit")

    def clickingForgotPW(self):

        try:
            self.driver.get(self.testURL)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

            forgotPW = self.driver.find_element(By.CLASS_NAME, "forgot-password-link")
            forgotPW.click()

            forgotPassURL = "https://rahulshettyacademy.com/client/#/auth/password-new"
            WebDriverWait(self.driver, 10)
            assert self.driver.current_url == forgotPassURL
            print("✅ Forgot password page loaded successfully")

        except Exception as e:
            print("❌ expected forgot password page did not open")

    def inputEmail(self):

        try:

            test_email = "testemail@example.com"

            email_input = self.driver.find_element(By.CSS_SELECTOR, "input[type = 'email']")
            email_input.clear()
            email_input.send_keys(test_email)

            entered_email = email_input.get_attribute("value")

            assert entered_email == test_email, f"Expected `{test_email}`, got '{entered_email}'"
            print("✅ email input successful")

        except Exception as e:
            print(f"❌ Input text test failed: {e}")

    def inputPassword(self):

        try:

            test_password = "123abc@"

            password_input = self.driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input")
            password_input.clear()
            password_input.send_keys(test_password)

            entered_pw = password_input.get_attrubute("value")

            assert entered_pw == test_password, f"Expected '{test_password}', got '{entered_pw}'"
            print("✅password input successful")

        except Exception as e:
            print(f"❌ Input password test failed: {e}")



    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🚀 Starting Selenium automation tests for forgot password page...")
        print(f"📄 Testing URL: {self.testURL}")
        print("-" * 60)

        try:
            self.setUpDriver()

            self.clickingForgotPW()
            print("-" *60)

            self.inputEmail()
            print("-" * 60)

            self.inputPassword()
            print("-" * 60)

        except Exception as e:
            print(f"💥 Test suite failed: {e}")

        finally:
            self.closeDriver()


test_runner = forgotPasswordTest()

test_runner.run_all_tests()







