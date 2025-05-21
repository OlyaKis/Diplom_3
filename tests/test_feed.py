import pytest
import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from utils.api_helper import create_test_user, delete_test_user, create_order
from utils.test_data import TestUser


@allure.epic("Раздел «Лента заказов»")
class TestFeed:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.test_user = TestUser.generate()
        create_test_user(self.test_user)
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(self.test_user.email, self.test_user.password)
        yield
        delete_test_user(self.test_user)

    @allure.title("Открытие всплывающего окна по клику на заказ")
    def test_click_order_opens_modal(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page.click_first_order()
        assert feed_page.is_order_modal_opened()

    @allure.title("Отображение заказов пользователя из «Истории заказов»")
    def test_user_orders_visible_in_feed(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_user_order_present(self.test_user)

    @allure.title("Увеличение счётчика «Выполнено за всё время» после нового заказа")
    def test_total_orders_counter_increases(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        feed_page.open()
        initial_count = feed_page.get_total_orders_count()
        main_page.click_constructor()
        main_page.make_order()
        main_page.close_confirmation_modal()
        feed_page.open()
        new_count = feed_page.get_total_orders_count()
        assert new_count > initial_count

    @allure.title("Увеличение счётчика «Выполнено за сегодня» после нового заказа")
    def test_today_orders_counter_increases(self, driver):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        feed_page.open()
        initial_count = feed_page.get_today_orders_count()
        main_page.click_constructor()
        main_page.make_order()
        main_page.close_confirmation_modal()
        feed_page.open()
        new_count = feed_page.get_today_orders_count()
        assert new_count > initial_count

    @allure.title("Оформленный заказ появляется в разделе «В работе»")
    def test_order_appears_in_work_section(self, driver):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_user_order_present(self.test_user)
