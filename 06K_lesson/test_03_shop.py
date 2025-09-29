from import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

@pytest.fixture
def test_buttons():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(16)

    user_name = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
    user_name.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, 'input#password')
    password.send_keys("secret_sauce")

    check_input = driver.find_element(By.CSS_SELECTOR, "#login-button")
    check_input.click()

    shop_input_1 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    shop_input_1.click()

    shop_input_2 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    shop_input_2.click()

    shop_input_3 = driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    shop_input_3.click()

    shopping_cart_link_input = driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link")
    shopping_cart_link_input.click()

    checkout_input = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout_input.click()

    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]')
    first_name.send_keys("Надежда")

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]')
    last_name.send_keys("Саратовцева")

    postal_code = driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]')
    postal_code.send_keys("403030")

    continue_input = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_input.click()

    text_prise = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
    text_prise_value = float(text_prise.split("$")[1])
    print(text_prise)

#total-label = driver.find_element(By.CSS_SELECTOR, "div.summary_total_label#text").text
    assert text_prise_value == 58.29

    driver.quit()
