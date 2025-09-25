from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.implicitly_wait(40)
driver.get(" https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#landscape")))


images = driver.find_elements(By.TAG_NAME, "img")


if len(images) >= 3:
    src_third_image = images[3].get_attribute("src")
    print(f"Src:{src_third_image}")
else:
    print("Меньше 3-х изображений")

driver.quit()