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
