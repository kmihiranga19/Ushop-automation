import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configuration.config


class Test_landing_page:
    driver = ''

    def setup(self):
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://uat.ushop.lk/")

    def test_d(self):
         
