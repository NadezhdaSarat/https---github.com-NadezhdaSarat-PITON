import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(50)
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Ввод название фильма")
@allure.severity("critical")
def test_form_movies(browser):
    with allure.step("Открыть страницу сайта"):
        browser.get("https://www.kinopoisk.ru/")
        browser.find_element(By.NAME, "kp_query").send_keys("Алиса в Стране чудес")
    with allure.step("проверка результата"):
        assert browser.find_element(By.ID, 'suggest-item-film-6218104').is_displayed()

@allure.title("Выбор фильма из списка ")
@allure.description("Ввод название фильма")
@allure.severity("critical")
def test_movi_page(browser):
    with allure.step("Открыть страницу сайта"):
        browser.get("https://www.kinopoisk.ru/")
    with allure.step("ввести данные в поиск"):
        browser.find_element(By.NAME, "kp_query").send_keys("Алиса в Стране чудес")
        browser.find_element(By.ID, 'suggest-item-film-6218104').click()
    with allure.step("проверить результат"):
        assert  browser.find_element(By.CSS_SELECTOR, '[data-tid="75209b22"]').text == "Алиса в Стране чудес (2025)"

@allure.title("Поиск актера по фамилии")
@allure.description("Ввод фамилия")
@allure.severity("critical")
def test_form_actor(browser):
    with allure.step("Открыть страницу сайта"):
        browser.get("https://www.kinopoisk.ru/")
    with allure.step("ввести фамилию"):
        browser.find_element(By.NAME, "kp_query").send_keys("Пересильд")
    with allure.step("проверить результат"):
        assert browser.find_element(By.ID, 'suggest-item-person-4583902').is_displayed()

@allure.title("Выбор актера из списка")
@allure.description("Ввод имя, фамилия")
@allure.severity("critical")
def test_movi_actor(browser):
    with allure.step("Открыть страницу сайта"):
        browser.get("https://www.kinopoisk.ru/")
    with allure.step("ввести имя и фамилию"):
        browser.find_element(By.NAME, "kp_query").send_keys("Анна Пересильд")
        browser.find_element(By.ID, 'suggest-item-person-4583902').click()
    with allure.step("проверить результат"):
        assert  browser.find_element(By.CSS_SELECTOR, '[data-tid="f22e0093"]').text == "Анна Пересильд"

@allure.title("Поиск по набору букв")
@allure.description("Ввод буквы")
@allure.severity("critical")
def test_negative_form(browser):
    with allure.step("Открыть страницу сайта"):
        browser.get("https://www.kinopoisk.ru/")
    with allure.step("ввести набор букв"):
        browser.find_element(By.NAME, "kp_query").send_keys("hgfh")
    with allure.step("проверить результат"):
        assert browser.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"


