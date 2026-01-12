from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_browser(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    
    driver = webdriver.Chrome(options=options)
    return driver
