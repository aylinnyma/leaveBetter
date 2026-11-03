# features/environment.py
from selenium import webdriver

def before_all(context):
    # open the browser before testing
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)

def after_all(context):
    # close the browser
    context.browser.quit()