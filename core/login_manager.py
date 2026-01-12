import json
import time
from selenium.webdriver.common.by import By
from .browser import create_browser

PROFILES_PATH = "config/profiles.json"

def load_profiles():
    with open(PROFILES_PATH, "r") as f:
        return json.load(f)

def login(profile_name):
    profiles = load_profiles()

    if profile_name not in profiles:
        print("Profile not found.")
        return

    profile = profiles[profile_name]

    driver = create_browser()
    driver.get(profile["login_url"])

    time.sleep(2)

    driver.find_element(By.XPATH, profile["username_xpath"]).send_keys(profile["username"])
    driver.find_element(By.XPATH, profile["password_xpath"]).send_keys(profile["password"])
    driver.find_element(By.XPATH, profile["login_button_xpath"]).click()

    print(f"Logged into {profile_name} successfully.")

    time.sleep(5)
    driver.quit()
