# https://practicetestautomation.com/practice-test-exceptions/

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage

class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        # Open the page
        exceptions_page.open()
        # Add the second row
        exceptions_page.add_second_row()
        # Verify row2 is displayed
        assert exceptions_page.is_row2_displayed(), "Row 2 input should be displayed, but it's not"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        # Open the page
        exceptions_page.open()
        # Add the second row
        exceptions_page.add_second_row()
        # Input some text in the new input
        exceptions_page.add_second_food("Sushi")
        # Verify that the confirmation message is the expected one
        assert exceptions_page.confirmation_message == "Row 2 was saved", "Confirmation message must contains saved word, but it's not"
    
    @pytest.mark.exceptions
    def test_invalid_element_state_exception(self, driver):

        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click edit button
        edit_btn_locator = driver.find_element(By.ID, "edit_btn")
        edit_btn_locator.click()

        # Get row1 input element and clear it using an explicit wait to avoid run conditions errors
        row_1_input_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='row1']/input")))
        row_1_input_locator.clear()

        # Set a new text
        row_1_input_locator.send_keys("sushi")

        # Click save button
        save_btn_locator = driver.find_element(By.ID, "save_btn")
        save_btn_locator.click()

        # Check confirmation message is the expected one
        confirmation_locator = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert confirmation_locator.text == "Row 1 was saved", "Confirmation message must contains saved word, but it's not"

        # Check value of input element changed
        text = row_1_input_locator.get_attribute("value")
        assert text == "sushi", "The text must be sushi, but got " + text


    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):

        # Open the page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Push Add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()

        # Verify instructions text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, "instructions")), "Error waiting to element be disapear"), "The instructions element should disapear, but it's not"

    def open_url_and_click_add_button(self, driver):
        # Open the url
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click add button
        add_btn_locator = driver.find_element(By.ID, "add_btn")
        add_btn_locator.click()