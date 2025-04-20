"""
test_PimPage.py contains selenium sripts for executing test cases to.
1. Create new user, verify and validate whether the new user is able to log-in into the CRM or not?
2. Verify and validate from the Admin Menu that the new user exists in the records of the user or not?

"""
import pytest
from PageObjects.PimPage import OrangeHRMpimPage

@pytest.mark.order(5)
def test_create_user_and_login():
    """
    Test-Case-5:
    1) Create new user.
    2) Verify that the new user is able to log in to the CRM.
    """

    # Admin login and user creation
    pim_page = OrangeHRMpimPage()
    pim_page.start()

    assert pim_page.login()
    assert pim_page.create_new_user()
    pim_page.shutdown()

    # Login with the newly created user
    new_user_page = OrangeHRMpimPage()
    new_user_page.start()

    assert new_user_page.new_user_login()
    new_user_page.shutdown()

@pytest.mark.order(6)
def test_verify_user_exists_in_admin():
    """
    Test-Case-6:
    1) Verify from Admin Menu that the new user exists in the user list.
    """

    pim_page = OrangeHRMpimPage()
    pim_page.start()

    assert pim_page.login()

    # Navigate to Admin Menu and verify new user
    is_user_found = pim_page.verify_new_user_in_admin_menu()
    assert is_user_found
    
    pim_page.shutdown()
