from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    if "web" in scenario.feature.filename.lower():
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--user-data-dir=/tmp/chrome_profile_{}".format(id(context)))
        context.driver = webdriver.Chrome(options=chrome_options)

def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
