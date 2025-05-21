from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):

    def click_logout(self):
        self.click(ProfileLocators.LOGOUT_BUTTON)

    def click_profile_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(ProfileLocators.MODAL_OVERLAY)
        )
        self.click(ProfileLocators.PROFILE_BUTTON)

    def click_order_history(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(ProfileLocators.MODAL_OVERLAY)
        )
        self.click(ProfileLocators.ORDER_HISTORY_BUTTON)

    def is_order_history_displayed(self):
        return self.is_visible(ProfileLocators.ORDER_HISTORY_BUTTON)
