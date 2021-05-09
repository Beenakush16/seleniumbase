from selenium import webdriver
import pytest
import allure


driver = None
@pytest.fixture(scope='module')
def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="E:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.selenium.dev/")
    yield
    driver.quit()


@allure.description("Validates Page Title")
@allure.severity(severity_level="NORMAL")
@pytest.mark.usefixtures("test_setup")
def test_validTitle():
    assert driver.current_url == "https://www.selenium.dev/"


def test_skiptest():
    pytest.skip()
