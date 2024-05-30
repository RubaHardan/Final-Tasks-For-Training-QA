import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver_init_chrome():
    web_driver = webdriver.Chrome()
    yield web_driver
    web_driver.quit()

@pytest.fixture(scope="function")
def driver_init_firefox():
    web_driver = webdriver.Firefox()
    yield web_driver
    web_driver.quit()