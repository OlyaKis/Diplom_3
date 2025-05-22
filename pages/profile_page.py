import allure
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    @allure.step("Кликаем по кнопке выхода из профиля")
    def click_logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    @allure.step("Кликаем по кнопке 'Профиль'")
    def click_profile_button(self):
        self.wait_overlay_invisible()
        self.click(ProfileLocators.PROFILE_BUTTON)

    @allure.step("Кликаем по кнопке 'История заказов'")
    def click_order_history(self):
        self.wait_overlay_invisible()
        self.click(ProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Проверяем, что отображается кнопка 'История заказов'")
    def is_order_history_displayed(self):
        return self.is_visible(ProfileLocators.ORDER_HISTORY_BUTTON)

    @allure.step("Проверяем, что открыт профиль")
    def is_profile_opened(self):
        return "account" in self.get_current_url()

    @allure.step("Проверяем, что открыта история заказов")
    def is_order_history_opened(self):
        return self.get_current_url().endswith("/account/order-history")
