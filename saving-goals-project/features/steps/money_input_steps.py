from behave import when, then, given
from selenium.webdriver.common.by import By
from time import sleep


@when('the user inputs "{valid_money_amount}" in the total amount field')
@given('the user inputs "{valid_money_amount}" in the total amount field')
def step_impl(context, valid_money_amount):
    context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']").send_keys(valid_money_amount)
    sleep(5)


@then('the value that should appear is "{formatted_as_money}"')
def step_impl(context, formatted_as_money):
    element = context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']")
    text = element.get_attribute("value")
    sleep(5)
    assert text == formatted_as_money


@when('the user inputs "{non_numeric_character}" in the total amount field using the keyboard')
def step_impl(context, non_numeric_character):
    context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']").send_keys(non_numeric_character)
    sleep(5)


@when('the user edits the total amount field value to "{new_value}" using the keyboard')
def step_impl(context, new_value):
    context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']").clear()
    context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']").send_keys(new_value)
    sleep(5)


@then('the input should be rejected and not appear in the field')
def step_impl(context):
    element = context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']")
    text = element.get_attribute("value")
    sleep(5)
    assert text == ""
