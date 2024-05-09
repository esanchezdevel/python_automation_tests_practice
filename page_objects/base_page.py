from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException

class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        # The * before the locator means that the tuple is separated in different parameters
        # So, if the tuple is (By.ID, "my_id") with *locator, the method will receive two paramters
        # By.ID and "my_id" automatically. Very cool functionality of python.
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    # The time is an int with default value of 10
    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    # The arrow str indicates that the method must return and String
    # The @property annotation indicates that the method is only a property because it doesn't
    # have any logic and only returns a value
    @property
    def current_url(self) -> str:
        return self._driver.current_url
    
    # In this method we capture possible exceptions throws by _find method.
    # and if we capture the exception then return false
    def is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
        
    def open_url(self, url: str):
        self._driver.get(url)

    def get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text
