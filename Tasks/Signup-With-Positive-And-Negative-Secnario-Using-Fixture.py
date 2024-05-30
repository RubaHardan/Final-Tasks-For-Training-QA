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


@pytest.mark.usefixtures("driver_init_firefox")
class BasicTest:
    pass


class Test_firefox(BasicTest):
    def test_signup_with_positive_secnario(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        signuplink = self.driver.find_element(By.XPATH, "//header//li[2]/a")
        signuplink.send_keys(Keys.ENTER)


        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = self.driver.find_element(By.NAME, "login[password]")
        password_field.send_keys("hardanrubA1234")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()
        assert True, "Test Passed"




    def test_signup_with_negtive_secnario1_email_not_correct(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        signuplink = self.driver.find_element(By.XPATH, "//header//li[2]/a")
        signuplink.send_keys(Keys.ENTER)


        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("rubahardan.com")

        password_field = self.driver.find_element(By.NAME, "login[password]")
        password_field.send_keys("hardanrubA1234")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()
        assert False, "Test failed"

    def test_signup_with_negtive_secnario2_password_not_correct(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        signuplink = self.driver.find_element(By.XPATH, "//header//li[2]/a")
        signuplink.send_keys(Keys.ENTER)


        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("hardanruba34@gmail.com")

        password_field = self.driver.find_element(By.NAME, "login[password]")
        password_field.send_keys("rrrrrrrggggg")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()
        assert False, "Test failed"
    def test_signup_with_negtive_secnario3_email_and_password_not_correct(self):
        self.driver.get('https://magento.softwaretestingboard.com/')
        self.driver.maximize_window()
        signuplink = self.driver.find_element(By.XPATH, "//header//li[2]/a")
        signuplink.send_keys(Keys.ENTER)


        wait = WebDriverWait(self.driver, 10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "login[username]")))
        email_field.send_keys("rubahardan.com")

        password_field = self.driver.find_element(By.NAME, "login[password]")
        password_field.send_keys("rrrrrrrggggg")


        signupbutton = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='send2']/span")))
        signupbutton.click()
        assert False, "Test failed"