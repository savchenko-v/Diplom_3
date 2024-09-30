import allure
from data import Urls
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    @allure.step('Клик на заказ, ожидание появления окна с деталями')
    def click_order_show_window(self):
        self.wait_and_click_element(OrderPageLocators.ORDER)

        return self.wait_and_find_element(OrderPageLocators.ORDER_INFO)

    @allure.step('Получение номера заказа')
    def get_number_order_in_history_orders(self):
        return self.get_text(OrderPageLocators.NUMBER_ORDER)

    @allure.step('Подождать загрузки модального окна')
    def find_modal_window(self):
        return self.wait_and_find_element(OrderPageLocators.MODAL_WINDOW)

    @allure.step('Дождаться обновления номера заказа в окне с деталями')
    def get_order_number_in_window(self):
        WebDriverWait(self.driver, self.timer).until_not(EC.text_to_be_present_in_element(
            OrderPageLocators.NUMBER_ORDER_IN_MODAL_WINDOW, '9999'))

    @allure.step('Найти кнопку закрытия')
    def find_close_button(self):
        return self.wait_and_find_element(OrderPageLocators.CLOSE_BUTTON)

    @allure.step('Закрыть модальное окно кнопкой крестик')
    def click_close_button(self):
        return self.wait_and_click_element(OrderPageLocators.CLOSE_BUTTON)

    @allure.step('Создать заказ')
    def create_order(self):
        element = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.INGREDIENTS_LIST)
        self.drag_and_drop(element, target)
        self.wait_and_click_element(MainPageLocators.ORDER_BUTTON)
        self.find_modal_window()
        self.find_close_button()
        self.get_order_number_in_window()
        self.click_close_button()

    @allure.step('Получить номер заказа в личном кабинете в истории заказов')
    def get_order_number_in_account(self):
        self.wait_and_click_element(OrderPageLocators.PERSONAL_ACCOUNT)
        self.wait_change_url(Urls.PROFILE_URL)
        self.wait_and_click_element(OrderPageLocators.ORDER_HISTORY_BUTTON)
        order_number = self.get_number_order_in_history_orders()
        return order_number

    @allure.step('Получить номер заказа в работе')
    def get_number_order_in_work(self):
        self.click_to_order_list()
        self.wait_and_find_element(OrderPageLocators.ORDER_IN_WORK)
        return self.get_text(OrderPageLocators.ORDER_IN_WORK)

    @allure.step('Получить список заказов в ленте')
    def get_orders_list(self):
        numbers = self.wait_visibility(OrderPageLocators.ORDER_HISTORY_ALL)
        orders_list = []
        for num in numbers:
            order_number = num.text
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получить счётчик заказов')
    def get_counter_orders(self, locator):
        self.click_to_order_list()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self.get_text(locator)
