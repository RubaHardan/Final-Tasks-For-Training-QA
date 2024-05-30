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
    pytest.param({"First Name": "RUBA", "Last Name": "Hardan", "Email": "hardanruba34@gmail.com", "Password": "hardanrubA1234", "Confirm Password": "hardanrubA1234"}),
    pytest.param({"First Name": "RUBA", "Last Name": "Hardan", "Email": "rubahardan.com", "Password": "hardanrubA1234", "Confirm Password": "hardanrubA1234"}, marks=pytest.mark.xfail(reason="Negative scenario test case")),
    pytest.param({"First Name": "RUBA", "Last Name": "Hardan", "Email": "hardanruba34@gmail.com", "Password": "rrrrrrrggggg", "Confirm Password": "rrrrrrrggggg"}, marks=pytest.mark.xfail(reason="Negative scenario test case")),
    pytest.param({"First Name": "RUBA", "Last Name": "Hardan", "Email": "hardanruba34@gmail.com", "Password": "rrrrrrrggggg", "Confirm Password": "4t4t4t4t4t"}, marks=pytest.mark.xfail(reason="Negative scenario test case"))
])
def createaccount_data(request):
    return request.param



def test_create_account_positive_and_negative_scenario( driver_init_chrome, createaccount_data):

     driver_init_chrome.get("https://magento.softwaretestingboard.com/")
     Create_an_acount_link = driver_init_chrome.find_element(By.XPATH, "//header//li[3]/a")
     Create_an_acount_link.send_keys(Keys.ENTER)

    # Explicit Wait for the First Name field
     wait = WebDriverWait(driver_init_chrome, 10)
     first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
     first_name_field.send_keys(createaccount_data["First Name"])

     last_name_field = driver_init_chrome.find_element(By.NAME, "lastname")
     last_name_field.send_keys(createaccount_data["Last Name"])

     email_field = driver_init_chrome.find_element(By.NAME, "email")
     email_field.send_keys(createaccount_data["Email"])

     password_field = driver_init_chrome.find_element(By.NAME, "password")
     password_field.send_keys(createaccount_data["Password"])

     confirm_password_field = driver_init_chrome.find_element(By.NAME, "password_confirmation")
     confirm_password_field.send_keys(createaccount_data["Confirm Password"])

    # Explicit Wait for the Create an Account button
     create_account_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
     create_account_button.click()