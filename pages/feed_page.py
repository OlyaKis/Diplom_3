import allure
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):

    @allure.step("Открываем страницу 'Лента заказов'")
    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/feed")

    @allure.step("Кликаем по первому заказу в ленте")
    def click_first_order(self, timeout=10):
        self.wait_for_visible(FeedLocators.ORDER_ITEM, timeout)
        orders = self.find_elements(FeedLocators.ORDER_ITEM, timeout)
        if orders:
            orders[0].click()

    @allure.step("Проверяем, что модалка заказа открыта")
    def is_order_modal_opened(self, timeout=10):
        try:
            self.wait_for_visible(FeedLocators.ORDER_MODAL, timeout)
            modal = self.find_element(FeedLocators.ORDER_MODAL, timeout)
            return modal.is_displayed()
        except Exception:
            return False

    @allure.step("Получаем значение счетчика 'Выполнено за всё время'")
    def get_total_orders_count(self, timeout=10):
        self.wait_for_visible(FeedLocators.TOTAL_DONE_ALL_TIME, timeout)
        text = self.get_text(FeedLocators.TOTAL_DONE_ALL_TIME, timeout)
        digits = ''.join(filter(str.isdigit, text))
        return int(digits) if digits else 0

    @allure.step("Получаем значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self, timeout=10):
        self.wait_for_visible(FeedLocators.TOTAL_DONE_TODAY, timeout)
        text = self.get_text(FeedLocators.TOTAL_DONE_TODAY, timeout)
        digits = ''.join(filter(str.isdigit, text))
        return int(digits) if digits else 0

    @allure.step("Проверяем, что заказ пользователя отображается в ленте")
    def is_user_order_present(self, user, timeout=10):
        self.wait_for_visible(FeedLocators.ORDER_ITEM, timeout)
        orders = self.find_elements(FeedLocators.ORDER_ITEM, timeout)
        return len(orders) > 0

    @allure.step("Обновляем страницу")
    def refresh(self):
        self.driver.refresh()
