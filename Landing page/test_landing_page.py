import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration.config


class TestLandingPage:
    def setup_method(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(configuration.config.BaseURL)
        self.driver.maximize_window()

    def test_navigate_correct_page(self):
        get_started_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Get Started']")))
        if get_started_btn:
            print("Successfully loaded page")
        self.driver.quit()

    def test_buttons_work(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Get Started']"))).click()
        enter_mobile_number = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Enter your mobile number.']")))
        if enter_mobile_number:
            print("Get Started button work")
            self.driver.back()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Sign in']"))).click()
        enter_mobile_number = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Enter your mobile number.']")))
        if enter_mobile_number:
            print("Sign in button work")
            self.driver.back()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Sign up']"))).click()
        enter_mobile_number = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[normalize-space()='Enter your mobile number.']")))
        if enter_mobile_number:
            print("Sign up button work")
            self.driver.back()
        self.driver.quit()








