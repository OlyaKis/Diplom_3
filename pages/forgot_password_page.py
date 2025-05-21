from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    def fill_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    def submit_reset(self):
        self.click(ForgotPasswordLocators.RESET_BUTTON)
