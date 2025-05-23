import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.epic("Основной функционал конструктора")
class TestConstructor:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.click_constructor()
        assert main_page.is_constructor_visible()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.click_order_feed()
        assert main_page.is_feed_opened()

    @allure.title("Открытие и закрытие всплывающего окна с деталями ингредиента")
    def test_ingredient_details_modal(self, driver, login_user):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.click_first_ingredient()
        main_page.close_confirmation_modal()
        profile_page.click_profile_button()
        assert profile_page.is_profile_opened()

    @allure.title("Увеличение счётчика ингредиента при добавлении")
    def test_ingredient_counter_increase(self, driver, login_user):
        main_page = MainPage(driver)
        count_before = main_page.get_ingredient_counter()
        main_page.drag_bun_to_constructor()
        count_after = main_page.get_ingredient_counter()
        assert count_after == count_before + 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_make_order(self, driver, login_user):
        main_page = MainPage(driver)
        main_page.drag_bun_to_constructor()
        main_page.click_order_button()
        assert main_page.is_order_confirmation_modal_opened()
