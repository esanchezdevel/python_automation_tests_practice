# To run script with python using virtual environment we have to:
# 1. Create the virtual environment with Ctrl+Shift+P look for "python: create virtual environment"
# 2. Once the Virtual environment is created in .venv folder, choose as python interpreter the python of the virtual environment with
#    Ctrl+Shift+P look for "python: select interpreter" and choose the virtual environment already created

import time
import pytest
from selenium.webdriver.common.by import By

class TestPositiveScenarios:

    # The marks are used to execute only specific tests. For example, if we run 
    # "pytest -m positive" only the tests marked with @pytest.mark.positive will be executed
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Test steps:
        # -----------
        # 1. Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # 3. Fill form inputs with data
        # To create a locator to our inputs attributes, we have to follow the next rule:
        # //tag[@attribute='value'], for example: //input[@id='username'] or //button[@class='btn']
        username_locator = driver.find_element(By.ID, 'username') # get username by the id of the html tag
        password_locator = driver.find_element(By.NAME, 'password') # get password by the name of the html tag
        submit_button_locator = driver.find_element(By.XPATH, '//button[@class=\'btn\']') # get the button using the XPATH format

        # type text in form inputs
        username_locator.send_keys('student')
        password_locator.send_keys('Password123')

        # 4. Submit the form
        submit_button_locator.click()
        time.sleep(2)

        # 5. Validate that the URL where we are redirected is the right one
        actual_url = driver.current_url
        assert actual_url.__contains__('practicetestautomation.com/logged-in-successfully/')

        # 6. Validate result page contains success data
        post_title_locator = driver.find_element(By.TAG_NAME, 'h1') # we can use it here, because we know that the page only has one h1 in the full page
        post_logout_locator = driver.find_element(By.LINK_TEXT, 'Log out')

        actual_title = post_title_locator.text
        assert actual_title == 'Logged In Successfully'

        assert post_logout_locator.is_displayed()

        time.sleep(5)
        print('Atomation tests PASSED!!!')


