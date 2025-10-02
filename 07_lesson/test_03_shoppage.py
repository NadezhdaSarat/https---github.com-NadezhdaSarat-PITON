import pytest
from selenium import webdriver
from pages.shoppage import ShopPage

def test_shopping_scenario(self):
    self.shoppage = ShopPage(self.shoppage)
    self.shoppage.open()

    login_page = LoginPage(driver)
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
    checkout_page