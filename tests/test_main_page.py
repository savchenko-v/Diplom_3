import allure
import pytest
from data import Urls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_click_to_constructor(self, driver):
        main_page = MainPage(driver)
        burger_title = main_page.click_to_constructor()

        assert main_page.driver.current_url == Urls.BASE_URL and burger_title.is_displayed()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_click_to_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_order_list()

        assert main_page.driver.current_url == Urls.ORDER_LIST

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @pytest.mark.parametrize('ingredient', [
        MainPageLocators.BUN_INGREDIENT,
        MainPageLocators.SAUCE_INGREDIENT,
        MainPageLocators.FILLING_INGREDIENT
    ])
    def test_click_to_ingredient(self, driver, ingredient):
        main_page = MainPage(driver)
        modal_window = main_page.click_ingredient_show_window(ingredient)

        assert modal_window.is_displayed()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient_show_window(MainPageLocators.BUN_INGREDIENT)

        assert main_page.close_window_return_burger_title().is_displayed()

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_check_counter(self, driver):
        main_page = MainPage(driver)
        main_page.add_buns()

        assert main_page.get_counter_text() == '2'

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_create_order(self, driver, login):
        main_page = MainPage(login)
        main_page.add_buns()
        main_page.wait_and_click_element(MainPageLocators.ORDER_BUTTON)
        order_id_text = main_page.wait_and_find_element(MainPageLocators.ORDER_ID)

        assert order_id_text.is_displayed()
