"""
This script demonstrates data-driven testing using Selenium and Excel files.
It automates the login functionality of the OrangeHRM webpage, performing multiple login attempts 
based on test data stored in an Excel file. The results of each test are logged back into the Excel file.
"""

# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime

# Importing exception handling classes
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

# Importing WebDriver wait utilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importing locators, test data, and utility functions
from TestLocators.locators import OrangeHRMLocators
from TestData.data import OrangeHRMData
from Utilities.excel_functions import ExcelFunctions

# Test class for OrangeHRM data-driven testing
class TestOrangeHrmDDTFLogin:

    def test_DDTF_login(self):
        """
        Performs data-driven login attempts using test data from an Excel file.
        """

        # Setting up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 10)

        # Navigating to the OrangeHRM login page
        self.driver.get(OrangeHRMData().url)

        # Maximize the browser window
        self.driver.maximize_window()

        try:
            # Load Excel file and sheet details
            self.excel_file = OrangeHRMData.excel_file
            self.sheet_number = OrangeHRMData.sheet_number

            # Initialize the Excel utility for data reading and writing
            self.excel = ExcelFunctions(self.excel_file, self.sheet_number)

            # Get the total number of rows with data in the Excel sheet
            total_rows = self.excel.row_count()

            # Loop through each row in the Excel sheet
            for row in range(2, total_rows + 1):
                # Read username and password from the Excel sheet
                username = self.excel.read_data(row, 5)
                password = self.excel.read_data(row, 6)

                # Enter username and password into the login form
                self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.username_locator))).send_keys(username)
                self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.password_locator))).send_keys(password)
                self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.login_button_locator))).click()

                # Check for login success based on cookies and URL
                cookies = self.driver.get_cookies()
                session_cookie = next((cookie for cookie in cookies if cookie['name'] == 'orangehrm'), None)

                if session_cookie and OrangeHRMData.dashboard_url in self.driver.current_url:
                    print("SUCCESS: Login Successful")

                    # Log success details in the Excel sheet
                    self.excel.write_data(row, 7, datetime.today())
                    self.excel.write_data(row, 8, datetime.now().time())
                    self.excel.write_data(row, 9, "Test Pass")

                    # Log out of the application
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.logout_dropdown_locator))).click()
                    self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.logout_button_locator))).click()

                elif OrangeHRMData().url in self.driver.current_url:
                    print("FAIL: Login Failed")

                    # Log failure details in the Excel sheet
                    self.excel.write_data(row, 7, datetime.today())
                    self.excel.write_data(row, 8, datetime.now().time())
                    self.excel.write_data(row, 9, "Test Fail")
                    self.driver.refresh()

        except (NoSuchElementException, ElementNotVisibleException) as error:
            # Handling exceptions
            print(f"ERROR: {error}")
            # Log error details in the Excel sheet
            self.excel.write_data(row, 7, datetime.today())
            self.excel.write_data(row, 8, datetime.now().time())
            self.excel.write_data(row, 9, f"Error: {error}")

        finally:
            # Close the WebDriver
            self.driver.quit()