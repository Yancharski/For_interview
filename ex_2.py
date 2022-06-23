from selenium.webdriver.common.by import By
from time import sleep


def test_ex_2(driver):
    driver.get('https://demoqa.com/')
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div[1]')
    element.click()
    check_box = driver.find_element(By.ID, 'item-1')
    check_box.click()
    galka_in_checkbox = driver.find_element(By.CSS_SELECTOR, 'span[class="rct-checkbox"]')
    galka_in_checkbox.click()
    sleep(3)
    radio_button = driver.find_element(By.ID, 'item-2')
    radio_button.click()
    impressive_in_radio = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]')
    yes_in_radio = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]')
    impressive_in_radio.click()
    sleep(3)
    yes_in_radio.click()

