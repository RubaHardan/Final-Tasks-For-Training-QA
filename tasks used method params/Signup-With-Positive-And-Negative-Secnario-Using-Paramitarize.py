import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep
import sys


@pytest.fixture(params=[
    pytest.param({"emailsignup": "hardanruba34@gmail.com", "passwordsignup": "hardanrubA1234"}),
    pytest.param({"emailsignup": "rubahardan.com", "passwordsignup": "hardanrubA1234"}, marks=pytest.mark.fail(reason="Negative scenario test case: Invalid email format")),
    pytest.param({"emailsignup": "hardanruba34@gmail.com", "passwordsignup": "rrrrrrrggggg"}, marks=pytest.mark.xfail(reason="Negative scenario test case: Weak password")),
    pytest.param({"emailsignup": "rubahardan.com", "passwordsignup": "rrrrrrrggggg"}, marks=pytest.mark.fail(reason="Negative scenario test case: Invalid email format and weak password"))
])
def createaccount_data(request):
    return request.param



def test_create_account_positive_and_negative_scenario( driver_init_firefox, createaccount_data):
     driver = driver_init_firefox
     driver.get("https://magento.softwaretestingboard.com/")
     signuplink = driver.find_element(By.XPATH, "//header//li[2]/a")
     signuplink.send_keys(Keys.ENTER)

    # Explicit Wait for the First Name field
     wait = WebDriverWait(driver, 10)
     emailsignup_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
     emailsignup_field.send_keys(createaccount_data["emailsignup"])
     wait = WebDriverWait(driver, 10)
     passwordsignup_field = wait.until(EC.presence_of_element_located((By.NAME, "login[password]")))
     passwordsignup_field.send_keys(createaccount_data["passwordsignup"])


    # Explicit Wait for the Create an Account button
     signupbutton = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
     signupbutton.click()