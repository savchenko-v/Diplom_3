import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Переход на вкладку "Конструктор"')
    def click_to_constructor(self):
        self.wait_and_click_element(MainPageLocators.ORDER_LIST_BUTTON)
        self.wait_and_click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

        return self.wait_and_find_element(MainPageLocators.COLLECT_BURGER_TITLE)

    @allure.step('Клик на ингредиент, ожидание появления окна с деталями')
    def click_ingredient_show_window(self, ingredient):
        self.wait_and_click_element(ingredient)

        return self.wait_and_find_element(MainPageLocators.MODAL_WINDOW)

    @allure.step('Зыкрытие окна с деталями')
    def close_window_return_burger_title(self):
        self.wait_and_click_element(MainPageLocators.CLOSE_BUTTON)

        return self.wait_and_find_element(MainPageLocators.COLLECT_BURGER_TITLE)

    @allure.step('Добавить булочки')
    def add_buns(self):
        element = self.wait_and_find_element(MainPageLocators.BUN_INGREDIENT)
        target = self.wait_and_find_element(MainPageLocators.INGREDIENTS_LIST)
        self.drag_and_drop(element, target)

    @allure.step('Получение текста счётчика')
    def get_counter_text(self):
        return self.get_text(MainPageLocators.COUNTER)
