class LocatorsSite:

    # кнопка Войти в аккаунт на главной
    BUTTON_LOGIN_TO_ACCOUNT = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"

    # кнопка Личный кабинет на главной
    BUTTON_PERSONAL_ACCOUNT = ".//a[@class='AppHeader_header__link__3D_hX' and @href='/account']"

    # кнопка Войти на странице авторизации
    BUTTON_LOGIN = ".//button[text()='Войти']"

    # кнопка зарегистрироваться на странице авторизации
    BUTTON_REGISRET = ".//a[@class='Auth_link__1fOlj' and @href='/register']"

    # кнопка восстановить пароль на странице авторизации
    BUTTON_RECOVER_PASSWORD = ".//a[@class ='Auth_link__1fOlj' and @href='/forgot-password']"

    # кнопка зарегистрироваться на странице регистрации
    BUTTON_REGISRET_ACCOUNT = ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"

    # кнопка войти на странице регистрации
    BUTTON_LOGIN_IN_REGISRET = ".//a[text()='Войти']"

    # кнопка войти на странице восстановления пароля
    BUTTON_LOGIN_IN_RECOVERY_PASSWORD = ".//a[@class ='Auth_link__1fOlj' and @href='/login']"

    # лого бургерной
    LOGO_BURGER = ".//div[@class='AppHeader_header__logo__2D0X2']"

    # кнопка контрукто'
    BUTTON_CONSTRUCTOR = ".//a[@class='AppHeader_header__link__3D_hX']"

    # логотип Соберите Бургер
    LOGO_COLLECT_BURGER = ".//h1[@class='text text_type_main-large mb-5 mt-10']"

    # поле ввода Имя
    INPUT_NAME = ".//label[text()='Имя']/following-sibling::input"

    # поле ввода email
    INPUT_EMAIL = ".//label[text()='Email']/following-sibling::input"

    # поле ввода Пароль
    INPUT_PASSWORD = ".//label[text()='Пароль']/following-sibling::input"

    # поле с Логинов в личном кабинете
    INPUT_LOGIN = ".//label[text()='Логин']/following-sibling::input"

    # кнопка Выйти из личного кабинета
    OUT_BUTTON = ".//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"

    # кнопка Булки
    BUTTON_ROLLS = ".//span[text()='Булки']"
    PARENTS_BUTTON_ROLLS = ".//span[text()='Булки']/parent::div"

    # кнопка Соусы
    BUTTON_SAUSES = ".//span[text()='Соусы']"
    PARENTS_BUTTON_SAUSES = ".//span[text()='Соусы']/.."

    # кнопка Начинки
    BUTTON_TOPPINGS = ".//span[text()='Начинки']"
    PARENTS_BUTTON_TOPPINGS = ".//span[text()='Начинки']/.."

    # плашка с текстом о неверном пароле
    ERROR_PASSWORD = ".//p[@class='input__error text_type_main-default']"