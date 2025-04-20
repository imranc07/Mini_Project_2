"""
This file contains all the locators used for interacting with elements on the OrangeHRM webpage.

The class `OrangeHRMLocators` serves as a central repository for storing:
- Locators for input fields, buttons, and other elements required in the test scripts.
- These locators are used by Selenium to locate and interact with the corresponding web elements on the UI.
"""

class OrangeHRMLocators:

    # Locator for the username input field
    username_locator = 'username'
    
    # Locator for the password input field
    password_locator = 'password'
    
    # XPath locator for the login button
    login_button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    
    # XPath locator for the logout dropdow
    logout_dropdown_locator = '//span[@class="oxd-userdropdown-tab"]'
    
    # XPath locator for the logout button within the dropdown
    logout_button_locator = '//a[contains(text(),"Logout")]'

    # Menu Locators for Home Page
    admin_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    pim_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    leave_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a/span'
    time_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[4]/a/span'
    recruitment_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a/span'
    my_info_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span'
    performance_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[7]/a/span'
    dashboard_menu_locator = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[8]/a/span'


    # Locators for PIM page
    first_name_locator = 'firstName'
    middle_name_locator = 'middleName'
    last_name_locator = 'lastName'
    login_radio_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    new_username_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    new_password_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    confirm_new_password_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    save1_button_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    save2_button_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'
    add_button_locator = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    admin_user_text_locator = '//div[contains(text(),"wanted")]'