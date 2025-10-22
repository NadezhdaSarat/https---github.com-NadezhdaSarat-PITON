import pytest
from selenium import webdriver
from ShopPage import LoginPage, MainPage, CartPage, CheckoutPage
import allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.id("Тест3 шоп")
@allure.story("Создание заказа")
@allure.title("Действия с заказами ШОП")
@allure.description("Создание и отправка заказа на ШОП")
def test_shopping_scenario(driver):
    with allure.step("Открыть страницу"):
        login_page = LoginPage(driver)
        login_page.open()
    with allure.step("Внести логин и пароль"):
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавить товары в корзину"):
        main_page = MainPage(driver)
        main_page.add_backpack()
        main_page.add_tshirt()
        main_page.add_onesie()
        main_page.go_to_cart()

    with allure.step("Перейти в корзину"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Оформить заказ"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_first_name("Nadezha")
        checkout_page.fill_last_name("Saratovceva")
        checkout_page.fill_postal_code("403031")