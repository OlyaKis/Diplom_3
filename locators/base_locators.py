from selenium.webdriver.common.by import By


class BaseLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    MAIN_LOGO = (By.XPATH, "//*[@id=root']/div/header/nav/div/a")
