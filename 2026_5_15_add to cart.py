from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

wait = WebDriverWait(driver, 10)


wait.until(
    EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
add_to_cart_btn.click()


cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

assert cart_badge.text == "1"

print("Test Passed")

driver.quit()