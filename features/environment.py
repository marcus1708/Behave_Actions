from selenium import webdriver

def before_scenario(context, scenario):
  if "web" in scenario.feature.filename.lower():
    context.driver = webdriver.Chrome()

def after_scenario(context, scenario):
  if hasattr(context, "driver"):
    context.driver.quit()
