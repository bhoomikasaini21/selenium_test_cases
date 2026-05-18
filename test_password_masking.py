from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.ewebdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expectec_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
webdriver_wait = WebDriverWait(driver, 10)


password_field = webdriver_wait.until(EC.visibility_of_element_loacted(By.ID, "password"))
password_field.send_keys("secret_sauce")

assert password_field.get_attribute("type") == "password"

print("Test passed")
driver.quit()
