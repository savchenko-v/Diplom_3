import allure
from data import Urls
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):

    @allure.step('Переход в «Личный кабинет», обнаружение кнопки выхода из аккаунта')
    def move_and_return_exit_button(self):
        self.wait_and_click_element(PersonalAccountLocators.PERSONAL_ACCOUNT)

        return self.wait_and_find_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Переход в раздел «История заказов»')
    def move_to_order_history(self):
        self.wait_and_click_element(PersonalAccountLocators.PERSONAL_ACCOUNT)
        self.wait_and_click_element(PersonalAccountLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Выход из аккаунта')
    def exit_from_account(self):
        self.wait_and_click_element(PersonalAccountLocators.PERSONAL_ACCOUNT)
        self.wait_and_click_element(PersonalAccountLocators.EXIT_BUTTON)
        self.wait_change_url(Urls.LOGIN_USER)
