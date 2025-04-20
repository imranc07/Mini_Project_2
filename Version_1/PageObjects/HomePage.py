
"""
Homepage.py - Python Selenium Script to 
1. Verify and Validate whether the home URL is working or not?
2. Verify and Validate whether the username, password input boxes are visible or not.
3. Verify and Validate after successful login, whether the Menus 
    1. Admin, 
    2. PIM, 
    3. Leave,
    4. Time, 
    5. Recruitment, 
    6. My Info, 
    7. Performance,
    8. Dashboard are visible or not?
4. Verify  and Validate after successful login, whether the Menus 
    1. Admin, 
    2. PIM, 
    3. Leave,
    4. Time, 
    5. Recruitment, 
    6. My Info, 
    7. Performance,
    8. Dashboard are clickable or not?
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

    # Method for verifying OrangeHRM Home Page
    def home_url(self):
        if not self.login():
            print("FAIL: Can not verify Home Page URL. User is not logged in")
            return False

        try:
            # Retrieve and return the current URL
            current_url = self.driver.current_url
            return current_url

        # Handling exceptions 
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print(f"ERROR: {error}")

    def is_admin_menu_visible(self):
        """
        Check if the admin menu is visible on the homepage.
        """
        if not self.home_url():
            print("Admin menu is not visible. User is not logged in")
            return False

        try:
            # Locate the admin menu
            admin_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.admin_menu_locator)))
            if admin_menu.is_displayed():
                return True
            else:
                print("ERROR: admin menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: admin menu not found! {error}")
            return False

    def is_admin_menu_clickable(self):
        """
        Check if the admin menu is clickable on homepage.
        """
        if not self.is_admin_menu_visible():
            print("Admin menu is not visible and clickable")
            return False
        try:
            # Locate the admin menu
            admin_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.admin_menu_locator)))
            # click the admin menu 
            admin_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: admin menu is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: admin menu not found! {error}")
            return False
 
    def is_pim_menu_visible(self):
        """
        Check if the pim menu is visible on the homepage.
        """
        if not self.home_url():
            print("pim menu is not visible. User is not logged in")
            return False

        try:
            # Locate the pim menu
            pim_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.pim_menu_locator)))
            if pim_menu.is_displayed():
                return True
            else:
                print("ERROR: pim menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: pim menu not found! {error}")
            return False

    def is_pim_menu_clickable(self):
        """
        Check if the pim menu is clickable.
        """
        if not self.is_admin_menu_visible():
            print("pim menu is not visible and clickable")
            return False
        try:
            # Locate the pim menu
            pim_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.pim_menu_locator)))
            # click the pim menu 
            pim_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: pim menu is not clickable! {error}")
            return False

        # Handling exceptions
        except NoSuchElementException as error:
            print(f"ERROR: pim menu not found! {error}")
            return False
 
    def is_leave_menu_visible(self):
        """
        Check if the leave menu is visible on the homepage.
        """
        if not self.home_url():
            print("leave menu is not visible. User is not logged in")
            return False

        try:
            # Locate the leave menu
            leave_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.leave_menu_locator)))
            if leave_menu.is_displayed():
                return True
            else:
                print("ERROR: leave menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: leave menu not found! {error}")
            return False

    def is_leave_menu_clickable(self):
        """
        Check if the leave menu is clickable on homepage.
        """
        if not self.is_leave_menu_visible():
            print("leave menu is not visible and clickable")
            return False
        try:
            # Locate the leave menu
            leave_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.leave_menu_locator)))
            # click the leave menu 
            leave_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: leave menu is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: leave menu not found! {error}")
            return False

    def is_time_menu_visible(self):
        """
        Check if the time menu is visible on the homepage.
        """
        if not self.home_url():
            print("time menu is not visible. User is not logged in")
            return False

        try:
            # Locate the time menu
            time_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.time_menu_locator)))
            if time_menu.is_displayed():
                return True
            else:
                print("ERROR: time menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: time menu not found! {error}")
            return False

    def is_time_menu_clickable(self):
        """
        Check if the time menu is clickable on homepage.
        """
        if not self.is_time_menu_visible():
            print("time menu is not visible and clickable")
            return False
        try:
            # Locate the time menu
            time_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.time_menu_locator)))
            # click the time menu 
            time_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: time menu is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: time menu not found! {error}")
            return False

    def is_recruitment_menu_visible(self):
        """
        Check if the recruitment menu is visible on the homepage.
        """
        if not self.home_url():
            print("recruitment menu is not visible. User is not logged in")
            return False

        try:
            # Locate the recruitment menu
            recruitment_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.recruitment_menu_locator)))
            if recruitment_menu.is_displayed():
                return True
            else:
                print("ERROR: recruitment menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: recruitment menu not found! {error}")
            return False

    def is_recruitment_menu_clickable(self):
        """
        Check if the recruitment menu is clickable on homepage.
        """
        if not self.is_recruitment_menu_visible():
            print("recruitment menu is not visible and clickable")
            return False
        try:
            # Locate the recruitment menu
            recruitment_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.recruitment_menu_locator)))
            # click the recruitment menu 
            recruitment_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: recruitment menu is not clickable! {error}")
            return False

        except NoSuchElementException as error:
            print(f"ERROR: recruitment menu not found! {error}")
            return False

    def is_my_info_menu_visible(self):
        """
        Check if the my info menu is visible on the homepage.
        """
        if not self.home_url():
            print("my info menu is not visible. User is not logged in")
            return False

        try:
            # Locate the my info menu
            my_info_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.my_info_menu_locator)))
            if my_info_menu.is_displayed():
                return True
            else:
                print("ERROR: my info menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: my info menu not found! {error}")
            return False

    def is_my_info_menu_clickable(self):
        """
        Check if the my info menu is clickable on homepage.
        """
        if not self.is_my_info_menu_visible():
            print("my info menu is not visible and clickable")
            return False
        try:
            # Locate the my info menu
            my_info_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.my_info_menu_locator)))
            # click the my info menu 
            my_info_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: my info menu is not clickable! {error}")
            return False

        # Handling exceptions
        except NoSuchElementException as error:
            print(f"ERROR: my info menu not found! {error}")
 
    def is_performance_menu_visible(self):
        """
        Check if the performance menu is visible on the homepage.
        """
        if not self.home_url():
            print("my inperformance is not visible. User is not logged in")
            return False

        try:
            # Locate the performance menu
            performance_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.performance_menu_locator)))
            if performance_menu.is_displayed():
                return True
            else:
                print("ERROR: performance menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: performance menu not found! {error}")
            return False

    def is_performance_menu_clickable(self):
        """
        Check if the performance menu is clickable.
        """
        if not self.is_performance_menu_visible():
            print("performance menu is not visible and clickable")
            return False
        try:
            # Locate the performance menu
            performance_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.performance_menu_locator)))
            # click the performance menu 
            performance_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: performance menu is not clickable! {error}")
            return False

        # Handling exceptions
        except NoSuchElementException as error:
            print(f"ERROR: performance menu not found! {error}")
            return False

    def is_dashboard_menu_visible(self):
        """
        Check if the dashboard menu is visible on the homepage.
        """
        if not self.home_url():
            print("my indashboard is not visible. User is not logged in")
            return False

        try:
            # Locate the dashboard menu
            dashboard_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.dashboard_menu_locator)))
            if dashboard_menu.is_displayed():
                return True
            else:
                print("ERROR: dashboard menu is not visible!")
                return False
            
        # Handling exceptions 
        except NoSuchElementException as error:
            print(f"ERROR: dashboard menu not found! {error}")
            return False

    def is_dashboard_menu_clickable(self):
        """
        Check if the dashboard menu is clickable on homepage.
        """
        if not self.is_dashboard_menu_visible():
            print("dashboard menu is not visible and clickable")
            return False
        try:
            # Locate the dashboard menu
            dashboard_menu = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRMLocators.dashboard_menu_locator)))
            # click the dashboard menu 
            dashboard_menu.click()
            return True

        # Handling exceptions
        except ElementClickInterceptedException as error:
            print(f"ERROR: dashboard menu is not clickable! {error}")
            return False

        # Handling exceptions
        except NoSuchElementException as error:
            print(f"ERROR: dashboard menu not found! {error}")
            return False

    # Closing the WebDriver
    def shutdown(self):
        self.driver.quit()
