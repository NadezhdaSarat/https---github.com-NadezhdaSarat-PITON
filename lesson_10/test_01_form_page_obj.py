import pytest
import allure
from selenium import webdriver
from FormPage import FormPage



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.story("Открыть сайт. Заполнить и отправить форму")
@allure.id("Test1")
@allure.title("Заполнение и отправка формы")
@allure.description("работа с формами")
def test_form_submission_flow(driver):
    with allure.step("Открыть страницу сайта"):
        form_page = FormPage(driver)
        form_page.open()
    with allure.step("Заполнить форму данными"):
        form_page.fill_form()
    with allure.step("Отправить форму"):
        form_page.submit_form()
        form_page.check_form_submission()