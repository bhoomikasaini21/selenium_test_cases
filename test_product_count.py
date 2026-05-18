from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
webdriver_wait = WebDriverWait(driver, 10)

webdriver_wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
webdriver_wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
webdriver_wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()     

products = webdriver_wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
assert len(products) == 6

print(f"total product displayed on the page is: {len(products)}")
print("Test passed")
driver.quit()   