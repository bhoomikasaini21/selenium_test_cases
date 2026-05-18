from selenium import webdriver
from selenium import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10)      

wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()               


wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
wait.until(EC.element_to_be_clickable((By.Class_NAME, "shopping_cart_link"))).click()
wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))).click()   

cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
assert cart_badge.text == "0" 

print("Item removed from cart successfully. Cart badge shows:", cart_badge.text)
print("Test passed")      

driver.quit()

