import pytest
from selenium import webdriver

# Fixture to be executed before and after the tests execution
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    print(f'Creating {browser} browser')
    if browser == 'chrome':
        mydriver = webdriver.Chrome()
    elif browser == 'firefox':
        mydriver = webdriver.Firefox()
    else:
        raise TypeError(f'Expected \'chrome\' or \'firefox\' but got \'{browser}\'')
    # Return the mydriver variable using the keyword yield. It's the same as return
    # But in this case all the things before the yield keywords are executed BEFORE the tests execution
    yield mydriver
    # And the things that are after the yield keyword, are executed AFTER the tests execution
    print('Closing Chrome driver')
    mydriver.quit()

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='browser to execute tests (chrome or firefox)')