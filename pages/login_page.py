import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        self.wait_for_visible(LoginLocators.EMAIL_INPUT, timeout=5)

    @allure.step("Выполняем логин с email")
    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    @allure.step("Переходим по ссылке 'Забыли пароль?'")
    def click_forgot_password_link(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)

    def is_login_opened(self):
        return "login" in self.get_current_url()
