import pytest
from selenium import webdriver

# Fixture to be executed before and after the tests execution
@pytest.fixture
def driver():
    print('Creating Chrome driver')
    mydriver = webdriver.Chrome();
    # Return the mydriver variable using the keyword yield. It's the same as return
    # But in this case all the things before the yield keywords are executed BEFORE the tests execution
    yield mydriver
    # And the things that are after the yield keyword, are executed AFTER the tests execution
    print('Closing Chrome driver')
    mydriver.quit()