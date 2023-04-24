from behave import given, when, then
from selenium.webdriver.common.by import By


@given('the user is on the saving goal page')
def step_impl(context):
    context.web.get('http://qa-assignment.useorigin.com.s3-website-us-east-1.amazonaws.com/')


@then('the confirm button should be visible on the screen')
def step_impl(context):
    assert context.web.find_element(By.XPATH, "//button[@class='sc-gKclnd ffjNtQ']")


@when('the user clicks on the confirm button')
def step_impl(context):
    context.web.find_element(By.XPATH, "//button[@class='sc-gKclnd ffjNtQ']").click


@then('nothing should happen')
def step_impl(context):
    # in this case, the Home page title should be visible/present
    # so it means that the click in Confirm button did not redirect to other page
    assert context.web.find_element(By.XPATH, "//h1[@class='sc-dkPtRN jnuFIW']")
