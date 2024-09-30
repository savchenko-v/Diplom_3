import allure
from data import Urls
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Переход по клику на «Личный кабинет»')
    def test_move_to_account(self, login, driver):
        personal_page = PersonalAccountPage(login)

        assert personal_page.move_and_return_exit_button().is_displayed()

    @allure.title('Переход в раздел «История заказов»')
    def test_move_to_order_history(self, login, driver):
        personal_page = PersonalAccountPage(login)
        personal_page.move_to_order_history()

        assert personal_page.driver.current_url == Urls.ORDER_HISTORY

    @allure.title('Проверка выхода из аккаунта')
    def test_exit_from_account(self, login, driver):
        personal_page = PersonalAccountPage(login)
        personal_page.exit_from_account()

        assert personal_page.driver.current_url == Urls.LOGIN_USER
