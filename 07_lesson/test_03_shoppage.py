import pytest
from selenium import webdriver
from ShopPage import LoginPage, MainPage, CartPage, CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()



def test_shopping_scenario(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()


    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_tshirt()
    main_page.add_onesie()
    main_page.go_to_cart()


    cart_page = CartPage(driver)
    cart_page.click_checkout()


    checkout_page = CheckoutPage(driver)
    checkout_page.fill_first_name("Nadezhda")
    checkout_page.fill_last_name("Saratovtceva")
    checkout_page.fill_postal_code("403030")