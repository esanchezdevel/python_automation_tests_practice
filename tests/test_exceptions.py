# https://practicetestautomation.com/practice-test-exceptions/

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        
        self.open_url_and_click_add_button(driver)

        # Explicit wait to wait until row2 input is present.
        wait = WebDriverWait(driver, 10) # 10 is the timeout to wait
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Check that row2 appears
        #driver.implicitly_wait(6)
        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):

        self.open_url_and_click_add_button(driver)

        wait = WebDriverWait(driver, 10)
        row_2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        assert row_2_input_locator.is_displayed(), "Row 2 input should be displayed, but it's not"

        row_2_input_locator.send_keys("some text")

        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        confirmation_locator = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert confirmation_locator.text == "Row 2 was saved", "Confirmation message must contains saved word, but it's not"
    
    def open_url_and_click_add_button(self, driver):
        # Open the url
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()