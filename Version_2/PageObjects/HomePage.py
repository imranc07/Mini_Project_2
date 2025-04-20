
"""
Homepage.py - Python Selenium Script to 
1. Verify and Validate whether the username, password input boxes are visible or not.
2. Verify and Validate whether the home URL is working or not?
3. Verify and Validate after successful login, whether the Menus 
    1. Admin, 
    2. PIM, 
    3. Leave,
    4. Time, 
    5. Recruitment, 
    6. My Info, 
    7. Performance,
    8. Dashboard are visible and clickable or not?
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Exception handling
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException

# WebDriver wait utilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing Test Locators and Test data
from TestLocators.locators import OrangeHRMLocators
from TestData.data import OrangeHRMData


class OrangeHRMHomePage:

    def __init__(self):
        """
        Initializes the WebDriver and sets up explicit wait.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def start(self):
        """
        Navigates to the OrangeHRM URL and maximizes the browser window.
        """
        self.driver.get(OrangeHRMData.url)
        self.driver.maximize_window()

    def are_login_elements_visible(self):
        """
        Verifies that the username and password input fields are visible.
        """
        try:
            username_visible = self.wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRMLocators.username_locator)))
            password_visible = self.wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRMLocators.password_locator)))
            return username_visible.is_displayed() and password_visible.is_displayed()
        except TimeoutException as e:
            print(f"ERROR: Login input fields are not visible - {e}")
            return False

    def login(self):
        """
        Logs into the application using provided credentials.
        """
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRMLocators.username_locator))).send_keys(OrangeHRMData.username)
            self.wait.until(EC.visibility_of_element_located((By.NAME, OrangeHRMLocators.password_locator))).send_keys(OrangeHRMData.password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.login_button_locator))).click()
            
            # Verify the home URL is working or not?
            expected_url = OrangeHRMData.dashboard_url  
            current_url = self.driver.current_url

            if expected_url == current_url:
                return True
            else:
                print(f"ERROR: Unexpected URL after login. Expected: {expected_url}, but got: {current_url}")
                return False

        except TimeoutException as e:
            print(f"ERROR: Login timeout - {e}")
            return False
        except Exception as e:
            print(f"ERROR: Login failed - {e}")
            return False

    def is_menu_item_visible_and_clickable(self, menu_locator, menu_name):
        """
        Generic method to check if a menu item is visible and clickable on the homepage.
        """
        try:
            # menu_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, menu_locator)))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, menu_locator)))
            self.wait.until(EC.element_to_be_clickable((By.XPATH, menu_locator))).click()
            return True
        except TimeoutException:
            print(f"ERROR: {menu_name} menu is not visible or not clickable within the timeout.")
        except ElementClickInterceptedException as e:
            print(f"ERROR: {menu_name} menu not clickable - {e}")
        except NoSuchElementException as e:
            print(f"ERROR: {menu_name} menu not found - {e}")
        return False

    def shutdown(self):
        """
        Closes the browser.
        """
        if self.driver:
            self.driver.quit()