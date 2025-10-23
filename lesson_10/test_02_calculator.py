import allure
import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.id("Тест2 калькулятор")
@allure.story("Выполнить действия")
@allure.title("Действия с калькулятором")
@allure.description("Работа калькулятора")
def test_calculator_complement(driver):
    with allure.step("Открыть страницу калькулятора"):
        calculator = CalculatorPage(driver)
        calculator.open()
    with allure.step("Поставить время ожидания"):
        calculator.set_delay('1')
    with allure.step("Прокликать кнопки на калькуляторе"):
        calculator.click_button(calculator.button_7)
        calculator.click_button(calculator.button_plus)
        calculator.click_button(calculator.button_8)
        calculator.click_button(calculator.button_equal)

    with allure.step("Проверить результат"):
        assert calculator.get_result() == '15'



