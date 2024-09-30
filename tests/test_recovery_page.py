import allure
from data import Urls
from pages.recovery_page import RecoveryPage
from helpers import TestDataHelper


class TestRecoveryPage:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_recovery_password(self, driver):
        page = RecoveryPage(driver)
        page.move_to_recovery_page()

        assert page.driver.current_url == Urls.RECOVERY_URL

    @allure.title('Проверка ввода почты и клика по кнопке «Восстановить»')
    def test_send_email_click_recovery(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.move_to_recovery_page()
        email = TestDataHelper.create_user_data()['email']
        recovery_page.send_email_input(email)
        recovery_page.click_recovery_button()

        assert recovery_page.driver.current_url == Urls.RESET_PASSWORD

    @allure.title('Проверка клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_password_visibility(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.move_to_recovery_page()
        email = TestDataHelper.create_user_data()['email']
        recovery_page.send_email_input(email)
        recovery_page.click_recovery_button()
        password = TestDataHelper.create_user_data()['password']
        recovery_page.send_password_input(password)

        assert recovery_page.check_password_visibility().is_displayed()
