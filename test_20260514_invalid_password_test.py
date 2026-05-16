from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


driver.maximize_window()


driver.find_element(By.ID, "user-name").send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("wrong_password")

driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)

error_message = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
)


if "Username and password do not match" in error_message.text:
    print("TEST CASE PASSED")
else:
    print("TEST CASE FAILED")


driver.quit()