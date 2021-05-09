from selenium import webdriver
import pytest

driver = webdriver.Chrome(executable_path="E:\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://www.selenium.dev/")
print(driver.title)
assert "Browser" in driver.title
driver.quit()