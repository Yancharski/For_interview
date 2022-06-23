import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('start-maximized')
    service = Service(executable_path='/Users/vlad_yancharski/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)
    yield driver
    sleep(3)
    driver.quit()
