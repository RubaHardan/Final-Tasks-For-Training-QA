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


@pytest.mark.usefixtures("driver_init_chrome")
class BasicTest:
    pass


class Test_chrome(BasicTest):
    def test_createaacount_with_positive_secnario(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        Createanacountlink = self.driver.find_element(By.XPATH, "//header//li[3]/a")
        Createanacountlink.send_keys(Keys.ENTER)

        # Explicit Wait for the First Name field
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = self.driver.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = self.driver.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("hardanrubA1234")

        # Explicit Wait for the Create an Account button
        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        assert True, "Test Passed"




    def test_createaacount_with_negtive_secnario1_email_not_correct(self):

        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        Createanacountlink = self.driver.find_element(By.XPATH, "//header//li[3]/a")
        Createanacountlink.send_keys(Keys.ENTER)

        # Explicit Wait for the First Name field
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = self.driver.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("rubahardan.com")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = self.driver.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("hardanrubA1234")

        # Explicit Wait for the Create an Account button
        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        assert False, "Test failed"


    def test_createaacount_with_negtive_secnario2_password_not_correct(self):

        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        Createanacountlink = self.driver.find_element(By.XPATH, "//header//li[3]/a")
        Createanacountlink.send_keys(Keys.ENTER)

        # Explicit Wait for the First Name field
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = self.driver.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("rrrrrrrggggg")

        confirm_password_field = self.driver.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("rrrrrrrggggg")

        # Explicit Wait for the Create an Account button
        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        assert False, "Test failed"

    def test_createaacount_with_negtive_secnario3_confirm_password_not_correct(self):

        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        Createanacountlink = self.driver.find_element(By.XPATH, "//header//li[3]/a")
        Createanacountlink.send_keys(Keys.ENTER)

        # Explicit Wait for the First Name field
        wait = WebDriverWait(self.driver, 10)
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
        first_name_field.send_keys("RUBA")

        last_name_field = self.driver.find_element(By.NAME, "lastname")
        last_name_field.send_keys("Hardan")

        email_field = self.driver.find_element(By.NAME, "email")
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("hardanrubA1234")

        confirm_password_field = self.driver.find_element(By.NAME, "password_confirmation")
        confirm_password_field.send_keys("rrrrrrrggggg")

        # Explicit Wait for the Create an Account button
        create_account_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='form-validate']//button/span")))
        create_account_button.click()
        assert False, "Test failed"