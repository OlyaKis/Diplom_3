from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    def click_first_order(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(FeedLocators.ORDER_ITEM)
        )
        orders = self.driver.find_elements(*FeedLocators.ORDER_ITEM)
        if orders:
            orders[0].click()

    def is_order_modal_opened(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(FeedLocators.ORDER_MODAL)
            )
            modal = self.driver.find_element(*FeedLocators.ORDER_MODAL)
            return modal.is_displayed()
        except Exception:
            return False

    def get_total_orders_count(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(FeedLocators.TOTAL_DONE_ALL_TIME)
        )
        text = self.get_text(FeedLocators.TOTAL_DONE_ALL_TIME)
        digits = ''.join(filter(str.isdigit, text))
        return int(digits) if digits else 0

    def get_today_orders_count(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(FeedLocators.TOTAL_DONE_TODAY)
        )
        text = self.get_text(FeedLocators.TOTAL_DONE_TODAY)
        digits = ''.join(filter(str.isdigit, text))
        return int(digits) if digits else 0

    def is_user_order_present(self, user, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(FeedLocators.ORDER_ITEM)
        )
        orders = self.driver.find_elements(*FeedLocators.ORDER_ITEM)
        return len(orders) > 0

    def refresh(self):
        self.driver.refresh()
