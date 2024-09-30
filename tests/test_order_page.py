import allure
import pytest
from data import Urls
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_to_order(self, driver):
        order_page = OrderPage(driver)
        order_page.click_to_order_list()

        modal_window = order_page.click_order_show_window()

        assert modal_window.is_displayed()

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_in_order_list(self, driver, create_and_delete_user, login):
        order_page = OrderPage(login)
        order_page.create_order()
        order_number = order_page.get_order_number_in_account()
        orders_in_order_list = order_page.get_orders_list()

        assert order_number in orders_in_order_list

    @pytest.mark.parametrize('counter', [OrderPageLocators.COUNTER_TOTAL, OrderPageLocators.COUNTER_DAILY])
    @allure.title('При создании нового заказа счётчик Выполнено за всё время/за сегодня увеличивается')
    def test_counter_increase(self, driver, create_and_delete_user, login, counter):
        order_page = OrderPage(login)
        counter_before = int(order_page.get_counter_orders(counter))
        order_page.wait_and_click_element(OrderPageLocators.CONSTRUCTOR_BUTTON)
        order_page.wait_change_url(Urls.BASE_URL)
        order_page.create_order()
        counter_after = int(order_page.get_counter_orders(counter))

        assert counter_after > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_user_order_in_work(self, driver, create_and_delete_user, login):
        order_page = OrderPage(login)
        order_page.create_order()
        order_number = order_page.get_order_number_in_account()[1:]
        orders_in_work = order_page.get_number_order_in_work()

        assert order_number in orders_in_work
