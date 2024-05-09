from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/logged-in-successfully/"

    __header_field = (By.TAG_NAME, "h1")
    __log_out_button_field = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
    
    @property
    def expected_url(self) -> str:
        return self._url
    
    @property
    def header(self) -> str:    
        return super().get_text(self.__header_field)

    def is_logout_button_displayed(self) -> bool:
        return super().is_displayed(self.__log_out_button_field)