import pytest
from selenium import webdriver
from CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_complement(driver):
    calculator = CalculatorPage(driver)
    calculator.open()
    calculator.set_delay('45')
    calculator.click_button(calculator.button_7)
    calculator.click_button(calculator.button_plus)
    calculator.click_button(calculator.button_8)
    calculator.click_button(calculator.button_equal)


    assert calculator.get_result() == '15'



