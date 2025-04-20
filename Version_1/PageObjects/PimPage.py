
"""
Homepage.py - Python Selenium Script to
1. Create new user.
2. Verify from the Admin Menu that the new user exists in the records of the user or not?
3. Verify whether the new user is able to log-in into the CRM or not
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Importing exception handling classes
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException

# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing locators, test data, and utility functions
from PageObjects.HomePage import OrangeHRMHomePage
from TestLocators.locators import OrangeHRMLocators
from TestData.data import OrangeHRMData

# OrangeHRMpimPage class and inherited OrangeHRMHomePage class
class OrangeHRMpimPage(OrangeHRMHomePage):

    def __init__(self):
        """
        Initializes the WebDriver.
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

    def start(self):
        """
        Sets up WebDriver.
        """
        self.driver.get(OrangeHRMData.url)
        self.driver.maximize_window()

    def create_new_user(self):
        """
        Creates new user.
        """
        if not self.is_admin_menu_visible():
            print("PIM menu is not visible")
            return False
        try:
            # Click PIM menu and Add button
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.pim_menu_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.add_button_locator))).click()
            
            # Fill in user details
            self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.first_name_locator))).send_keys(OrangeHRMData().firts_name)
            self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.middle_name_locator))).send_keys(OrangeHRMData().middle_name)
            self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.last_name_locator))).send_keys(OrangeHRMData().last_name)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.login_radio_button))).click()
            self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.new_username_locator))).send_keys(OrangeHRMData().new_username)
            self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.new_password_locator))).send_keys(OrangeHRMData().new_password)
            self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.confirm_new_password_locator))).send_keys(OrangeHRMData().new_password)
 
            # Save the new user
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.save1_button_locator))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.save2_button_locator))).click()

            #Click on admin menu
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.admin_menu_locator))).click()
            
            # Verify the new user was created
            new_username_display = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.admin_user_text_locator))).text
            expected_name = f"{OrangeHRMData().new_username}"
            if expected_name in new_username_display:
                print(f"New user '{expected_name}' successfully created.")
                return True
            else:
                print(f"Newly added user '{expected_name}' not found in: {new_username_display}")
                return False
        
        # Handling exceptions 
        except ElementClickInterceptedException as error:
            print(f"ERROR: PIM menu is not clickable! {error}")
            return False

        # Handling exceptions 
        except (NoSuchElementException,ElementNotVisibleException) as error:
            print(f"ERROR: PIM menu not found! {error}")
            return False

    def new_user_login(self):
            """
            Verifying new user login.
            """
            try:
                # Entering username and password into the login form
                self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.username_locator))).send_keys(OrangeHRMData.new_username)
                self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.password_locator))).send_keys(OrangeHRMData.new_password)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.login_button_locator))).click()

                if OrangeHRMData.dashboard_url == self.driver.current_url:
                    print("SUCCESS: LOGIN SUCCESSFUL")
                    return True

                else:
                    print("FAIL: LOGIN FAILED")
                    return False

            # Handling exceptions 
            except (NoSuchElementException, ElementNotVisibleException) as error:
                print(f"ERROR: {error}")

# Closing the WebDriver
    def shutdown(self):
        self.driver.quit()