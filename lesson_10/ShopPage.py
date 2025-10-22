from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("ВВести логин {username}")
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    @allure.step("Ввести пароль {password}")
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    @allure.step("Авторизоваться")
    def click_login(self):
        self.driver.find_element(*self.login_button).click()


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.backpack_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.tshirt_btn = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.onesie_btn = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_btn = (By.CSS_SELECTOR, "#shopping_cart_container button")

    @allure.step("Выбрать товар1")
    def add_backpack(self):
        self.driver.find_element(*self.backpack_btn).click()

    @allure.step("Выбрать товар2")
    def add_tshirt(self):
        self.driver.find_element(*self.tshirt_btn).click()

    @allure.step("Выбрать товар3")
    def add_onesie(self):
        self.driver.find_element(*self.onesie_btn).click()

    @allure.step("Посмотреть на корзину")
    def go_to_cart(self):
        self.driver.find_element(*self.cart_btn).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Перейти в корзину")
    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.total_price = (By.CSS_SELECTOR, "#total_price_value")

    @allure.step("Ввести в форму имя {first_name}")
    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    @allure.step("Ввести в форму фамилию {last_name}")
    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    @allure.step("Ввести в форму индекс {postal.code}")
    def fill_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)

    @allure.step("Отправить заказ")
    def get_total_price(self):
        return self.driver.find_element(*self.total_price).text