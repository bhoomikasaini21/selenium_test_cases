from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)

wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))

assert "Username is required" in error_message.text

print("Test Passed")

driver.quit()