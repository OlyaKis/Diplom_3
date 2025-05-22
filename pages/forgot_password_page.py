import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Заполняем e-mail")
    def fill_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Кликаем по кнопке восстановления пароля")
    def submit_reset(self):
        self.click(ForgotPasswordLocators.RESET_BUTTON)

    def is_reset_page_opened(self):
        return "forgot-password" in self.get_current_url()