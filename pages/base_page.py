import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ищем элемент по локатору")
    def find_element(self, locator, timeout=10):
        self.wait_for_visible(locator, timeout)
        return self.driver.find_element(*locator)

    @allure.step("Ищем все элементы по локатору")
    def find_elements(self, locator, timeout=10):
        self.wait_for_visible(locator, timeout)
        return self.driver.find_elements(*locator)

    @allure.step("Кликаем по элементу")
    def click(self, locator, reason=None, wait_timeout=10):
        self.wait_overlay_invisible(wait_timeout)
        self.wait_for_clickable(locator, wait_timeout)
        self.driver.find_element(*locator).click()

    @allure.step("Вводим значение в элемент")
    def send_keys(self, locator, value, timeout=10):
        elem = self.find_element(locator, timeout)
        elem.clear()
        elem.send_keys(value)

    @allure.step("Проверяем видимость элемента")
    def is_visible(self, locator, timeout=10):
        try:
            return self.wait_for_visible(locator, timeout).is_displayed()
        except Exception:
            return False

    @allure.step("Получаем текст элемента")
    def get_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    @allure.step("Ожидаем, что оверлей модалки станет невидимым")
    def wait_overlay_invisible(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr"))
            )
        except Exception:
            pass

    @allure.step("Ожидаем, что элемент станет видимым")
    def wait_for_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем, что элемент станет кликабельным")
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидаем, что элемент исчезнет")
    def wait_for_invisible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )
