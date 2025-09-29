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
def test_buttons():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(16)

    first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")

    zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
    zip_code.send_keys("")

    city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")

    email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number.send_keys("+7985899998787")

    job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")

    check_input = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
    check_input.click()

    WebDriverWait(driver, 10).until(
        lambda driver: driver.find_element(By.ID, "zip_code_field_id").value_of_css_property(
            "background-color") == "rgba(255, 0, 0, 1)"
    )

    for field in fields:
        zip_field = driver.find_element(By.CSS_SELECTOR,'[name="zip-code"]').value_of_css_property(field)
    assert zip_field == "rgb(248, 215, 218)"
    fields = ["first-name", "last-name", "address", "email", "phone", "city", "country", "job", "company"]

    for field in fields:
        taps = driver.find_element(By.CSS_SELECTOR, "form-label").value_of_css_property(field)
    assert taps == "rgb(209, 231, 221)"

driver.quit()