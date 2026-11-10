from selenium import webdriver

def before_all(context):
    # This will launch the Chrome browser before tests start
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)

def after_all(context):
    # This will close the browser after tests finish
    context.browser.quit()