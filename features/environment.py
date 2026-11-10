<<<<<<< HEAD
from selenium import webdriver

def before_all(context):
    # This will launch the Chrome browser before tests start
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(5)

def after_all(context):
    # This will close the browser after tests finish
    context.browser.quit()
=======
# features/environment.py

def before_all(context):
    # Browser only when we run: behave -D browser=chrome
    context.use_browser = context.config.userdata.get("browser") == "chrome"
    if context.use_browser:
        from selenium import webdriver
        context.browser = webdriver.Chrome()
        context.browser.implicitly_wait(5)


def after_all(context):
    if getattr(context, "use_browser", False):
        context.browser.quit()
>>>>>>> 6626d1b1980a2227c62061565f330f0bbfe67896
