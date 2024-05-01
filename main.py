# To run script with python using virtual environment we have to:
# 1. Create the virtual environment with Ctrl+Shift+P look for "python: create virtual environment"
# 2. Once the Virtual environment is created in .venv folder, choose as python interpreter the python of the virtual environment with
#    Ctrl+Shift+P look for "python: select interpreter" and choose the virtual environment already created

import time
from selenium import webdriver

# Test steps:
# -----------
# 1. Open Browser
driver = webdriver.Chrome()
time.sleep(5)

# 2. Go to webpage
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(10)
