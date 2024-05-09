from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginSuccessfullyPage:
    _url = "https://practicetestautomation.com/logged-in-successfully/"

    __header_field = (By.TAG_NAME, "h1")
    __log_out_button_field = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    # The arrow str indicates that the method must return and String
    # The @property annotation indicates that the method is only a property because it doesn't
    # have any logic and only returns a value
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    @property
    def expected_url(self) -> str:
        return self._url
    
    @property
    def header(self) -> str:
        return self._driver.find_element(self.__header_field).text

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(self.__log_out_button_field).is_displayed()
