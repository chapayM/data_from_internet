from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://matchtv.ru/')


actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH, "//div[@class='footer__sub-item footer__sub-item_contains_agreement']"))
actions.perform()

while True:
    wait = WebDriverWait(driver, 15)
    try:
        actions = ActionChains(driver)
        actions.move_to_element(driver.find_element(By.XPATH, "//div[@class='footer__sub-item footer__sub-item_contains_agreement']"))
        actions.perform()
        button = wait.until(EC.element_to_be_clickable((By.XPATH,
            "//div[@class='content-loader']//button[@class='reset-button button content-loader__button-element']")))
        button.click()
    except TimeoutException:
        print("Кнопку найти не удалось")
        break



print()
