from import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

@pytest.fixture
def test_calculator():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    driver.find_element(By.CSS_SELECTOR, '#delay').clear()
    driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

#WebDriverWait(driver, 80).until(EC.text_to_be_present_in_element(By.CSS_SELECTOR, ".screen"))
    WebDriverWait(driver, 80).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

res = driver.find_element(By.CSS_SELECTOR, ".screen").text
assert res == "15"


