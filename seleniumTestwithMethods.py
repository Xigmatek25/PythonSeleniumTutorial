import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPageTest:
    def __init__(self):
        self.driver = None
        self.loginURL = "https://rahulshettyacademy.com/angularpractice/"

    def setup_driver(self):
        """Initialize Web Driver"""

        try:
            self.driver = webdriver.Chrome()
            print("✅ Web driver initialized successfully")

        except Exception as e:
            print(f"❌ Failed to initialize web driver {e}")

    def teardown_driver(self):
        """Closes the Driver"""

        if self.driver:
            time.sleep(10)
            self.driver.quit()
            print("✅ Web Driver closed successfully")

    def test_page_loads(self):
        """Tests if the page loads successfully"""

        try:
            self.driver.get(self.loginURL)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1"))
                                                 )

            page_title = self.driver.title
            assert "ProtoCommerce" in page_title, f"Expected 'ProtoCommerce' in title, got  '{page_title}'"
            print("✅ page loaded succesfully")

        except Exception as e:
            print(f"💥 Test suite failed: {e}")

    def test_input_fields_present(self):
        """tests if email and password fields are present in the form"""

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))

            #verify name field is present
            name_input = self.driver.find_element(By.NAME, "name")
            assert name_input.is_displayed(), "Name field is not found"
            print("✅ Name input field is visible")

            #verify email input field is present
            email_input = self.driver.find_element(By.NAME, "email")
            assert email_input.is_displayed(), "Email field is not found"
            print("✅ Email input field is visible")

            #verify password field is present
            password_input = self.driver.find_element(By.ID, "exampleInputPassword1")
            assert password_input.is_displayed(), "Password field is not found"
            print("✅ Password input field is visible")

        except Exception as e:
            print(f"❌ Page loading test failed: {e}")
            raise





    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🚀 Starting Selenium automation tests for login page...")
        print(f"📄 Testing URL: {self.loginURL}")
        print("-" * 60)

        try:
            self.setup_driver()

            self.test_page_loads()
            print("-" *60)

            self.test_input_fields_present()
            print("-"*60)

        except Exception as e:
            print(f"💥 Test suite failed: {e}")

        finally:
            self.teardown_driver()


test_runner = LoginPageTest()
test_runner.run_all_tests()
