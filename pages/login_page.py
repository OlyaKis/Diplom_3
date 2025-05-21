from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def open(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/login")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_INPUT)
        )

    def login(self, email, password):
        self.send_keys(LoginLocators.EMAIL_INPUT, email)
        self.send_keys(LoginLocators.PASSWORD_INPUT, password)
        self.click(LoginLocators.LOGIN_BUTTON)

    def click_forgot_password_link(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)
