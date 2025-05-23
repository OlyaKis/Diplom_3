import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site"

    @allure.step("Открываем главную страницу конструктора бургеров")
    def open(self):
        self.go(self.URL)
        self.wait_for_load()

    @allure.step("Ожидаем загрузки ингредиентов на главной")
    def wait_for_load(self, timeout=10):
        self.wait_for_visible(MainPageLocators.INGREDIENTS, timeout)

    @allure.step("Переходим во вкладку 'Конструктор'")
    def click_constructor(self):
        self.click(BaseLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Проверяем, что виден конструктор")
    def is_constructor_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENTS)

    @allure.step("Переходим во вкладку 'Лента заказов'")
    def click_order_feed(self):
        self.click(BaseLocators.FEED_BUTTON)

    @allure.step("Кликаем по первому ингредиенту")
    def click_first_ingredient(self):
        self.wait_for_ingredients()
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if not ingredients:
            raise Exception("Не найдено ни одного ингредиента")
        ingredients[0].click()

    @allure.step("Проверяем видимость модального окна ингредиента")
    def is_ingredient_modal_visible(self, timeout=5):
        try:
            self.wait_for_visible(MainPageLocators.INGREDIENT_DETAILS_MODAL, timeout)
            return True
        except Exception:
            return False

    @allure.step("Проверяем, что модальное окно ингредиента открыто")
    def is_ingredient_modal_opened(self):
        return self.is_ingredient_modal_visible()

    @allure.step("Ожидаем открытия модалки подтверждения заказа")
    def wait_for_confirmation_modal_open(self, timeout=10):
        self.wait_for_visible(MainPageLocators.ORDER_MODAL, timeout)
        self.wait_for_visible(MainPageLocators.CLOSE_BUTTON, timeout)

    @allure.step("Ожидаем закрытия модалки подтверждения заказа")
    def wait_for_confirmation_modal_close(self, timeout=10):
        self.wait_for_invisible(MainPageLocators.ORDER_MODAL, timeout)

    @allure.step("Получаем каунтер ингредиента")
    def get_ingredient_counter(self):
        counters = self.find_elements(MainPageLocators.INGREDIENT_COUNTER)
        if counters and counters[0].text.isdigit():
            return int(counters[0].text)
        return 0

    @allure.step("Перетаскиваем первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        time.sleep(3)
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if not ingredients:
            raise Exception("Не найдено ни одного ингредиента")
        target = self.find_element(MainPageLocators.INGREDIENTS)
        self.drag_and_drop(ingredients[0], target)

    @allure.step("Оформляем заказ")
    def make_order(self):
        self.drag_first_ingredient_to_constructor()
        self.drag_bun_to_constructor()
        self.click_order_button()
        self.wait_for_confirmation_modal_open()

    @allure.step("Закрываем модалку подтверждения заказа")
    def close_confirmation_modal(self, timeout=10):
        close_btn = self.wait_for_clickable(MainPageLocators.CLOSE_BUTTON, timeout)
        try:
            close_btn.click()
        except Exception:
            self.execute_script("arguments[0].click();", close_btn)
        self.wait_for_invisible(MainPageLocators.ORDER_MODAL, timeout)

    @allure.step("Перетаскиваем булку в конструктор")
    def drag_bun_to_constructor(self):
        self.wait_for_visible(MainPageLocators.BUN_ITEM, 5)
        buns = self.find_elements(MainPageLocators.BUN_ITEM)
        if not buns:
            raise Exception("Булка не найдена!")
        self.wait_for_visible(MainPageLocators.CONSTRUCTOR_DROP_AREA, 5)
        drop_area = self.find_element(MainPageLocators.CONSTRUCTOR_DROP_AREA)
        ActionChains(self.driver).drag_and_drop(buns[0], drop_area).perform()

    @allure.step("Кликаем на кнопку 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Проверяем открытие модалки подтверждения заказа")
    def is_order_confirmation_modal_opened(self):
        try:
            self.wait_for_visible(MainPageLocators.ORDER_MODAL, 10)
            return True
        except Exception:
            return False

    @allure.step("Закрываем модальное окно")
    def close_modal(self, timeout=5):
        close_btn = self.wait_for_clickable(MainPageLocators.CLOSE_BUTTON, timeout)
        close_btn.click()

    @allure.step("Ожидаем загрузку ингредиентов")
    def wait_for_ingredients(self, timeout=10):
        self.wait_for_visible(MainPageLocators.INGREDIENT_ITEM, timeout)

    @allure.step("Drag and drop: перетаскиваем элемент")
    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step("Проверяем, что сейчас открыта лента заказов")
    def is_feed_opened(self):
        return "feed" in self.get_current_url()

    @allure.step("Проверяем, что открыт конструктор")
    def is_constructor_opened(self):
        url = self.get_current_url()
        return url == self.URL or "/constructor" in url
