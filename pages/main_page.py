from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.base_locators import BaseLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class MainPage(BasePage):
    URL = "https://stellarburgers.nomoreparties.site"

    def open(self):
        self.driver.get(self.URL)
        self.wait_for_load()

    def wait_for_load(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENTS)
        )

    def click_constructor(self):
        self.click(BaseLocators.CONSTRUCTOR_BUTTON)

    def is_constructor_visible(self):
        return self.is_visible(MainPageLocators.INGREDIENTS)

    def click_order_feed(self):
        self.click(BaseLocators.FEED_BUTTON)

    def click_first_ingredient(self):
        self.wait_for_ingredients()
        ingredients = self.find_elements(MainPageLocators.INGREDIENT_ITEM)
        if not ingredients:
            raise Exception("Не найдено ни одного ингредиента")
        ingredients[0].click()

    def is_ingredient_modal_visible(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS_MODAL)
            )
            return True
        except Exception:
            return False

    def is_ingredient_modal_opened(self):
        return self.is_ingredient_modal_visible()

    def wait_for_confirmation_modal_open(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(MainPageLocators.CLOSE_BUTTON)
        )

    def wait_for_confirmation_modal_close(self, timeout=10):
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )

    def get_ingredient_counter(self):
        counters = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        if counters and counters[0].text.isdigit():
            return int(counters[0].text)
        return 0

    def drag_first_ingredient_to_constructor(self):
        time.sleep(3)
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT_ITEM)
        print(f"Найдено ингредиентов: {len(ingredients)}")
        if not ingredients:
            raise Exception("Не найдено ни одного ингредиента")
        target = self.find_element(MainPageLocators.INGREDIENTS)
        self.drag_and_drop(ingredients[0], target)

    def make_order(self):
        self.drag_first_ingredient_to_constructor()
        self.drag_bun_to_constructor()
        self.click_order_button()
        self.wait_for_confirmation_modal_open()

    def close_confirmation_modal(self, timeout=10):
        close_btn = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainPageLocators.CLOSE_BUTTON)
        )
        try:
            close_btn.click()
        except Exception as e:
            self.driver.execute_script("arguments[0].click();", close_btn)
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )

    def drag_bun_to_constructor(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(MainPageLocators.BUN_ITEM)
        )
        buns = self.driver.find_elements(*MainPageLocators.BUN_ITEM)
        if not buns:
            raise Exception("Булка не найдена!")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(MainPageLocators.CONSTRUCTOR_DROP_AREA)
        )
        drop_area = self.driver.find_element(*MainPageLocators.CONSTRUCTOR_DROP_AREA)
        ActionChains(self.driver).drag_and_drop(buns[0], drop_area).perform()

    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def is_order_confirmation_modal_opened(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
            )
            return True
        except Exception:
            return False

    def close_modal(self, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(MainPageLocators.CLOSE_BUTTON)
        )
        self.driver.find_element(*MainPageLocators.CLOSE_BUTTON).click()

    def wait_for_ingredients(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(MainPageLocators.INGREDIENT_ITEM)
        )

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(source, target).perform()
