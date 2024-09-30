class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    INFO_USER = f'{BASE_URL}auth/user'
    LOGIN_USER = f'{BASE_URL}login'

    RECOVERY_URL = f'{BASE_URL}forgot-password'
    RESET_PASSWORD = f'{BASE_URL}reset-password'
    PROFILE_URL = f'{BASE_URL}account/profile'

    CREATE_USER_API = f'{BASE_URL}api/auth/register'
    CREATE_ORDER_API = f'{BASE_URL}/api/orders'
    GET_ORDERS_API = f'{BASE_URL}/api/orders'

    ORDER_HISTORY = f'{BASE_URL}account/order-history'
    ORDER_LIST = f'{BASE_URL}feed'
