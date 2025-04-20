"""
test_homepage.py contains selenium sripts for executing test cases to.
1. Verify whether the home URL is working or not?
2. Verify whether the username, password input boxes are visible or not.
3. Verify after successful login, whether the Menus 
    1. Admin, 
    2. PIM, 
    3. Leave,
    4. Time, 
    5. Recruitment, 
    6. My Info, 
    7. Performance,
    8. Dashboard are visible or not?
4. Verify after successful login, whether the Menus 
    1. Admin, 
    2. PIM, 
    3. Leave,
    4. Time, 
    5. Recruitment, 
    6. My Info, 
    7. Performance,
    8. Dashboard are clickable or not?

"""

from PageObjects.HomePage import OrangeHRMHomePage
from TestData.data import OrangeHRMData


def test_username_and_password_input_box():
    """
    Test case to Check if the username and password input boxes are visible on the login page.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.username_and_password_input_box() == True
        print("SUCCESS: USERNAME AND PASSWORD INPUT BOX VISIBLE.")
    finally:
        homepage.shutdown()

def test_home_url():
    """
    Test case to Verify Home Page URL.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()

    try:
        # Retrieve the homepage URL
        home_url = homepage.home_url()
        # Assert that the homepage URL matches the expected dashboard URL
        assert home_url == OrangeHRMData().dashboard_url
        print("SUCCESS: HOME PAGE URL VERIFIED")
    finally:
        homepage.shutdown()

def test_admin_menu_visible():
    """
    Test case to verify if the admin menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_admin_menu_visible() == True
        print("SUCCESS: ADMIN MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_admin_menu_clickable():
    """
    Test case to verify if the admin menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_admin_menu_clickable() == True
        print("SUCCESS: ADMIN MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_pim_menu_visible():
    """
    Test case to verify if the pim menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_pim_menu_visible() == True
        print("SUCCESS: PIM MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_pim_menu_clickable():
    """
    Test case to verify if the pim menu is clickableafter successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_pim_menu_clickable() == True
        print("SUCCESS: PIM MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_leave_menu_visible():
    """
    Test case to verify if the leave menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_leave_menu_visible() == True
        print("SUCCESS: LEAVE MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_leave_menu_clickable():
    """
    Test case to verify if the leave menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_leave_menu_clickable() == True
        print("SUCCESS: LEAVE MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_time_menu_visible():
    """
    Test case to verify if the time menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_time_menu_visible() == True
        print("SUCCESS: TIME MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_time_menu_clickable():
    """
    Test case to verify if the time menu is clickable.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_time_menu_clickable() == True
        print("SUCCESS: TIME MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_recruitment_menu_visible():
    """
    Test case to verify if the recruitment menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_recruitment_menu_visible() == True
        print("SUCCESS: RECRUITMENT MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_recruitment_menu_clickable():
    """
    Test case to verify if the recruitment menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_recruitment_menu_clickable() == True
        print("SUCCESS: RECRUITMENT MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_my_info_menu_visible():
    """
    Test case to verify if the my info menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_my_info_menu_visible() == True
        print("SUCCESS: MY INFO MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_my_info_menu_clickable():
    """
    Test case to verify if the my info menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_my_info_menu_clickable() == True
        print("SUCCESS: MY INFO MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_performance_menu_visible():
    """
    Test case to verify if the performance menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_performance_menu_visible() == True
        print("SUCCESS: PERFORMANCE MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_performance_menu_clickable():
    """
    Test case to verify if the performance menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_performance_menu_clickable() == True
        print("SUCCESS: PERFORMACE MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()

def test_dashboard_menu_visible():
    """
    Test case to verify if the dashboard menu is visible after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_dashboard_menu_visible() == True
        print("SUCCESS: DASHBOARD MENU IS VISIBLE.")
    finally:
        homepage.shutdown()

def test_dashboard_menu_clickable():
    """
    Test case to verify if the dashboard menu is clickable after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()
    try:
        assert homepage.is_dashboard_menu_clickable() == True
        print("SUCCESS: DASHBOARD MENU IS CLICKABLE.")
    finally:
        homepage.shutdown()