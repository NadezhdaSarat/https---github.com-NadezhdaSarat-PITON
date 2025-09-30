import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    yield driver
    driver.quit()

def test_shop(browser):
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    browser.find_element(By.ID, "checkout").click()
    browser.find_element(By.ID, "first-name").send_keys("Надежда")
    browser.find_element(By.ID, "last-name").send_keys("Саратовцева")
    browser.find_element(By.ID, "postal-code").send_keys("403030")
    browser.find_element(By.ID, "continue").click()
    total = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
    total_value = float(total.split("$")[1])
    assert total_value == 58.29