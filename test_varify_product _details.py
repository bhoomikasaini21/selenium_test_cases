from selenium import webdriver
from selenium import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
webdriver_wait = WebDriverWait(driver, 10)

webdriver_wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
webdriver_wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
webdriver_wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()   

product_name = webdriver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
product_desc = webdriver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_desc")))
product_price = webdriver_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))) 

assert product_name.text != ""
assert product_desc.text != ""
assert "$" in product_price.text

print("Product Name:", product_name.text)
print("Product Description:", product_desc.text)
print("Product Price:", product_price.text)
print("Test passed")
driver.quit()   

