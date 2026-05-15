from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10)


wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()


wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

remove_button = wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack")))
remove_button.click()


cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
assert len(cart_badges) == 0

print("Test Passed")

driver.quit()