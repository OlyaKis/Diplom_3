import pytest
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.api_helper import create_test_user, delete_test_user
from utils.test_data import TestUser


@allure.epic("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_profile_page(self, driver, login_user):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        assert profile_page.is_profile_opened()

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver, login_user):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        profile_page.click_order_history()
        assert profile_page.is_order_history_opened()

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, login_user):
        profile_page = ProfilePage(driver)
        profile_page.click_profile_button()
        profile_page.click_logout()
        assert profile_page.is_profile_opened()
