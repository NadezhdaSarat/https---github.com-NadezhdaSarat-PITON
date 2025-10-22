from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, '#delay')
        self.result_field = (By.CSS_SELECTOR, '#result')
        self.button_7 = (By.XPATH, '//button[text()="7"]')
        self.button_plus = (By.XPATH, '//button[text()="+"]')
        self.button_8 = (By.XPATH, '//button[text()="8"]')
        self.button_equal = (By.XPATH, '//button[text()="="]')


    @allure.step("Открыть сайт")
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить ожидание {delay_field}")
    def set_delay(self, delay):
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(delay)

    @allure.step("Прокликать кнопки {button}")
    def click_button(self, button):
        self.driver.find_element(*button).click()

    @allure.step("Получить результат {result}")
    def get_result(self):
        return self.driver.find_element(*self.result_field).text