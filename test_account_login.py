import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# вход по кнопке «Войти в аккаунт» на главной
def test_with_button_entrance_in_account(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button"))) # ожидаем кликабильности кнопки регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click() # зарегистрировали аккаунт

    driver.get("https://stellarburgers.nomoreparties.site/") # перешли на главную
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
    entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/section[2]/div/button')))
    entrance.click() # ждем кликабильности кнопки Войти в аккаунт и нажимаем на нее

    # авторизуемся
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')))
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click() # кнопка Войти

    #проверяем вход в аккаунт в личном кабинете
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))  # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    check_email = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")))  # ожидаем видимости поля с логином и сохраняем в переменную
    value = check_email.get_attribute('value')  # сохранили значение атрибута

    assert r_random_email.upper() == value.upper()  # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра

# вход через кнопку «Личный кабинет»
def test_entrance_personal_account_button(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button")))  # ожидаем кликабильности кнопки регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()  # зарегистрировали аккаунт

    driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
    entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))
    entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее

    # авторизуемся
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')))
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()  # кнопка Войти

    # проверяем вход в аккаунт в личном кабинете
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))  # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    check_email = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")))  # ожидаем видимости поля с логином и сохраняем в переменную
    value = check_email.get_attribute('value')  # сохранили значение атрибута

    assert r_random_email.upper() == value.upper()  # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра

# вход через кнопку в форме регистрации
def test_entrance_in_the_registration_form(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button")))  # ожидаем кликабильности кнопки регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()  # зарегистрировали аккаунт

    driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
    entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))
    entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click() # кнопка Зарегистрироваться
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click() # кнопка Войти

    # авторизуемся
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')))
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()  # кнопка Войти

    # проверяем вход в аккаунт в личном кабинете
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))  # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    check_email = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")))  # ожидаем видимости поля с логином и сохраняем в переменную
    value = check_email.get_attribute('value')  # сохранили значение атрибута

    assert r_random_email.upper() == value.upper()  # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра

# вход через кнопку в форме восстановления пароля
def test_entrance_in_the_password_recovery_form(setup_registration, random_email):
    driver = setup_registration
    r_random_email = random_email()
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("andrey")
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("123456")
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/div/form/button")))  # ожидаем кликабильности кнопки регистрации
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()  # зарегистрировали аккаунт

    driver.get("https://stellarburgers.nomoreparties.site/")  # перешли на главную
    WebDriverWait(driver, 3).until(expected_conditions.url_to_be('https://stellarburgers.nomoreparties.site/'))
    entrance = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))
    entrance.click()  # ждем кликабильности кнопки Личный кабинет и нажимаем на нее
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[2]/a").click() # кнопка Восстановить пароль
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p/a").click() # кнопка Войти

    # авторизуемся
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')))
    driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(r_random_email)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys("123456")
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()  # кнопка Войти

    # проверяем вход в аккаунт в личном кабинете
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '/html/body/div/div/header/nav/a/p')))  # Подождали загрузки кнопки ЛК на главной
    driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p').click()  # перешли в личный кабинет
    check_email = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input")))  # ожидаем видимости поля с логином и сохраняем в переменную
    value = check_email.get_attribute('value')  # сохранили значение атрибута

    assert r_random_email.upper() == value.upper()  # проверили, что созданный логин совпадает с введенным при регистрации и учитываем возможность расхождения регистра