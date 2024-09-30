from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    RECOVERY_LINK = By.XPATH, ".//a[text()='Восстановить пароль']"  # ссылка на страницу восстановления пароля
    PERSONAL_ACCOUNT = By.XPATH, ".//p[text()='Личный Кабинет']"  # кнопка "Личный Кабинет"
    RECOVERY_BUTTON = By.XPATH, ".//button[text()= 'Восстановить']"  # кнопка 'Восстановить'
    EMAIL_INPUT_FIELD = By.XPATH, ".//input[@name = 'name']"  # поля ввода email
    PASSWORD_INPUT_FIELD = By.XPATH, ".//input[@name='Введите новый пароль']"  # поле ввода пароля
    PASSWORD_VISIBILITY = By.XPATH, ".//div[@class='input__icon input__icon-action']"  # кнопка "Показать пароль"
    PASSWORD_FIELD_ACTIVE = By.CSS_SELECTOR, ".input.input_status_active"  # видимость пароля
