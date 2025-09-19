from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path="C:\geckodriver-v0.36.0-win32\geckodriver.exe")

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(5)

input_field = driver.find_element(By.CSS_SELECTOR,"input")

input_field.send_keys("Sky")

sleep(5)

input_field.clear()

input_field.send_keys("Pro")

sleep(5)

driver.quit()