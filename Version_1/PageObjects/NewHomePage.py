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
from TestLocators.locators import OrangeHRMLocators
from TestData.data import OrangeHRMData

# OrangeHRMHomePage class to automate the Orange HRM Home Page
class OrangeHRMHomePage:

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

    def username_and_password_input_box(self):
        """
        Checks if the username and password input boxes are visible on the login page.
        """
        try:
            # Locate the username input box
            username_input_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.username_locator)))

            # Locate the password input box
            password_input_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.password_locator)))

            # Check if both input boxes are visible
            if username_input_box.is_displayed() and password_input_box.is_displayed():
                return True
            else:
                print("ERROR: Username and password input boxes are not visible!")
                return False

        # Handling exceptions
        except NoSuchElementException as error:
            print(f"ERROR: Username and password input box not found! {error}")
            return False

    def login(self):
        try:
            # Entering username and password into the login form
            self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.username_locator))).send_keys(OrangeHRMData.username)
            self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRMLocators.password_locator))).send_keys(OrangeHRMData.password)
            self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRMLocators.login_button_locator))).click()
            return True

        # Handling exceptions
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR: {error}")

    def home_url(self):
        if not self.login():
            print("FAIL: Cannot verify Home Page URL. User is not logged in")
            return False

        try:
            # Retrieve and return the current URL
            current_url = self.driver.current_url
            return current_url

        # Handling exceptions
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR: {error}")

    def is_menu_item_visible_and_clickable(self, menu_locator, menu_name):
        """
        Generic method to check if a menu item is visible and clickable on the homepage.
        :param menu_locator: Locator of the menu item (XPath or other supported locators).
        :param menu_name: Name of the menu item for logging purposes.
        :return: True if the menu item is visible and clickable, False otherwise.
        """
        if not self.home_url():
            print(f"{menu_name} menu is not visible. User is not logged in")
            return False

        try:
            # Locate the menu item
            menu_item = self.wait.until(EC.presence_of_element_located((By.XPATH, menu_locator)))

            # Check visibility
            if not menu_item.is_displayed():
                print(f"ERROR: {menu_name} menu is not visible!")
                return False

            # Check clickability
            menu_item.click()
            return True

        except ElementClickInterceptedException as error:
            print(f"ERROR: {menu_name} menu is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: {menu_name} menu not found! {error}")
            return False

    # Example usages of the generic method for each menu item
    def is_admin_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.admin_menu_locator, "Admin")

    def is_pim_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.pim_menu_locator, "PIM")

    def is_leave_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.leave_menu_locator, "Leave")

    def is_time_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.time_menu_locator, "Time")

    def is_recruitment_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.recruitment_menu_locator, "Recruitment")

    def is_my_info_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.my_info_menu_locator, "My Info")

    def is_performance_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.performance_menu_locator, "Performance")

    def is_dashboard_menu_visible_and_clickable(self):
        return self.is_menu_item_visible_and_clickable(OrangeHRMLocators.dashboard_menu_locator, "Dashboard")

    # Closing the WebDriver
    def shutdown(self):
        self.driver.quit()
