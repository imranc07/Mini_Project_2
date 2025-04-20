"""
test_homepage.py - Selenium Pytest Script to:
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

from PageObjects.HomePage import OrangeHRMHomePage
from TestLocators.locators import OrangeHRMLocators

import pytest

@pytest.mark.order(2)
def test_login_elements_are_visible():
    """
    Test-Case-2: 
    Test to verify that username and password fields are visible on the login page.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    assert homepage.are_login_elements_visible()
    print("SUCCESS - The username and password input boxes are visible.")
    homepage.shutdown()

@pytest.mark.order(3)
def test_home_url():
    """
    Test-Case-3: 
    Test to verify that after successful login, the user is redirected to the home page.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    assert homepage.login()
    print("Successfully logged in and homepage URL Verified and Validated.")
    homepage.shutdown()

@pytest.mark.order(4)
def test_menu_visible_and_clickable():
    """
    Test-Case-4: 
    Test to verify that main menu items are visible and clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()

    # Perform login
    assert homepage.login()

    # Menu items with their locators
    menu_items = {
        "Admin": OrangeHRMLocators.admin_menu_locator,
        "PIM": OrangeHRMLocators.pim_menu_locator,
        "Leave": OrangeHRMLocators.leave_menu_locator,
        "Time": OrangeHRMLocators.time_menu_locator,
        "Recruitment": OrangeHRMLocators.recruitment_menu_locator,
        "My Info": OrangeHRMLocators.my_info_menu_locator,
        "Performance": OrangeHRMLocators.performance_menu_locator,
        "Dashboard": OrangeHRMLocators.dashboard_menu_locator,
    }

    for index, (menu_name, menu_locator) in enumerate(menu_items.items(), start=1):
        assert homepage.is_menu_item_visible_and_clickable(menu_locator, menu_name), f"{menu_name} menu check failed!"
        print(f"Menu {index}: SUCCESS - {menu_name.upper()} menu is visible and clickable.")

    homepage.shutdown()