import allure
from data import Urls
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators


class RecoveryPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def move_to_recovery_page(self):
        self.wait_and_click_element(RecoveryPageLocators.PERSONAL_ACCOUNT)
        self.wait_and_click_element(RecoveryPageLocators.RECOVERY_LINK)

    @allure.step('Клик по кнопке восстановления')
    def click_recovery_button(self):
        self.wait_and_click_element(RecoveryPageLocators.RECOVERY_BUTTON)
        self.wait_change_url(Urls.RESET_PASSWORD)

    @allure.step('Ввести пароль')
    def send_password_input(self, password):
        self.wait_and_send_keys(RecoveryPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Проверка видимости пароля')
    def check_password_visibility(self):
        self.wait_and_find_element(RecoveryPageLocators.PASSWORD_VISIBILITY).click()
        return self.wait_and_find_element(RecoveryPageLocators.PASSWORD_FIELD_ACTIVE)
