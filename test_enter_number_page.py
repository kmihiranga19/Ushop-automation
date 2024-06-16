import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.mark.usefixtures("setup")
class TestEnterNumberPage:
    driver: WebDriver
    wait: WebDriverWait
    
    def test_enter_valid_number(self):
        self.driver.get("https://uat.ushop.lk/admin/otp")
        # self.wait.until(EC.visibility_of_element_located((By.ID, "phone-no"))).send_keys("0710431920")
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
        otp = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name = "otp"]')))

        assert otp is not None, "OTP input field was not found, test failed"





