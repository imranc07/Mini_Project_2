from PageObjects.HomePage import OrangeHRMHomePage
from TestData.data import OrangeHRMData

def test_username_and_password_input_box():
    """
    Test case to Check if the username and password input boxes are visible on the login page.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()

    assert homepage.username_and_password_input_box() is True
    print("SUCCESS: USERNAME AND PASSWORD INPUT BOX VISIBLE.")

    homepage.shutdown()

def test_home_url():
    """
    Test case to Verify Home Page URL.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()

    home_url = homepage.home_url()
    assert home_url == OrangeHRMData().dashboard_url
    print("SUCCESS: HOME PAGE URL VERIFIED")

    homepage.shutdown()

def test_menu_visibility_and_clickable():
    """
    Test case to verify visibility and clickability of all menus after successful login.
    """
    homepage = OrangeHRMHomePage()
    homepage.start()

    menus = ["admin", "pim", "leave", "time", "recruitment", "my_info", "performance", "dashboard"]
    for menu in menus:
        is_visible = getattr(homepage, f"is_{menu}_menu_visible")()
        is_clickable = getattr(homepage, f"is_{menu}_menu_clickable")()

        assert is_visible is True, f"FAILURE: {menu.upper()} MENU IS NOT VISIBLE."
        assert is_clickable is True, f"FAILURE: {menu.upper()} MENU IS NOT CLICKABLE."

        print(f"SUCCESS: {menu.upper()} MENU IS VISIBLE AND CLICKABLE.")

    homepage.shutdown()
