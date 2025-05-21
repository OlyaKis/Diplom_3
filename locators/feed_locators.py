from selenium.webdriver.common.by import By


class FeedLocators:
    ORDER_ITEM = (By.XPATH, "//li[1]//a[1]//div[2]")
    ORDER_MODAL = (By.XPATH, "//div[@class='Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']")
    TOTAL_DONE_ALL_TIME = (By.CSS_SELECTOR, "p.OrderFeed_number__2MbrQ")
    TOTAL_DONE_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")
    IN_ORDER_DETAILS = (By.CLASS_NAME, "OrderDetails_order__details__3Na_f")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-large")
    IN_PROGRESS_ORDER = (By.CLASS_NAME, "text_color_inactive")

