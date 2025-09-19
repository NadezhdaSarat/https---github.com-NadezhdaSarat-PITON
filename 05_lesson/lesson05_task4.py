from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/login")

sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")
sleep(2)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "#login > button")
login_button.click()

sleep(5)


success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
print("Оповещение об успехе:", success_message.text)


driver.quit()