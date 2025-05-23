from selenium.webdriver.common.by import By


class MainPageLocators:
    INGREDIENTS = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients')]")
    INGREDIENT_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_DETAILS_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "(//div[contains(@class, 'counter_counter__') and contains(@class, 'counter_default__')])[1]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    BUN_ITEM = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')][.//img[contains(@alt, 'булка')]]")
    MODAL_WINDOW = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    CONSTRUCTOR_DROP_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    CLOSE_MODAL = (By.CLASS_NAME, "OrderDetails_order__details__3Na_f")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")

