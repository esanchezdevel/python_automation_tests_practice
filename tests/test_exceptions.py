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
        exceptions_page = ExceptionsPage(driver)

        # Open the page
        exceptions_page.open()
        # Modify the text of row1 input from Pizza to Sushi
        exceptions_page.modify_row1_input("Sushi")
        # Verify that the confirmation message is the expected one
        assert exceptions_page.confirmation_message == "Row 1 was saved", "Confirmation message must contains saved word, but it's not"

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exceptions_page = ExceptionsPage(driver)

        # Open the page
        exceptions_page.open()
        # Push Add button
        exceptions_page.add_second_row()
        # Verify instructions text element is no longer displayed
        assert not exceptions_page.are_instructions_displayed(), "The instructions element should dissapear, but it's still present"