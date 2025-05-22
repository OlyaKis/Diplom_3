import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage


@allure.suite("Восстановление пароля")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password_link()
        assert "forgot-password" in login_page.get_current_url()

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_reset_password_submit(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password_link()
        reset_page = ForgotPasswordPage(driver)
        reset_page.fill_email("testuser@example.com")
        reset_page.submit_reset()
        assert reset_page.is_reset_page_opened()
