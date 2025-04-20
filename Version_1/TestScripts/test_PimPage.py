"""
test_PimPage.py contains selenium sripts for executing test cases to.
1. Verify and validate new user creation.
2. Verify and validate from the Admin Menu that the new user exists in the records of the user or not?
3. Verify and validate whether the new user is able to log-in into the CRM or not?

"""

from PageObjects.PimPage import OrangeHRMpimPage

def test_create_new_user():
    """
    Test case to add new user
    """

    pim_page = OrangeHRMpimPage()
    pim_page.start()

    try:
        assert pim_page.create_new_user()
        print("SUCCESS: NEW USER CREATED.")
    finally:
        pim_page.shutdown()

def test_new_user_login():
    """
    Test case to add new user
    """

    pim_page = OrangeHRMpimPage()
    pim_page.start()

    try:
        assert pim_page.new_user_login()
        print("SUCCESS: NEW USER LOGIN VERIFIED.")
    finally:
        pim_page.shutdown()