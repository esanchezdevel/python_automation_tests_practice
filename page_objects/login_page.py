from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage

class LoginPage(BasePage):

    __url = "https://practicetestautomation.com/practice-test-login/"

    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.XPATH, "//button[@class='btn']")
    __error_message = (By.ID, 'error')

    def __init__(self, driver: WebDriver):
        # Call to the superclass init method
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_login(self, username: str, password: str):
        # Input to username and password elements
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        
        # Click the submit button
        super()._click(self.__submit_button)

    @property
    def error_message(self) -> str:
        return super().get_text(self.__error_message, 3)