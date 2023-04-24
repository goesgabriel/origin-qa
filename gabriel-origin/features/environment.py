from selenium import webdriver
# This file is to be used as HOOKS of the project


def before_all(context):
    # context to share 'web' among all steps
    context.web = webdriver.Chrome()


def after_step(context, step):
    pass


def after_scenario(context, scenario):
    pass


def after_all(context):
    context.web.quit()
