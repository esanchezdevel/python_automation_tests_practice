
import time
import pytest
from selenium.webdriver.common.by import By

class TestLoginPageNegative:

    @pytest.mark.login
    @pytest.mark.negative
    # driver parameter is the parameter returned by the fixture method at the top the class
    def test_negative_username(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        # Type username incorrectUser into username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('incorrectUser')
        
        # Type password Password123 into password field
        password_locator = driver.find_element(By.ID, 'password')
        password_locator.send_keys('Password123')
        # Click submit button
        submit_button_locator = driver.find_element(By.ID, 'submit')
        submit_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, 'error')
        assert error_message_locator.is_displayed(), 'ERROR: is not displayed but it should'
        assert error_message_locator.text == 'Your username is invalid!', 'Error message expected is not present'

    @pytest.mark.login
    @pytest.mark.negative
    # driver parameter is the parameter returned by the fixture method at the top the class
    def test_negative_password(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        
        # Type username student into username field
        username_locator = driver.find_element(By.ID, 'username')
        username_locator.send_keys('student')
        
        # Type incorrect password incorrectPassword into password field
        password_locator = driver.find_element(By.ID, 'password')
        password_locator.send_keys('incorrectPassword')
        # Click submit button
        submit_button_locator = driver.find_element(By.ID, 'submit')
        submit_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, 'error')
        assert error_message_locator.is_displayed(), 'ERROR: is not displayed but it should'
        assert error_message_locator.text == 'Your password is invalid!', 'Error message expected is not present'