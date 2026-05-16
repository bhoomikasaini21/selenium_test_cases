from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.maximize_window()


username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")


password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")


login_button = driver.find_element(By.ID, "login-button")
login_button.click()


time.sleep(3)
current_url = driver.current_url

if "inventory" in current_url:
    print("TEST CASE PASSED")
else:
    print("TEST CASE FAILED")

driver.quit()
