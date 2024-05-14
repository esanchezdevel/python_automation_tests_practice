import time
from behave import *

from selenium import webdriver
from selenium.webdriver.common.by import By

login_url = "https://www.caratlane.com/login"

@given("Launching chrome BaseBrowser")
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when("Open caratlane Login page")
def openLoginUrl(context):
    context.driver.maximize_window()
    context.driver.get(login_url)

@when("Enter username \"{email}\"")
def enterUsername(context, email):
    context.driver.find_element(by=By.XPATH, value="//*[@name='emailMobile']").send_keys(email)

@when("click continue to login button")
def click_continue_to_login_cta(context):
    context.driver.find_element(by=By.XPATH, value="//*[text()='CONTINUE_TO_LOGIN']").click()

@when("Enter Password \"{password}\"")
def enter_password(context, password):
    print(f"-->{password}")
    time.sleep(5)
    context.driver.find_element(by=By.XPATH, value="//*[@name='password']").send_keys(password)

#@when("click on the Login Button")

#@then("user must logined successfully")