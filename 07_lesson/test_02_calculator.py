import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_complement(self):
    self.calculator = CalculatorPage(self.calculator)
    self.calculator.open()
    self.calculator.set_delay('45')
    self.calculator.click_button(self.calculator.button_7)
    self.calculator.click_button(self.calculator.button_plus)
    self.calculator.click_button(self.calculator.button_8)
    self.calculator.click_button(self.calculator.button_equal)

    self.assertEqual(self.calculator.get_result(), '15')



