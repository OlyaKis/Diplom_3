import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.epic("Раздел «Лента заказов»")
class TestFeed:

    @allure.title("Открытие всплывающего окна по клику на заказ")
    def test_click_order_opens_modal(self, driver, login_user):
        feed_page = FeedPage(driver)
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page.click_first_order()
        assert feed_page.is_order_modal_opened()

    @allure.title("Отображение заказов пользователя из «Истории заказов»")
    def test_user_orders_visible_in_feed(self, driver, login_user):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_user_order_present(login_user)

    @allure.title("Увеличение счётчика «Выполнено за всё время» после нового заказа")
    def test_total_orders_counter_increases(self, driver, login_user):
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
    def test_today_orders_counter_increases(self, driver, login_user):
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
    def test_order_appears_in_work_section(self, driver, login_user):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_user_order_present(login_user)
