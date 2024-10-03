from behave import given, when, then
from selenium import webdriver
from pages.login_Intu_page import LoginIntuPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By


@given('the user is on the intu login page')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.icesi.edu.co/moodle/login/index.php")
    context.login_Intu_page = LoginIntuPage(context.driver)
    
@when('the user logs Intu in with valid credentials')
def step_when_user_logs_in_valid(context):
    context.login_Intu_page.login("", "")
    
    
@then('the user should be redirected to the dashboard page')
def step_then_dashboard_page(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_top_bar_displayed()

