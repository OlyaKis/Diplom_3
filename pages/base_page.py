from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_element(locator).click()

    def send_keys(self, locator, value):
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(value)

    def is_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except Exception:
            return False

    def get_text(self, locator):
        return self.find_element(locator).text

    def wait_overlay_invisible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
        except Exception:
            pass

    def click(self, locator, reason=None, wait_timeout=10):
        self.wait_overlay_invisible(timeout=wait_timeout)
        WebDriverWait(self.driver, wait_timeout).until(EC.element_to_be_clickable(locator))
        self.find_element(locator).click()
