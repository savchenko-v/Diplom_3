import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from locators.personal_account_locators import PersonalAccountLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timer = 10

    @allure.step('Ожидание загрузки и поиск элемента на странице')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, self.timer).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание загрузки и клик по элементу')
    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, self.timer).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ожидание смены адреса')
    def wait_change_url(self, url):
        WebDriverWait(self.driver, self.timer).until(EC.url_to_be(url))

    @allure.step('Ожидание загрузки и внесение данных')
    def wait_and_send_keys(self, locator, text):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Ввести email')
    def send_email_input(self, email):
        self.wait_and_send_keys(PersonalAccountLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('Ввести пароль')
    def send_password_input(self, password):
        self.wait_and_send_keys(PersonalAccountLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('Авторизация')
    def login_user(self, email, password):
        self.send_email_input(email)
        self.send_password_input(password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(PersonalAccountLocators.LOGIN_SUBMIT_BUTTON))
        self.wait_and_click_element(PersonalAccountLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Подождать загрузки элемента')
    def wait_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, element, target):
        return ActionChains(self.driver).drag_and_drop(element, target).perform()

    @allure.step('Переход на вкладку "Лента заказов"')
    def click_to_order_list(self):
        self.scroll_to_element(MainPageLocators.ORDER_LIST_BUTTON)
        self.wait_and_click_element(MainPageLocators.ORDER_LIST_BUTTON)

    @allure.title('Прокрутка до указанного элемента')
    def scroll_to_element(self, element):
        element = self.wait_and_find_element(element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
