from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text() = 'Конструктор']"  # кнопка "Конструктор"
    ORDER_LIST_BUTTON = By.XPATH, ".//p[contains(text(), 'Лента Заказов')]"  # кнопка "Лента заказов"
    COLLECT_BURGER_TITLE = By.XPATH, ".//h1[text()='Соберите бургер']"  # заголовок "Соберите бургер"
    BUN_INGREDIENT = By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']"  # Флюоресцентная булка R2-D3
    SAUCE_INGREDIENT = By.XPATH, ".//p[text()='Соус Spicy-X']"  # Соус Spicy-X
    FILLING_INGREDIENT = By.XPATH, ".//p[text()='Мини-салат Экзо-Плантаго']"  # Мини-салат Экзо-Плантаго
    MODAL_WINDOW = By.XPATH, ".//div[@class='Modal_modal__container__Wo2l_']"  # Модальное окно с деталями ингредиента
    CLOSE_BUTTON = By.XPATH, ".//button[contains(@class, 'close')]"  # крестик закрытия модального окна
    COUNTER = By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]"  # счетчик ингредиентов
    # конструктор (список) ингредиентов
    INGREDIENTS_LIST = By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']"

    ORDER_BUTTON = By.XPATH, "//button[contains(text(),'Оформить заказ')]"  # кнопка "Оформить заказ"
    ORDER_ID = By.XPATH, "//p[contains(text(),'идентификатор заказа')]"  # надпись "идентификатор заказа"
