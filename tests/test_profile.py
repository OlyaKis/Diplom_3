import pytest
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.api_helper import create_test_user, delete_test_user
from utils.test_data import TestUser


@allure.epic("Личный кабинет")
class TestProfile:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.test_user = TestUser.generate()
        create_test_user(self.test_user)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(self.test_user.email, self.test_user.password)
        yield
        delete_test_user(self.test_user)

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_profile_page(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account"

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        profile_page.click_order_history()
        assert driver.current_url.endswith("/account/order-history")

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        profile_page.click_logout()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
