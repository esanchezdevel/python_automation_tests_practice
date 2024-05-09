# To run script with python using virtual environment we have to:
# 1. Create the virtual environment with Ctrl+Shift+P look for "python: create virtual environment"
# 2. Once the Virtual environment is created in .venv folder, choose as python interpreter the python of the virtual environment with
#    Ctrl+Shift+P look for "python: select interpreter" and choose the virtual environment already created

import pytest

from page_objects.logged_in_successfully_page import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage

class TestPositiveScenarios:

    # The marks are used to execute only specific tests. For example, if we run 
    # "pytest -m positive" only the tests marked with @pytest.mark.positive will be executed
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        
        # initialize our LoginPage class
        login_page = LoginPage(driver)

        # Open page
        login_page.open()

        # Type username student into Username field
        # Type password Password123 into Password field
        # Push Submit button
        login_page.execute_login("student", "Password123")

        logged_in_successfully = LoggedInSuccessfullyPage(driver)
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in_successfully.expected_url == logged_in_successfully.current_url, "The URL is not the expected one"
        
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_successfully.header == "Logged In Successfully", "The confirmation text is not the expected one"

        # Verify button Log out is displayed on the new page
        assert logged_in_successfully.is_logout_button_displayed(), "The logout button is not displayed"


