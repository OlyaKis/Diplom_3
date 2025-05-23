from selenium.webdriver.common.by import By


class ProfileLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_BUTTON = (
        By.XPATH, "//a[contains(@href, '/account/order-history') and contains(text(), 'История заказов')]"
    )
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
