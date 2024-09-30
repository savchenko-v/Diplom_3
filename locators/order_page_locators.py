from selenium.webdriver.common.by import By


class OrderPageLocators:
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"  # кнопка "Личный Кабинет"
    ORDER_HISTORY_BUTTON = By.XPATH, './/a[contains(text(), "История заказов")]'  # кнопка "История заказов"
    ORDER_LIST_BUTTON = By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"  # кнопка "Лента заказов"
    ORDER = By.XPATH, './/*[contains(@class, "OrderHistory_link")]'  # заказ в ленте
    ORDER_INFO = By.XPATH, './/p[text()="Cостав"]'  # детали заказа
    ORDER_HISTORY_ALL = By.XPATH, './/p[contains(@class, "text_type_digits-default")]'  # все заказы в ленте заказов
    ORDER_IN_WORK = By.XPATH, ".//li[contains(@class, 'text text_type_digits-default mb-2')]"  # заказы "В работе"
    # счетчик заказов за все время
    COUNTER_TOTAL = By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"
    COUNTER_DAILY = By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"  # счетчик заказов за сегодня
    NUMBER_ORDER = By.XPATH, ".//p[@class='text text_type_digits-default']"  # номер заказа
    CLOSE_BUTTON = By.XPATH, ".//button[contains(@class, 'close')]"  # крестик закрытия модального окна
    MODAL_WINDOW = By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']"  # модальное окно заказа
    # номер заказа в модальном окне
    NUMBER_ORDER_IN_MODAL_WINDOW = By.XPATH, './/section[contains(@class, "Modal_modal_opened")]//h2'
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']"  # кнопка "Конструктор"
