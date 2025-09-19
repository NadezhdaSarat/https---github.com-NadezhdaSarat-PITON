from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
service = ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid/")
check_input = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
check_input.click()

sleep(5)

driver.get("http://uitestingplayground.com/dynamicid/")
check_input = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
check_input.click()

sleep(5)

driver.get("http://uitestingplayground.com/dynamicid/")
check_input = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
check_input.click()
sleep(5)


