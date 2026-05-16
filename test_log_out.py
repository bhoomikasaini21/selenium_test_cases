from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.maximize_window()
wait =WebDriverWait(driver,10)

wait.until(EC.visibility_of_element_located((By.ID,"user-name"))).send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()       

wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
wait.until(EC.element_to_be_clickable(By.ID,"Logout_sidebar_link")).click()

assert driver.current_url == "https://www.saucedemo.com/"

print("test passed")

driver.quit()