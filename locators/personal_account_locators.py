from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"  # кнопка "Личный Кабинет"
    EMAIL_INPUT_FIELD = By.XPATH, ".//input[@name = 'name']"  # поля ввода email
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name='Пароль']"  # поле ввода пароля
    LOGIN_SUBMIT_BUTTON = By.XPATH, ".//button[text()='Войти']"  # кнопка "Войти" в форме входа
    EXIT_BUTTON = By.XPATH, ".//button[text()='Выход']"  # кнопка "Выход" в личном кабинете
    ORDER_HISTORY_BUTTON = By.XPATH, ".//a[text()='История заказов']"  # кнопка "История заказов" в личном кабинете
