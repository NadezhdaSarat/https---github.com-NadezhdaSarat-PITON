from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure



class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_field = (By.CSS_SELECTOR, '#delay')
        self.result_field = (By.CSS_SELECTOR, '#result')
        self.button_7 = (By.XPATH, '//span[text()="7"]')
        self.button_plus = (By.XPATH, '//span[text()="+"]')
        self.button_8 = (By.XPATH, '//span[text()="8"]')
        self.button_equal = (By.XPATH, '//span[text()="="]')


    @allure.step("Открыть сайт")
    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установить ожидание 45")
    def set_delay(self, delay):
        self.driver.find_element(*self.delay_field).clear()
        self.driver.find_element(*self.delay_field).send_keys(delay)

    @allure.step("Прокликать кнопки {button}")
    def click_button(self, button):
        self.driver.find_element(*button).click()

    @allure.step("Получить результат 15")
    def get_result(self):
        wait = WebDriverWait(self.driver, 46)
        wait.until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text