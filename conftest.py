import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)
    driver.get("https://uat.ushop.lk/")
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    # driver.quit()