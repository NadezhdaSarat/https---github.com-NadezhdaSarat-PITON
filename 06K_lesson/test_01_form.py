from import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
#edge_driver_path = r"C:\edgedriver_win64\msedgedriver.exe"
#driver = webdriver.Edge(service=EdgeService(edge_driver_path))
options = webdriver.EdgeOptions()
driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install(), options=options)



@pytest.fixture
def browser():
    driver = webdriver.Edge
    yield driver
    driver quit()

def test_form(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def test_form(browser):
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        browser.find_element(By.NAME, "first-name").send_keys("Иван")
        browser.find_element(By.NAME, "last-name").send_keys("Петров")
        browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
        browser.find_element(By.NAME, "city").send_keys("Москва")
        browser.find_element(By.NAME, "country").send_keys("Россия")
        browser.find_element(By.NAME, "job-position").send_keys("QA")
        browser.find_element(By.NAME, "company").send_keys("SkyPro")
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        zip_code_field = browser.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code_field.get_attribute("class")

        green_fields = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]
        for field in green_fields:
            el = browser.find_element(By.ID, field)
            assert "alert-success" in el.get_attribute("class")