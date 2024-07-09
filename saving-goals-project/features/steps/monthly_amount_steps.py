from behave import when, then, given
from selenium.webdriver.common.by import By
from time import sleep


@given('the "total amount" field value is "{total_amount_equal_to}"')
def step_impl(context, total_amount_equal_to):
    context.web.find_element(By.XPATH, "//input[@class='sc-eCImPb fQhPco']").send_keys(total_amount_equal_to)
    sleep(5)


@when('the month on "reach goal by" component is the "{month}"')
def step_impl(context, month):
    if month == 'current month':
        pass
    elif month == 'next month':
        context.web.find_element(By.XPATH, '//*[name()="svg" and @class="sc-furwcr gfjHRP"]').click()
    elif month == 'next month +2':
        number_of_clicks = [0, 1, 2]
        for n in number_of_clicks:
            context.web.find_element(By.XPATH, '//*[name()="svg" and @class="sc-furwcr gfjHRP"]').click()
            sleep(3)


@then('the "monthly amount" field value is "{monthly_amount_equal_to}"')
def step_impl(context, monthly_amount_equal_to):
    element = context.web.find_element(By.XPATH, '//p[@class="sc-hKwDye ldRKEV"]')
    text = element.get_attribute('outerText')
    sleep(5)
    assert text == "$"+monthly_amount_equal_to
