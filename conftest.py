import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import configuration.config


@pytest.fixture(scope="function")
def setup_method(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)
    driver.get(configuration.config.BaseURL)
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.wait = wait

    yield