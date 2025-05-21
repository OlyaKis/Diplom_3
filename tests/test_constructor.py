import allure
import pytest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from utils.api_helper import create_test_user, delete_test_user
from utils.test_data import TestUser


@allure.epic("Основной функционал конструктора")
class TestConstructor:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.test_user = TestUser.generate()
        create_test_user(self.test_user)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(self.test_user.email, self.test_user.password)
        yield
        delete_test_user(self.test_user)

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert main_page.is_constructor_visible()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert "feed" in driver.current_url

    @allure.title("Открытие и закрытие всплывающего окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.click_first_ingredient()
        main_page.close_confirmation_modal()
        profile_page.click_profile_button()
        assert driver.current_url.endswith("/account/profile")

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_ingredient_counter_increase(self, driver):
        main_page = MainPage(driver)
        count_before = main_page.get_ingredient_counter()
        main_page.drag_bun_to_constructor()
        count_after = main_page.get_ingredient_counter()
        assert count_after == count_before + 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_make_order(self, driver):
        main_page = MainPage(driver)
        main_page.drag_bun_to_constructor()
        main_page.click_order_button()
        assert main_page.is_order_confirmation_modal_opened()
