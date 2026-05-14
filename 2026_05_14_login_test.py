from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")

# Maximize window
driver.maximize_window()

# Enter username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Enter password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Click login button
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for page load
time.sleep(3)

# Verify login success
current_url = driver.current_url

if "inventory" in current_url:
    print("TEST CASE PASSED")
else:
    print("TEST CASE FAILED")

# Close browser
driver.quit()